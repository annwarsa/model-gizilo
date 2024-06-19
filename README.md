# Machine Learning Model Gizilo
This repository contains machine learning for gizilo apps. The modles include image classification and nutrition grade system.

# Models Image
We pre trained models and do fine tune transfer learning. We also try build from scratch without help pre trained models

| Model       | Accuracy | Val Accuracy |
|-------------|----------|--------------|
| InceptionV3 | ??       | ??           |
| Resnet50V2  | 1.00     | 0.63         |


# Models Nutrition 
We trained nutrition models from scratch without help pre trained models.

| Model       | Accuracy | Val Accuracy |
|-------------|----------|--------------|
| Model       | 0.97     | 0.99         |

# Dataset
We have to datset, one image and another one is nutrition list.
| Dataset   | Link                                                                         |
|-----------|------------------------------------------------------------------------------|
| Image     | [Datset](https://github.com/giziloid/model-gizilo/tree/master/dataset-image) |
| Nutrition | [Dataset](https://github.com/giziloid/model-gizilo/tree/master/dataset-nutrition) |

# How to reproduce this model
To reproduce this model you can follow this step:
1. Download what model you cen reproduce 
| Type      | Dataset Link                                                                                   | Model Link                                                                                             |
|-----------|------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| Nutrition | [Data](https://github.com/giziloid/model-gizilo/blob/master/models-nutrition/clean_data.csv) | [Train Notebook](https://github.com/giziloid/model-gizilo/blob/master/models-nutrition/train_nutrition.ipynb) |
| Image (Resnet50V2) | Link included in notebook | [Train Notebook](https://github.com/giziloid/model-gizilo/blob/master/models-image/resnet50v2/resnet50v2.ipynb) |

2. Now after download the notebook and dataset you upload the notebook and dataset to use Kagggle or Google Collab for free resource training.
3. After that you can run the kernel and run each cell.

# Deployment nutrition model using docker 
