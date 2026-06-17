# AI-Based Smart Network Traffic Analyzer

## Overview

This project uses Machine Learning to analyze network traffic and classify connections as Normal or Attack traffic.

## Features

* Network traffic anomaly detection
* Random Forest Machine Learning model
* Interactive Streamlit dashboard
* Traffic visualization
* Prediction statistics

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Joblib

## Dataset

NSL-KDD Intrusion Detection Dataset

## Model Performance

* Algorithm: Random Forest Classifier
* Accuracy: 99.76%

## Project Structure

AI_Network_Traffic_Analyzer/

* dataset/
* models/
* reports/
* screenshots/
* train_model.py
* app.py
* requirements.txt
* README.md

## Installation

pip install -r requirements.txt

## Run Model Training

python train_model.py

## Run Dashboard

streamlit run app.py

## Future Improvements

* Real-time packet capture using Scapy
* Live threat detection
* Email alerts for suspicious traffic
* Advanced attack classification
