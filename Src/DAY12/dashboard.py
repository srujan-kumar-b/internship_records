import matplotlib.pyplot as plt
categories = ['Electronics', 'Clothing', 'Home']
values = [300, 450, 200]
plt.subplot(1, 2, 1)
plt.bar(categories, values)
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales (in thousands)")

plt.subplot(1, 2, 2)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [100, 150, 200, 180, 250]
plt.plot(months, sales)
plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales (in thousands)")
plt.tight_layout()