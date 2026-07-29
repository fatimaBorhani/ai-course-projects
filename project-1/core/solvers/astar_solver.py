from .weighted_astar_solver import weighted_astar_solver

def astar_solver(game, timeout=10):
    return weighted_astar_solver(game, weight=1.0, timeout=timeout)