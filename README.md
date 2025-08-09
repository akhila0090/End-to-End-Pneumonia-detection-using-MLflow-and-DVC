# End-to-End-Pneumonia detection pipeline using MLflow and DVC

## Objective

The goal of this project is to develop, track, and deploy a pneumonia detection model using chest X-ray images. The model is built using DenseNet121 for high-accuracy feature extraction and classification. The entire workflow integrates MLflow for experiment tracking, DVC for data and pipeline management, and AWS CICD for automated deployment.

---

## 1. Project Setup and Configuration
The project is organized with configuration files such as `config.yaml` for all paths and global settings, `params.yaml` for hyperparameters like batch size, learning rate, and epochs.
Entity classes are created for structured configuration handling, and a Configuration Manager is implemented in `src/config` to load settings.  
Components are built for data ingestion, data transformation, model training, and model evaluation.  
These components are linked into pipelines for automation, with `main.py` used to trigger the pipelines and `dvc.yaml` updated to define the DVC pipeline stages.

---

## 2. Model Development with DenseNet121
DenseNet121, pre-trained on ImageNet, is selected for its strong feature extraction capabilities on chest X-ray images.  
The top classification layers are removed and replaced with custom layers for binary classification (Pneumonia vs. Normal).  
Top DenseNet layers are fine-tuned to improve accuracy.
Evaluation metrics include Accuracy, Precision and Recall.

---

## 3. Experiment Tracking with MLflow
MLflow is integrated to log parameters, metrics, and confusion matrices, as well as to store trained DenseNet121 model artifacts and tag model versions.  
DagsHub is configured as the remote MLflow tracking server.  
Using `mlflow ui`, experiments can be visualized and compared.  
Environment variables are set to push experiment logs to the remote server.

---

## 4. Data Version Control with DVC
DVC is initialized to manage datasets and pipeline stages, ensuring that all data and models are versioned for reproducibility.  
The `dvc repro` command is used to rerun the pipeline.  
This setup helps maintain clear experiment history and simplifies collaboration.  
It also ensures that the workflow can be reproduced at any stage.

---

## 5. Deployment with AWS and GitHub Actions
The trained DenseNet121 model is deployed using an automated CI/CD pipeline with GitHub Actions and AWS services.  
As part of the pipeline, the EC2 instance configured as a self-hosted GitHub Actions runner that builds the Docker image for the model inference service and pushes it to AWS ECR.  
Then it pulls the image from ECR and runs it as a container to serve predictions.  
IAM policies such as AmazonEC2FullAccess and AmazonEC2ContainerRegistryFullAccess are applied, and GitHub Secrets store AWS credentials and configuration details.

---

## 6. Web Application for Pneumonia Detection
A Flask-based web application is developed to provide an interface for uploading chest X-ray images and predicting whether the image indicates pneumonia or a normal condition.  
The application uses the trained DenseNet121 model and exposes a prediction API along with an HTML front-end for ease of use.  
It is run locally using `app.py` during development and configured to listen on a custom port when deployed to AWS after the CICD process.  


<img width="1375" height="990" alt="Screenshot (398)" src="https://github.com/user-attachments/assets/067f5ea2-a742-42d3-b3ab-03c176947501" />

---

## Outcome
The result is a production-ready pneumonia detection system that uses DenseNet121 for robust chest X-ray classification.  
It automates training and evaluation pipelines with DVC, tracks all experiments with MLflow, and deploys seamlessly to AWS using Docker and GitHub Actions.  
A user-friendly web application enables real-time predictions through a browser interface.  
This setup ensures reproducibility, scalability, and maintainability for real-world applications in medical imaging.

---

## Key Tools and Technologies
Python (data handling and model training)  
TensorFlow / Keras (DenseNet121 transfer learning)  
MLflow (experiment tracking)  
DVC (data and pipeline version control)  
Docker (containerization)  
AWS ECR and EC2 (cloud deployment)  
GitHub Actions (CICD automation)  
DagsHub (remote MLflow server)  
Flask (web application framework)  








