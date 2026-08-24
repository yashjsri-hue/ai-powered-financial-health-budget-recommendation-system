# AI-Powered Personal Finance & Budget Recommendation System

## 📌 Project Overview

The **AI-Powered Personal Finance & Budget Recommendation System** is a Data Science and Machine Learning project designed to analyze personal financial data, assess financial health, and generate personalized financial recommendations.

The system combines **Python, Pandas, Machine Learning, and Streamlit** to transform financial data into actionable insights.

It classifies users into different financial-health categories and generates personalized recommendations based on savings, expenses, debt, EMI, emergency funds, and credit-related indicators.

---

## 🎯 Project Objectives

The main objectives of this project are:

* Analyze personal financial information.
* Clean and preprocess financial data.
* Calculate important financial indicators.
* Predict financial health using Machine Learning.
* Generate personalized AI-based financial recommendations.
* Assign recommendation categories and priorities.
* Calculate a recommendation score from 0–100.
* Provide an interactive financial dashboard.
* Help users identify areas requiring financial improvement.

---

## 🏗️ Project Workflow

```text
Raw Financial Dataset
        ↓
Data Cleaning & Preprocessing
        ↓
Financial Data Analysis
        ↓
Financial Health Prediction
        ↓
AI/ML Recommendation Engine
        ↓
Personalized Recommendations
        ↓
Interactive Streamlit Dashboard
        ↓
Testing & Validation
```

---

## 📂 Project Modules

### Step 1 — User Financial Data

The project starts with a synthetic personal-finance dataset containing financial information for individual users.

The dataset contains:

* User information
* Income
* Expenses
* Savings
* Debt
* EMI
* Credit-related information
* Emergency-fund information
* Financial ratios and indicators

---

### Step 2 — Data Cleaning & Storage

The raw financial dataset is processed to prepare it for analysis and Machine Learning.

Major activities include:

* Handling missing values
* Checking duplicate records
* Correcting data types
* Validating financial fields
* Creating derived financial indicators
* Preparing the processed dataset for further analysis

---

### Step 3 — Financial Data Analysis

Important financial indicators are analyzed to understand user financial behavior.

Key indicators include:

* Savings Rate
* Expense-to-Income Ratio
* EMI-to-Income Ratio
* Debt-to-Income Ratio
* Emergency Fund
* Credit Score
* Monthly Income
* Monthly Expenses
* Monthly Savings

---

### Step 4 — AI/ML Recommendation System

A Machine Learning classification model is used to predict financial health.

The system classifies users into:

* **Healthy**
* **Moderate**
* **Needs Attention**

### Model Performance

The implemented model achieved:

**Accuracy: 98.7%**

Classification performance:

| Financial Health | Precision | Recall | F1-Score |
| ---------------- | --------: | -----: | -------: |
| Healthy          |      0.99 |   0.99 |     0.99 |
| Moderate         |      0.97 |   0.97 |     0.97 |
| Needs Attention  |      0.99 |   0.99 |     0.99 |

Overall:

* Accuracy: **98.7%**
* Macro F1-score: **0.98**
* Weighted F1-score: **0.99**

---

## 🤖 AI Recommendation Engine

After predicting financial health, the system generates personalized recommendations.

The recommendation engine uses financial indicators to determine appropriate actions.

### Recommendation Categories

The system currently generates seven major recommendation categories:

1. Negative Savings
2. Maintain Financial Discipline
3. Investment Ready
4. Reduce Expenses
5. Reduce Debt
6. Increase Savings
7. Build Emergency Fund

### Recommendation Priorities

Each recommendation is assigned a priority:

* **High**
* **Medium**
* **Low**

### Recommendation Score

The system generates a financial recommendation score ranging from:

**0–100**

A higher score generally represents a stronger financial position or recommendation readiness.

---

## 📊 Recommendation Distribution

The final recommendation dataset contains **32,424 user records**.

| Recommendation Category       |  Users |
| ----------------------------- | -----: |
| Negative Savings              | 10,695 |
| Maintain Financial Discipline | 10,647 |
| Investment Ready              |  7,045 |
| Reduce Expenses               |  3,311 |
| Reduce Debt                   |    394 |
| Increase Savings              |    265 |
| Build Emergency Fund          |     67 |

### Recommendation Priority Distribution

