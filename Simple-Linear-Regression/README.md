# 📈 Simple Linear Regression using Advertising Dataset

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange.svg)
![Statsmodels](https://img.shields.io/badge/Statsmodels-OLS-green.svg)
![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-F37626.svg)
![License](https://img.shields.io/badge/License-Educational-success.svg)

A beginner-friendly Machine Learning project that demonstrates **Simple Linear Regression** using the popular **Advertising Dataset**.

This repository teaches how advertising budgets influence product sales through visualization, statistical analysis, and machine learning models.

---

# 📚 Project Overview

The dataset contains advertising budgets spent on different media:

| Feature      | Description                  |
| ------------ | ---------------------------- |
| 📺 TV        | TV advertising budget        |
| 📻 Radio     | Radio advertising budget     |
| 📰 Newspaper | Newspaper advertising budget |
| 💰 Sales     | Product sales                |

The notebook demonstrates how to predict **Sales** using **Simple Linear Regression**.

---

# ✨ Features

* 📊 Exploratory Data Analysis (EDA)
* 📈 Correlation Heatmap
* 🎯 Scatter Plots
* 📉 Pair Plots
* 🤖 Simple Linear Regression
* 📐 Model using **Statsmodels (OLS)**
* ⚡ Model using **Scikit-Learn**
* 🔀 Train-Test Split
* 📋 Residual Analysis
* 📏 Performance Metrics
* 🧠 Beginner-friendly explanations

---

# 📂 Repository Structure

```text
Simple-Linear-Regression/
│
├── advertising.csv
├── Simple+Linear+Regression+in+Python.ipynb
├── scripts/
│   └── compute_metrics.py
└── README.md
```

---

# 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Statsmodels
* Jupyter Notebook

---

# 🚀 Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/simple-linear-regression.git

cd simple-linear-regression
```

---

## 2️⃣ Create Virtual Environment (Optional)

### Windows

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Linux / macOS

```bash
python -m venv .venv
source .venv/bin/activate
```

---

## 3️⃣ Install Required Libraries

```bash
pip install pandas numpy scikit-learn statsmodels matplotlib seaborn jupyter
```

---

## 4️⃣ Launch Jupyter Notebook

```bash
jupyter notebook
```

Open:

* `Simple+Linear+Regression+in+Python.ipynb`

or

* `simple_linear_regression_self.ipynb`

---

## 5️⃣ Run the Evaluation Script

```bash
python scripts/compute_metrics.py
```

---

# 📊 Model Evaluation

Both **Statsmodels** and **Scikit-Learn** produce identical results.

| Metric                         |        Value |
| ------------------------------ | -----------: |
| Mean Squared Error (MSE)       | **5.348503** |
| Mean Absolute Error (MAE)      | **1.905152** |
| Root Mean Squared Error (RMSE) | **2.312683** |
| R² Score                       | **0.728135** |

---

# 📖 What You'll Learn

✔ Loading CSV datasets

✔ Data preprocessing

✔ Exploratory Data Analysis

✔ Correlation analysis

✔ Data visualization

✔ Simple Linear Regression

✔ Train/Test Split

✔ Model Training

✔ Prediction

✔ Performance Evaluation

✔ Residual Analysis

✔ Regression Equation

✔ Coefficient Interpretation

---

# 📸 Sample Visualizations

The notebooks include visualizations such as:

* 📈 Scatter Plot
* 🔥 Correlation Heatmap
* 📊 Pair Plot
* 📉 Regression Line
* 📌 Residual Plot

> **Tip:** Add screenshots inside a `screenshots/` folder and display them here.

Example:

```markdown
## Screenshots

![Scatter Plot](screenshots/scatter.png)

![Heatmap](screenshots/heatmap.png)

![Regression Line](screenshots/regression.png)
```

---

# 📂 Dataset

**advertising.csv**

Columns:

```text
TV
Radio
Newspaper
Sales
```

---

# 📚 Future Improvements

* Multiple Linear Regression
* Polynomial Regression
* Cross Validation
* Feature Engineering
* Model Comparison
* MAPE Calculation
* Interactive Visualizations
* Model Deployment with Flask or FastAPI

---

# 🎯 Who is this Project For?

* Beginners learning Machine Learning
* Students
* Data Science Enthusiasts
* Python Learners
* College Assignments
* Machine Learning Practice

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

If you find this project useful:

⭐ Star the repository

🍴 Fork the repository

🐞 Open an Issue

🚀 Submit a Pull Request

---

# 📜 License

This project is intended for **educational and learning purposes**.

---

# 👨‍💻 Author

**Niki**

If you like this project, consider giving it a ⭐ on GitHub to support future educational content.

---

## 🌟 Happy Learning!

*"The best way to learn Machine Learning is by building projects."*
