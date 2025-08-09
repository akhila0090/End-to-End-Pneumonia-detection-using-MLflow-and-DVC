# End-to-End-Pneumonia detection pipeline using MLflow and DVC

## Objective

The goal of this project is to develop, track, and deploy a pneumonia detection model using chest X-ray images. The model is built using DenseNet121 for high-accuracy feature extraction and classification. The entire workflow integrates MLflow for experiment tracking, DVC for data and pipeline management, and AWS CICD for automated deployment.

---
## 1. Project Setup and Configuration
- Organized the project with:
  - `config.yaml` for all paths and global settings  
  - `params.yaml` for hyperparameters like batch size, learning rate, and epochs   
- Created entity classes for structured configuration handling.  
- Implemented a Configuration Manager in `src/config` to load settings.  
- Built components for:
  - Data ingestion
  - Base model preperatin
  - Model training
  - Model evaluation  
- Linked components into pipelines for automation.  
- Added `main.py` to trigger pipelines and updated `dvc.yaml` to define the DVC pipeline stages.

---

## 2. Model Development with DenseNet121
- Selected **DenseNet121**, pre-trained on ImageNet, for strong feature extraction from chest X-ray images.  
- Removed top classification layers and replaced them with custom layers for binary classification (Pneumonia vs. Normal).  
- Fine-tuned top DenseNet layers to improve accuracy.  
- Evaluated model using metrics:
  - Accuracy
  - Precision
  - Recall
 
---

## 3. Experiment Tracking with MLflow
- Integrated MLflow to:
  - Log parameters, metrics, and confusion matrices  
  - Store trained DenseNet121 model artifacts  
  - Tag model versions  
- Configured **DagsHub** as the remote MLflow tracking server.  
- Used `mlflow ui` to visualize and compare experiments.  
- Set environment variables to push experiment logs to the remote server.

---

## 4. Data Version Control with DVC
- Initialized DVC to manage datasets and pipeline stages.  
- Ensured reproducibility by versioning all data and models.  
- Used:
  - `dvc repro` to rerun the pipeline from any stage  
  - `dvc dag` to visualize the workflow  
- Simplified collaboration and maintained a clear experiment history.
  
---

## 5. Deployment with AWS and GitHub Actions
- Used an **automated CI/CD pipeline** with GitHub Actions and AWS services.  
- Configured an **EC2 instance** as a self-hosted GitHub Actions runner.  
- During the pipeline:
  - builds the Docker image for the model inference service.  
  - The image is pushed to AWS **ECR**.  
  - EC2 pulls the image from ECR and runs it as a container to serve predictions.  
- Applied IAM policies:
  - AmazonEC2FullAccess
  - AmazonEC2ContainerRegistryFullAccess  
- Stored AWS credentials and configuration details as GitHub Secrets.
---

## 6. Web Application for Pneumonia Detection
- Developed a **Flask-based web application** for user interaction.  
- Allows uploading of chest X-ray images to predict whether the case is normal or pneumonia.  
- Uses the trained DenseNet121 model for predictions via a REST API and HTML front-end.  
- Runs locally using `app.py` during development.  
- Configured to listen on a custom port in AWS after CICD deployment.
- 
<img width="1375" height="990" alt="Screenshot (398)" src="https://github.com/user-attachments/assets/067f5ea2-a742-42d3-b3ab-03c176947501" />

---

## Outcome
- Production-ready pneumonia detection system using DenseNet121.  
- Automated training and evaluation pipelines with DVC.  
- Experiment tracking and model versioning using MLflow.  
- Fully automated deployment to AWS using Docker and GitHub Actions.  
- User-friendly web application for real-time pneumonia detection from chest X-ray images.

---

## Key Tools and Technologies
- Python (data handling and model training)  
- TensorFlow / Keras (DenseNet121 transfer learning)  
- MLflow (experiment tracking)  
- DVC (data and pipeline version control)  
- Docker (containerization)  
- AWS ECR and EC2 (cloud deployment)  
- GitHub Actions (CICD automation)  
- DagsHub (remote MLflow server)  
- Flask (web application framework)  







