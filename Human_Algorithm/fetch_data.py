import os
import pandas as pd
df = pd.read_csv("/workspaces/Human-vs-ML-Project/Human_Algorithm/apple_quality.csv") 
print(df.columns)
file_path = "/workspaces/Human-vs-ML-Project/Human_Algorithm/apple_quality.csv"

def load_apple_data_from_csv(file_path):
    df = pd.read_csv(file_path)

    target_name = 'Quality' 

    return df, target_name

load_apple_data_from_csv(file_path)