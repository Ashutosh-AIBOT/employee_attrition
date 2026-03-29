import os

from dashboard_core import ProjectConfig, run_project_app


CONFIG = ProjectConfig(
    key="Project 07",
    title="Employee Attrition Prediction",
    subtitle="Workforce risk analytics for retention strategy",
    icon="👥",
    domain="HR analytics and workforce planning",
    objective="Predict attrition likelihood to prioritize retention interventions.",
    business_value="Improves talent retention, cuts replacement cost, and supports workforce continuity.",
    prediction_label="Attrition Risk",
    highlights=[
        "Transforms HR data into proactive retention intelligence for managers.",
        "Supports model-driven intervention prioritization for high-risk employee groups.",
        "Uses clear benchmark reporting to align HR and analytics stakeholders.",
        "Enables practical, non-technical use with clean prediction workflows.",
        "Demonstrates business translation from metrics to people strategy outcomes.",
    ],
)


run_project_app(CONFIG, os.path.dirname(__file__))