| Priority |  Users |
| -------- | -----: |
| High     | 14,400 |
| Low      | 14,204 |
| Medium   |  3,820 |

---

## 📈 Step 5 — Interactive Dashboard

The Streamlit dashboard provides an interactive interface for exploring financial recommendations.

### Dashboard Features

#### KPI Cards

* Total Users
* Healthy Users
* Moderate Users
* Needs Attention Users
* Average Recommendation Score
* High-Priority Users

#### Visualizations

* Financial Health Distribution
* Recommendation Priority Distribution
* Recommendation Category Distribution
* Savings Rate Distribution
* Expense-to-Income Ratio Distribution
* Recommendation Score Distribution
* Financial Health vs Recommendation Category

#### Interactive Analysis

Users can filter the dashboard using:

* Financial Health
* Recommendation Category
* Recommendation Priority

The dashboard also provides:

* High-priority financial cases
* Personalized AI recommendations
* Filtered dataset preview
* Filtered CSV download

---

## 🧪 Step 6 — Testing & Validation

The complete system was tested successfully.

Testing covered:

* Dataset loading
* Data processing
* Financial calculations
* Machine Learning prediction
* Recommendation generation
* Recommendation categories
* Recommendation priorities
* Recommendation scores
* Dashboard loading
* Interactive filtering
* Data visualization
* CSV export

**Testing Status: ✅ Passed**

---

## 📁 Project Structure

```text
AI_Powered_Personal_Finance_Budget_Recommendation_System/
│
├── ai_financial_recommendation.py
├── financial_recommendation_dashboard.py
│
├── synthetic_personal_finance_dataset.csv
├── financial_recommendations_v2.csv
│
├── README.md
├── requirements.txt
│
└── screenshots/
    ├── dashboard_overview.png
    ├── financial_health.png
    ├── recommendation_analysis.png
    └── ai_recommendations.png
```

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Data Analysis

* Pandas
* NumPy

### Machine Learning

* Scikit-learn

### Visualization

* Plotly

### Dashboard

* Streamlit

### Data Storage

* CSV

---

## ⚙️ Installation

Clone or download the project repository.

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Step 1 — Generate Financial Recommendations

Run:

```bash
python ai_financial_recommendation.py
```

This generates:

```text
financial_recommendations_v2.csv
```

### Step 2 — Launch the Dashboard

Run:

```bash
streamlit run financial_recommendation_dashboard.py
```

The Streamlit dashboard will open in your browser.

---

## 📊 Dataset Information

The recommendation system processes:

* **32,424 records**
* **33 columns**

The final recommendation dataset contains user-level financial indicators, predicted financial health, recommendation category, priority, recommendation score, and AI-generated recommendation text.

---

## 💡 Business Insights

The system can help identify:

* Users with negative savings.
* Users with excessive expenses.
* Users requiring debt reduction.
* Users who should increase savings.
* Users who need stronger financial discipline.
* Users who are financially ready for investment-oriented recommendations.
* High-priority financial cases.

---

## 🎯 Business Value

This project demonstrates how Data Science and Machine Learning can support personal financial decision-making.

Potential applications include:

* Personal finance applications
* Banking platforms
* FinTech applications
* Financial wellness platforms
* Budget management systems
* Customer financial-risk analysis

---

## ⚠️ Disclaimer

This project is intended for **educational, analytical, and portfolio purposes**.

The generated recommendations should not be considered professional financial, investment, tax, or legal advice.

---

## 👨‍💻 Skills Demonstrated

This project demonstrates practical experience in:

* Python Programming
* Data Cleaning
* Exploratory Data Analysis
* Financial Data Analysis
* Feature Engineering
* Machine Learning
* Classification
* Model Evaluation
* Recommendation Systems
* Data Visualization
* Streamlit Dashboard Development
* Business Insights
* Data-Driven Decision Making

---

## 🏆 Project Status

**Project Status: ✅ Completed**

### Final Pipeline

```text
Data Collection
      ↓
Data Cleaning
      ↓
Financial Analysis
      ↓
Machine Learning
      ↓
AI Recommendations
      ↓
Interactive Dashboard
      ↓
Testing & Validation
      ↓
Portfolio Ready
```

---

## 📌 Author

**Yash Srivastava**

MCA — Data Science

**Project #6 — Financial Data Science Portfolio Project**
