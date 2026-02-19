import pandas as pd

df = pd.DataFrame({
    "Values": [10, 12, 11, 13, 12, 14, 15, 100]
})

mu = df["Values"].mean()
sigma = df["Values"].std()

df["z_score"] = (df["Values"] - mu) / sigma

outliers = df[abs(df["z_score"]) > 3]

print("Data with Z-scores:\n", df)
print("\nOutliers:\n", outliers)