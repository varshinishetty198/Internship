import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)


data = np.random.exponential(scale=50, size=10000)


sample_means = []
for _ in range(1000):
    sample = np.random.choice(data, size=30)
    sample_means.append(np.mean(sample))


sns.histplot(sample_means, bins=30, kde=True)
plt.title("Distribution of Sample Means (n=30)")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.show()