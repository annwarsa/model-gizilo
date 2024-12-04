from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sklearn.preprocessing import LabelEncoder
from starlette.responses import JSONResponse
from typing import Any, List, Dict
from dotenv import load_dotenv
import tensorflow as tf
import pandas as pd
import numpy as np
import os
import logging

logger = logging.getLogger(__name__)
    
def init_model():
    try:
        le = LabelEncoder()
        df = pd.read_csv('clean_data.csv')
        le.fit(df['grade'])
    except FileNotFoundError:
        raise RuntimeError("clean_data.csv not found. Ensure the file is present in the expected directory.")
    except Exception as e:
        raise RuntimeError(f"Error loading clean_data.csv: {str(e)}")
    
    try:
        model = tf.keras.models.load_model("nutrient.h5")
    except FileNotFoundError:
        raise RuntimeError("nutrient.h5 not found. Ensure the file is present in the expected directory.")
    except Exception as e:
        raise RuntimeError(f"Error loading nutrient.h5: {str(e)}")
    
    return le, model


class BaseAPI:
    def __init__(self):
        self.app = FastAPI()
        self.setup_api()
        self.setup_middleware()
        self.le, self.model = init_model()  
    
    def setup_api(self):
        self.app.post("/api/v1/nutrient")(self.process_nutrient)
    
    async def process_nutrient(self, request: Request):
        try:
            body = await request.json()
            print(body)
            known_keys = {'fat', 'sugar', 'sodium'}
            val_input = [body[k] for k in body if k in known_keys]
            if len(val_input) != 3:
                raise HTTPException(status_code=400, detail=f"Please provide values for 'fat', 'sugar', and 'sodium' keys{body}")
            val_input_arr = np.array(val_input, dtype=np.float32).reshape(1, -1)
        
            predictions = self.model.predict(val_input_arr)
            predicted_class = self.le.inverse_transform(np.argmax(predictions, axis=1))[0]
        
            return JSONResponse(content={"result": predicted_class})
        
        except KeyError:
            raise HTTPException(status_code=400, detail="Invalid keys provided in JSON data")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
    def setup_middleware(self):
        load_dotenv()
        allowed_origins = os.getenv("allowed_origins", "").split(",")
        
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=allowed_origins,
            allow_credentials=True,
            allow_methods=["POST"],
            allow_headers=["Content-Type"]
        )
        
        
        
        async def log_request(request: Request, call_next):
            logger.info(f"Incoming request: {request.method} {request.url}, headers: {request.headers}, body: {await request.body()}")

            response = await call_next(request)

            return response
        
        self.app.middleware("http")(log_request)

base_api = BaseAPI()
