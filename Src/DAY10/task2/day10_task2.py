import pandas as pd
df = pd.read_csv("customer_orders_cls.csv")

print("Data types BEFORE conversion:\n")
print(df.dtypes)
print("\n-----------------------------\n")

df["Price"] = df["Price"].str.replace("$", "", regex=False)
df["Price"] = df["Price"].astype(float)
df["Date"] = pd.to_datetime(df["Date"])

print("Data types AFTER conversion:\n")
print(df.dtypes)
print("\n-----------------------------\n")

average_price = df["Price"].mean()
print("Average Price:", average_price)

latest_date = df["Date"].max()
print("Most Recent Order Date:", latest_date)
print("\n-----------------------------\n")

print("Final Cleaned Data:\n")
print(df)
