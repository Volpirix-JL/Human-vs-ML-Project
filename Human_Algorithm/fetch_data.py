
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt




df = pd.read_csv("/workspaces/Human-vs-ML-Project/Human_Algorithm/apple_quality.csv") 
dfG = df[df['Quality'] == "good"].head(500)
dfB = df[df['Quality'] == "bad"].head(500)
# print(df.columns)

plt.scatter(dfG['Size'], dfG['Weight'], color = 'green', label = "Good")
plt.scatter(dfB['Size'], dfB['Weight'], color='blue', label = "Bad")
plt.xlabel("Size")
plt.ylabel("Weight")
plt.title("Apple Quality: Size vs Weight")
plt.legend()

plt.savefig("Size_v_Weight.png", dpi=150)

