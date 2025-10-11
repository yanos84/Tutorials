import numpy as np

def roulette_wheel_selection(population, fitness, n_select=1):
    """
    Roulette Wheel Selection (Fitness Proportionate Selection)

    Args:
        population : list or array of individuals
        fitness    : list or array of fitness values (non-negative)
        n_select   : number of individuals to select
    
    Returns:
        list of selected individuals
    """
    # Convert to numpy arrays for vector ops
    fitness = np.array(fitness, dtype=float)
    population = np.array(population)
    
    # Normalize fitness to get probabilities
    total_fitness = np.sum(fitness)
    if total_fitness == 0:
        # Avoid division by zero — fallback to uniform selection
        probabilities = np.ones_like(fitness) / len(fitness)
    else:
        probabilities = fitness / total_fitness

    # Compute cumulative probabilities
    cumulative = np.cumsum(probabilities)

    # Select individuals
    selected = []
    for _ in range(n_select):
        r = np.random.rand()  # random number in [0,1)
        idx = np.searchsorted(cumulative, r)  # find index
        selected.append(population[idx])

    return selected
