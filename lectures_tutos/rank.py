# Step 1: assign ranks
ranks = np.argsort(np.argsort(fitness)) + 1  # lowest = 1, highest = N

# Step 2: convert ranks to probabilities (linear ranking)
N = len(fitness)
s = 1.7
probs = (2 - s)/N + (2 * ranks * (s - 1)) / (N * (N - 1))
probs /= np.sum(probs)

# Step 3: apply roulette wheel using these probs
selected_indices = np.random.choice(len(fitness), size=2, p=probs)
