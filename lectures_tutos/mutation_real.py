import matplotlib.pyplot as plt

x = 5.0
sigma = 0.5
mutations = x + np.random.normal(0, sigma, 10000)

plt.hist(mutations, bins=50, density=True)
plt.axvline(x, color='red', label='original x')
plt.title(f"Distribution of x' = x + N(0, {sigma})")
plt.legend()
plt.show()
