import numpy as np
import matplotlib.pyplot as plt

data = np.random.exponential(scale=2, size=10000)

sample_means = []

for _ in range(1000):
    sample = np.random.choice(data, size=30)
    sample_means.append(np.mean(sample))

plt.hist(sample_means, bins=30)
plt.title("Distribution of Sample Means (CLT)")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.show()