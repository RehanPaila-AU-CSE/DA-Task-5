import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# For clean plots
sns.set(style='whitegrid')

# Load dataset
df = pd.read_csv('titanic.csv')
print(df.head())
