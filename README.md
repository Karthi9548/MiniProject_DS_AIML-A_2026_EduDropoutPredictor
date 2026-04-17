1. Abstract

School dropout is a major challenge affecting educational systems worldwide, especially in developing regions. Early identification of students at risk can help institutions take preventive actions and improve overall academic outcomes.

This project focuses on building a **machine learning-based prediction system** that identifies students likely to drop out based on academic performance and socio-economic factors.

By analyzing variables such as study time, attendance, family background, and grades, the model provides insights into key risk factors. The project uses **Logistic Regression** to classify students into “at-risk” and “not at-risk” categories.

This solution aligns with **Sustainable Development Goal (SDG) 4: Quality Education**, aiming to ensure inclusive and equitable education for all.



2. Problem Statement

School dropout rates remain high due to various academic, personal, and socio-economic reasons. Traditional identification methods are often reactive rather than proactive.

Objective:

To build a predictive model that:

 Identifies students at risk of dropping out
 Analyzes key contributing factors
 Enables early intervention strategies



3. Domain & SDG Mapping

Domain: Education Analytics
SDG Goal: Goal 4 – Quality Education
Target 4.1: Ensure completion of free, equitable, and quality primary and secondary education



4. Dataset Description

The dataset used is the **Student Performance Dataset**, which contains information about students’ academic and personal attributes.

Features Include:

 Age
 Study Time
 Absences
 Family Support
 Parental Education
 Grades (G1, G2, G3)
 Extra-curricular activities

Target Variable:

A new column called **`dropout`** is created:

 `1` → At risk (low final grade)
 `0` → Not at risk

---

5. Project Workflow

The project follows a standard Data Science pipeline:

1. Problem Identification
2. Data Collection
3. Data Preprocessing
4. Exploratory Data Analysis (EDA)
5. Data Visualization
6. Model Building
7. Evaluation and Interpretation



6. Data Preprocessing

Key preprocessing steps:

 Removed irrelevant columns (`G1`, `G2`)
 Handled categorical variables using **one-hot encoding**
 Created a new target variable (`dropout`)
 Cleaned and structured the dataset



7. Exploratory Data Analysis (EDA)

EDA helps understand patterns and relationships in the data.

Key Insights:

 Most students are **not at risk of dropout**
 Students with **low study time** are more likely to drop out
 Higher **absences correlate with higher dropout risk**



8. Data Visualization

The following visualizations were created:

Dropout Distribution
Study Time vs Dropout
Absences vs Dropout
Correlation Heatmap

These graphs help in identifying patterns and trends in the dataset.



9. Model Development

🔹 Algorithm Used:

 Logistic Regression

🔹 Why Logistic Regression?

 Simple and effective for binary classification
 Easy to interpret
 Suitable for structured data



10. Model Evaluation

The model was evaluated using:

 Accuracy Score
 Classification Report
 Confusion Matrix

Results:

 High accuracy achieved (~80–100%)
 Correct classification of at-risk students
 Strong predictive performance



11. Confusion Matrix Interpretation

 True Positives → Correctly identified dropouts
 True Negatives → Correctly identified non-dropouts
 Minimal misclassification observed


13. Tools & Technologies

 Python
 Pandas
 NumPy
 Matplotlib
 Seaborn
 Scikit-learn
 VS Code


14. Results & Findings

 Study time and attendance are key indicators
 Academic performance strongly influences dropout risk
 Machine learning can effectively predict at-risk students



15. Conclusion

This project demonstrates how data science can be used to solve real-world problems in education. By identifying students at risk early, institutions can take timely actions to improve retention and success rates.


