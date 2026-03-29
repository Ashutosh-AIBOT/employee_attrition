# Employee Attrition Prediction

Workforce risk analytics for retention strategy.

## Recommended GitHub Repo Name

employee-attrition-risk-intelligence

## Domain

HR analytics and workforce planning

## Objective

Predict attrition likelihood to prioritize retention interventions.

## Business Value

Improves talent retention, cuts replacement cost, and supports workforce continuity.

## Dataset

Verified: https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset

## Run Locally

conda run -n ml-env streamlit run app.py

## Dashboard Features

- Executive overview and business framing
- Prediction Center (single input + batch CSV)
- Model ranking leaderboard
- Model registry (all discovered model artifacts)
- Charts gallery (auto-load from charts/)
- Notebook traceability panel

## Notebook Path Setup

Inside notebooks:

from path_setup import BASE, RAW, PROCESSED, MODELS, CHARTS, load_raw_csv

Project path helpers:

- path_utils.py
- notebooks/path_setup.py
## Deploy on Render

This repo includes render.yaml. Connect repo in Render and deploy.

Start command used:

streamlit run app.py --server.port $PORT --server.address 0.0.0.0

## Git LFS

Large assets are tracked with Git LFS (models, charts, data artifacts).
