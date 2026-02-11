import pandas as pd

products = pd.Series(
    [7000, 1500, 700],
    index=['TV', 'FireStick', 'Keyboard']
)
print("Full Product Price List:")
print(products)

TV_price = products['TV']
print("\nPrice of TV:")
print(TV_price)

first_two = products.iloc[0:2]
print("\nFirst Two Products:")
print(first_two)
