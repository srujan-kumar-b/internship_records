import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("housing_data.csv")

df = df.dropna()

corr_matrix = df.corr(numeric_only=True)

print("\nCorrelation Matrix:\n")
print(corr_matrix)

plt.subplot(1, 2, 1)
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix Heatmap")
plt.tight_layout()

print("\nHighly Correlated Pairs (>|0.8|):\n")

for i in range(len(corr_matrix.columns)):
    for j in range(i):
        if abs(corr_matrix.iloc[i, j]) > 0.8:
            print(f"{corr_matrix.columns[i]} and {corr_matrix.columns[j]} --> Correlation: {corr_matrix.iloc[i, j]:.2f}")

plt.subplot(1, 2, 2)
sns.boxplot(y=df["Price"])
plt.title("Boxplot of House Prices")
plt.ylabel("Price")
plt.tight_layout()
plt.show()

