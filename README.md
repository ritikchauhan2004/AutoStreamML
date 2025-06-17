# 🚀 AutoStreamML

AutoStreamML is a **Streamlit-based automated machine learning (AutoML) web application** that allows users to perform quick Exploratory Data Analysis (EDA), train classification models, and download the best model — all from an intuitive UI with minimal coding.

![AutoStreamML Banner](https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png)

---

## 📌 Project Overview

This project is designed for data analysts, data scientists, and students who want to:
- Upload datasets
- Run **automated EDA** using `pandas_profiling`
- Select the target variable
- Compare and train ML models using `PyCaret`
- Download the trained model for future use

---

## 🌟 Features

- 📂 **Upload Data**: Upload your own `.csv` dataset.
- 📊 **Automated Profiling**: Perform exploratory data analysis using `pandas-profiling`.
- 🤖 **AutoML with PyCaret**: Select a target column, automatically train multiple classification models, and compare performance.
- 💾 **Download Model**: Save and export the best model.
- 🖼️ **Clean UI**: Built with Streamlit’s sidebar navigation.

---

## 🧰 Tech Stack

| Technology | Use |
|------------|-----|
| `Python` | Core programming language |
| `Streamlit` | Web app interface |
| `pandas` | Data manipulation |
| `pandas_profiling` | Automated EDA |
| `PyCaret` | Automated machine learning (classification) |

---

## 🔄 App Workflow

1. **Upload**: Load a dataset through the UI.
2. **Profiling**: Perform EDA via `pandas_profiling`.
3. **ML**:
   - Select the target variable.
   - Automatically compare classification models using PyCaret.
   - View the comparison report.
   - Save the best-performing model.
4. **Download**: (Coming soon) Option to download reports and models.

---

## 🖥️ How to Run This Project on Another Machine

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/yourusername/AutoStreamML.git
cd AutoStreamML
