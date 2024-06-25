import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

prof_data = pd.read_csv('Salary.csv')
print(prof_data.head())

# cleaning Data
prof_data.columns = prof_data.columns.str.strip()
print(prof_data.describe())

# Replacing empty sets
columns_to_fill = ["AGE","SALARY","LEAVES USED", "LEAVES REMAINING", "RATINGS", "PAST EXP"]
for column in columns_to_fill:
    mean_value = prof_data[column].mean()
    prof_data.fillna({column: mean_value}, inplace=True)

# Removing duplicates
duplicated_rows = prof_data[prof_data.duplicated()]
print("Duplicates: ")
print(duplicated_rows)
prof_data.drop_duplicates(inplace=True)

print(prof_data.describe())

prof_data['DOJ'] = prof_data['DOJ'].replace('##########', pd.NaT)
prof_data = prof_data.dropna(subset=['DOJ'])
print(prof_data.describe())
print(prof_data['DOJ'])
