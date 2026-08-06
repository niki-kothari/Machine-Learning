<div align="center">

# Customer Churn Prediction

### Predict telecom customer churn with a beginner-friendly Artificial Neural Network

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-Keras-FF6F00?logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![Notebook](https://img.shields.io/badge/Notebook-Jupyter-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)

**Learn the complete machine-learning workflow—from customer data to useful churn insights.**

</div>

---

## ✨ Overview

Customer churn happens when a customer stops using a company's service. In telecom, predicting churn early gives the business a chance to offer help, discounts, or a better plan before the customer leaves.

This project uses a TensorFlow/Keras **Artificial Neural Network (ANN)** to predict whether a customer is likely to churn. It is designed as a clear, hands-on introduction to classification with deep learning.

> **Goal:** predict whether a customer will **stay** or **churn** using their account, service, contract, and billing information.

| Prediction | Meaning |
| :---: | --- |
| `0` | The customer is expected to stay |
| `1` | The customer is expected to churn |

## 🗂️ Project structure

```text
11_chrun_prediction/
│
├── churn.ipynb          # Step-by-step analysis and ANN model
├── customer_churn.csv   # Telecom customer dataset
└── README.md            # Project documentation
```

## 🚀 Quick start

### 1. Install the required packages

```bash
pip install pandas numpy matplotlib seaborn scikit-learn tensorflow jupyter
```

### 2. Start Jupyter Notebook

```bash
jupyter notebook
```

### 3. Open and run

Open `churn.ipynb`, then choose **Run All**. The notebook is ordered so every cell can be run from top to bottom.

> If TensorFlow is not installed, run `pip install tensorflow` in your terminal and restart the notebook kernel.

## 📊 Dataset at a glance

The dataset contains **7,043 telecom customer records**. Each row describes one customer and their eventual churn status.

| Feature group | Examples | Why it may matter |
| --- | --- | --- |
| Customer profile | `gender`, `SeniorCitizen`, `Partner`, `Dependents` | Different customer groups may have different needs. |
| Account history | `tenure`, `Contract`, `PaperlessBilling` | A short-term contract or new account can signal risk. |
| Services | `InternetService`, `OnlineSecurity`, `StreamingTV` | Service choices may be related to customer satisfaction. |
| Billing | `MonthlyCharges`, `TotalCharges`, `PaymentMethod` | Price and payment preferences can influence retention. |
| Target | `Churn` | `Yes` when the customer left; `No` when they stayed. |

## 🔄 What happens in the notebook?

| Step | Activity | What you learn |
| :---: | --- | --- |
| 01 | Load and inspect data | Understand rows, columns, and class balance. |
| 02 | Clean data | Remove identifiers and fix missing numeric values. |
| 03 | Visualize patterns | Compare churn with tenure and monthly charges. |
| 04 | Prepare features | Convert categories to numbers and scale numeric values. |
| 05 | Split data | Keep unseen test data for a fair final evaluation. |
| 06 | Train ANN | Let the network learn churn patterns from training examples. |
| 07 | Evaluate | Measure accuracy, precision, recall, F1-score, and errors. |

## 🧠 Model architecture

```text
Customer information
        │
        ▼
Preprocessing
• Numeric values → scaled to 0–1
• Text categories → one-hot encoded
        │
        ▼
Dense layer  ── 16 neurons, ReLU
        │
        ▼
Dense layer  ── 8 neurons, ReLU
        │
        ▼
Output layer ── 1 neuron, Sigmoid
        │
        ▼
Churn probability (0 to 1)
```

The final **sigmoid** layer returns a probability. For example, `0.78` means the model estimates a 78% chance that the customer will churn. The notebook labels probabilities of **0.50 or above** as churn.

## 📈 How success is measured

Because more customers stay than churn, accuracy alone does not give the full picture. The notebook reports several metrics:

| Metric | Plain-language question it answers |
| --- | --- |
| **Accuracy** | How often was the model correct overall? |
| **Precision** | When the model predicts churn, how often is it right? |
| **Recall** | Of customers who actually churned, how many did the model find? |
| **F1-score** | How well does the model balance precision and recall? |
| **Confusion matrix** | Which types of correct and incorrect predictions occurred? |

> For customer-retention work, churn **recall** is often especially useful: it shows how many at-risk customers the business manages to identify.

## 🛠️ Technologies used

| Tool | Purpose |
| --- | --- |
| Python | Main programming language |
| pandas & NumPy | Data loading and preparation |
| Matplotlib & Seaborn | Visualizations |
| scikit-learn | Splitting, scaling, encoding, and metrics |
| TensorFlow / Keras | Building and training the neural network |
| Jupyter Notebook | Interactive learning environment |

## ✅ Good practices included

- The customer ID is removed because it is an identifier, not a meaningful predictive signal.
- `TotalCharges` is safely converted from text to a numeric value.
- The train/test split is stratified, keeping the churn ratio similar in both sets.
- Scaling and encoding are fitted on training data only, preventing test-data leakage.
- Early stopping helps reduce overfitting during neural-network training.
- The final evaluation uses data the model did not see while training.

## 🔍 Ideas to explore next

1. Try a lower prediction threshold such as `0.40` and compare churn recall and precision.
2. Compare the ANN against logistic regression, random forest, or gradient boosting.
3. Add dropout layers and test different neuron counts.
4. Investigate which customer groups experience the highest churn rate.
5. Save the trained model and preprocessing pipeline for use with new customer data.

## ⚠️ Notes

- Neural-network results can vary slightly between runs due to random initialization.
- This is an educational project, not a production deployment.
- A production churn system should include additional validation, fairness checks, monitoring, retraining, and a defined business decision process.

---

<div align="center">

Built for learning the fundamentals of **classification**, **data preprocessing**, and **neural networks**. 🚀

</div>
