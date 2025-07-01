from sklearn.metrics import confusion_matrix, f1_score, classification_report

# Sample predictions
y_true = [1, 0, 1, 1, 0, 0, 1]
y_pred = [1, 0, 0, 1, 0, 1, 1]

# Confusion Matrix
cm = confusion_matrix(y_true, y_pred)
print("Confusion Matrix:")
print(cm)

# F1-Score
f1 = f1_score(y_true, y_pred)
print("\nF1-Score:", round(f1, 2))

# Full Report
print("\nClassification Report:")
print(classification_report(y_true, y_pred))

