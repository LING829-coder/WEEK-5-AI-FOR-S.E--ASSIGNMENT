import pandas as pd
from sklearn.metrics import accuracy_score

# Sample DataFrame
data = pd.DataFrame({
    'actual': [1, 0, 1, 1, 0, 0, 1, 0],
    'predicted': [1, 0, 1, 0, 0, 1, 1, 0],
    'group': ['urban', 'urban', 'rural', 'rural', 'urban', 'rural', 'rural', 'urban']
})

# Group-wise accuracy
group_accuracy = data.groupby('group').apply(lambda g: accuracy_score(g['actual'], g['predicted']))
print("Accuracy by Group:")
print(group_accuracy)

