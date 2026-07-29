
from ..environment.game import PacmanGame
import math

def manhattan_distance(pos1, pos2):

    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def heuristic_func(game: PacmanGame):
    pacman_pos = game.player
    snacks = game.snacks
    target_type = game.determine_goal()
    if target_type is None:
        return 0

    target_snacks = [s for s in snacks if s.type == target_type and s.exists]

    if not target_snacks:
        return 0 
    min_dist = float('inf')
    for snack in target_snacks:
        dist = manhattan_distance(pacman_pos, (snack.x, snack.y))
        if dist < min_dist:
            min_dist = dist
            
    return min_dist