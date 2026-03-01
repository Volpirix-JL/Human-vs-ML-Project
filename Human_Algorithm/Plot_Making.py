import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from fetch_data import load_apple_data_from_csv

def make_plot(factor1, factor2):
    factor1_label = factor1.replace('_', ' ')
    factor2_label = factor2.replace('_', ' ')
    
    df, target_name = load_apple_data_from_csv("/workspaces/Human-vs-ML-Project/Human_Algorithm/apple_quality.csv")

    os.makedirs("plots", exist_ok=True)

    plt.figure(figsize=(8, 6))
    sns.scatterplot(
        data=df,
        x=factor1,
        y=factor2,
        hue=target_name,
        style=target_name,
        s=30
    )

    plt.title(f'Apple Quality: {factor1_label} vs {factor2_label}')
    plt.xlabel(f'{factor1_label}')
    plt.ylabel(f'{factor2_label}')
    plt.legend(title='Apple Quality')
    plt.savefig(f'plots/{factor1_label}_v_{factor2_label}.png', dpi=100)
    plt.close()

make_plot('Sweetness', 'Ripeness')
make_plot('Sweetness', 'Acidity')
make_plot('Ripeness', 'Acidity')
