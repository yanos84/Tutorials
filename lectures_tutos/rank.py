import numpy as np

def rank_selection(population, fitness, s=1.7, num_selected=2):
    """
    Perform rank-based selection.
    
    Args:
        population (list): list of individuals
        fitness (list): list of fitness values (higher is better)
        s (float): selection pressure parameter (1 <= s <= 2)
        num_selected (int): number of individuals to select
    
    Returns:
        selected (list): chosen individuals
    """
    N = len(population)
    
    # Sort individuals by fitness (ascending)
    sorted_indices = np.argsort(fitness)
    ranks = np.empty_like(sorted_indices)
    ranks[sorted_indices] = np.arange(1, N + 1)
    
    # compute selection probabilities using Baker’s formula
    probs = (2 - s) / N + (2 * (ranks - 1) * (s - 1)) / (N * (N - 1))
    probs /= probs.sum()  # Normalize (numerical safety)
    
    # Select individuals using roulette wheel based on rank probs
    selected_indices = np.random.choice(np.arange(N), size=num_selected, p=probs)
    
    return [population[i] for i in selected_indices], probs

if __name__ == "__main__":
        # Example population (just labels)
    population = ['A', 'B', 'C', 'D', 'E']

    # Fitness values (higher is better)
    fitness = [10, 13, 35, 60, 75]  # B is best, A is worst

    selected, probs = rank_selection(population, fitness, s=1.7, num_selected=1)

    print("Ranks & Probabilities:")
    for ind, fit, p in zip(population, fitness, probs):
        print(f"Individual {ind}: fitness={fit}, prob={p:.3f}")

    print("\nSelected individuals:", selected)


