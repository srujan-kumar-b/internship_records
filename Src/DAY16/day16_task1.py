import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

heights = np.random.normal(loc=170, scale=10, size=1000)

incomes = np.random.exponential(scale=50000, size=1000)

scores = 100 - np.random.exponential(scale=15, size=1000)

df = pd.DataFrame({
    "Heights (Normal)": heights,
    "Incomes (Right-Skewed)": incomes,
    "Scores (Left-Skewed)": scores
})

def plot_distribution(data, title, subplot_position):
    plt.subplot(1, 3, subplot_position)
    
    sns.histplot(data, kde=True)
    
    mean = data.mean()
    median = data.median()
    skewness = data.skew()
    
    plt.axvline(mean, linestyle='--', label=f"Mean = {mean:.2f}")
    plt.axvline(median, linestyle='-', label=f"Median = {median:.2f}")
    
    plt.title(title)
    plt.legend()
    
    print(f"\n{title}")
    print(f"Mean   : {mean:.2f}")
    print(f"Median : {median:.2f}")
    print(f"Skewness : {skewness:.2f}")
    
    if mean > median:
        print("→ Distribution is Right-Skewed (Positive Skew)")
    elif mean < median:
        print("→ Distribution is Left-Skewed (Negative Skew)")
    else:
        print("→ Distribution is Normal (Symmetric)")

plt.figure(figsize=(18,5))

plot_distribution(df["Heights (Normal)"], "Human Heights (Normal Distribution)", 1)
plot_distribution(df["Incomes (Right-Skewed)"], "Household Income (Right-Skewed)", 2)
plot_distribution(df["Scores (Left-Skewed)"], "Easy Exam Scores (Left-Skewed)", 3)

plt.tight_layout()
plt.show()

