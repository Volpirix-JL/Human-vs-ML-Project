import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from hode import human_checker as human_classify
from fetch_data import load_apple_data_from_csv
from sklearn.model_selection import train_test_split

df = pd.read_csv("/workspaces/Human-vs-ML-Project/Human_Algorithm/apple_quality.csv")