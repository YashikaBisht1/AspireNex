import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('creditcard.csv')

# Display the first few rows
print(df.head())

# Display basic information about the dataset
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Explore the target variable distribution
print(df['Class'].value_counts(normalize=True))

# Plot the target variable distribution
sns.countplot(x='Class', data=df)
plt.title('Class Distribution')
plt.show()
