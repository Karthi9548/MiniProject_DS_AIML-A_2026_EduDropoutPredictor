import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import os

# Ensure output folders exist
os.makedirs("outputs/results", exist_ok=True)
os.makedirs("outputs/graphs", exist_ok=True)

# Load cleaned data
df = pd.read_csv("dataset/processed_data/cleaned.csv")

# Split features and target
X = df.drop("dropout", axis=1)
y = df["dropout"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Results
acc = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print("Accuracy:", acc)
print(report)

# Save results to file
with open("outputs/results/model_results.txt", "w") as f:
    f.write("Accuracy: " + str(acc) + "\n\n")
    f.write(report)

# Save predictions to CSV
pred_df = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": y_pred
})
pred_df.to_csv("outputs/results/predictions.csv", index=False)

print("Predictions saved to outputs/results/predictions.csv")

# Confusion Matrix (save as image)
ConfusionMatrixDisplay.from_estimator(model, X_test, y_test)
plt.title("Confusion Matrix")
plt.savefig("outputs/graphs/confusion_matrix.png")
plt.show()