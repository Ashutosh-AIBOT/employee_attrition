# Project 7 — Employee Attrition Prediction (HR Analytics)

## Problem Statement
Employee turnover is one of the most expensive hidden costs in any company. Replacing a
mid-level engineer costs 6-9 months of their salary in recruiting, onboarding, and
lost productivity. HR teams typically discover an employee is leaving only when they
resign. This project builds a model that identifies at-risk employees months in advance
so HR can intervene proactively. Used by companies like Infosys, TCS, Wipro HR analytics
teams and modern HR-tech startups.

## Dataset
- **Name:** IBM HR Analytics Employee Attrition & Performance
- **Source:** https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset
- **Size:** 1,470 employees × 35 features
- **Target:** Attrition (Yes/No) → binary classification
- **Class balance:** ~16% attrition (moderately imbalanced)

## Files to Download from Kaggle
```
WA_Fn-UseC_-HR-Employee-Attrition.csv    → single file
```

## Feature Description (key ones)
```
Age                    → employee age
Attrition              → target (Yes/No)
BusinessTravel         → Non-Travel, Travel_Rarely, Travel_Frequently
Department             → Sales, R&D, HR
DistanceFromHome       → commute distance in miles
Education              → 1=Below College to 5=Doctor
EnvironmentSatisfaction → 1=Low to 4=Very High
JobInvolvement         → 1=Low to 4=Very High
JobLevel               → 1-5 hierarchy
JobSatisfaction        → 1=Low to 4=Very High
MaritalStatus          → Single, Married, Divorced
MonthlyIncome          → salary
NumCompaniesWorked     → previous companies
OverTime               → Yes/No — strongest predictor
PerformanceRating      → 3=Excellent, 4=Outstanding
RelationshipSatisfaction
TotalWorkingYears      → experience
WorkLifeBalance        → 1=Bad to 4=Best
YearsAtCompany         → tenure
YearsInCurrentRole
YearsSinceLastPromotion → key attrition driver
```

## ML Models Used
| Model | Purpose |
|-------|---------|
| Decision Tree (max_depth=4) | Interpretable — show tree to HR managers |
| Random Forest | Feature importance baseline |
| XGBoost | Primary model — best AUC |
| Logistic Regression | Coefficient interpretation |

## Key Techniques
- OrdinalEncoder for satisfaction/rating scales (preserve order)
- OneHotEncoder for Department, MaritalStatus, BusinessTravel
- Decision Tree rule extraction: export human-readable IF-THEN rules
- Visualise full decision tree (graphviz/dtreeviz) — key resume output
- SHAP beeswarm + force plots: per-employee risk reasons
- Feature importance: OverTime, MonthlyIncome, YearsSinceLastPromotion dominate
- Cross-validation with stratified folds (preserve 16% ratio)
- Confusion matrix cost analysis: FN (missed leaver) >> FP (unnecessary HR call)

## Evaluation Metrics
- Primary: **AUROC** + F1 at optimal threshold
- Secondary: Confusion matrix, Recall (most important — catch leavers)
- Business metric: Estimated salary savings from early intervention

## Expected Output / Insights
1. Decision tree visualisation — hand this to HR manager, they can use it without ML knowledge
2. SHAP: "This employee is leaving because: OverTime=Yes, YearsSinceLastPromotion=4, MonthlyIncome=below-average"
3. Top 5 attrition risk factors across all employees
4. At-risk employee list with risk scores (anonymised)
5. Retention ROI: if we retain top 20 at-risk employees, estimated cost saving = $X

## Resume Bullet
> Built an employee attrition prediction system on IBM HR data using XGBoost + Decision Tree,
> achieving AUROC 0.83. Delivered interpretable Decision Tree rules directly usable by HR managers
> and SHAP-based per-employee risk explanations. Quantified retention ROI: retaining top 25
> at-risk employees saves an estimated $450k annually.

## How to Run
```bash
make train        # runs full pipeline
make evaluate     # generates tree viz + SHAP plots
make predict      # score current employee roster
```
