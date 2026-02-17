
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt




df = pd.read_csv("/workspaces/Human-vs-ML-Project/Human_Algorithm/apple_quality.csv") 
dfG = df[df['Quality'] == "good"].head(500)
dfB = df[df['Quality'] == "bad"].head(500)
print(df.columns)

plt.scatter(dfG[''], dfG[''], color = 'green', label = "Good")
plt.scatter(dfB[''], dfB[''], color = 'blue', label = "Bad")
plt.xlabel("")
plt.ylabel("")
plt.title("Apple Quality: ")
plt.legend()

plt.savefig("Size_v_Weight.png", dpi=150)

# plt.scatter(dfG['Sweetness'], dfG['Acidity'], color = 'green', label = "Good")
# plt.scatter(dfB['Sweetness'], dfB['Acidity'], color = 'blue', label = "Bad")
# plt.xlabel("Sweetness")
# plt.ylabel("Acidity")  
# plt.title("Apple Quality: Sweetness vs Acidity")
# plt.legend()

# plt.savefig('Sweetness_v_Acidity.png', dpi=150)

# plt.scatter(dfG['Ripeness'], dfG['Acidity'], color = 'green', label = "Good")
# plt.scatter(dfB['Ripeness'], dfB['Acidity'], color = 'blue', label = "Bad")
# plt.xlabel("Ripeness")
# plt.ylabel("Acidity")  
# plt.title("Apple Quality: Ripeness vs Acidity")
# plt.legend()

# plt.savefig('Ripeness_v_Acidity.png', dpi=150)