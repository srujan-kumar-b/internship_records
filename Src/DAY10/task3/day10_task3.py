import pandas as pd

df = pd.read_csv("locations_data.csv")

print("Unique Locations BEFORE cleaning:\n")
print(df["Location"].unique())
print("\n-----------------------------\n")

df["Location"] = df["Location"].str.strip()
df["Location"] = df["Location"].str.title()

print("Unique Locations AFTER cleaning:\n")
print(df["Location"].unique())
print("\n-----------------------------\n")

print("Cleaned Data:\n")
print(df)
