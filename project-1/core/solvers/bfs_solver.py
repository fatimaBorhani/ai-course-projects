from collections import deque
from ..environment.game import PacmanGame
import time

def bfs_solver(game: PacmanGame, timeout=10):
    start_time = time.time()

    queue = deque([([], game)])
    visited = set()
    visited.add(game.get_state())

    while queue:
        if time.time() - start_time > timeout:
            print("BFS solver reached the time limit!")
            return None

        path, current_game = queue.popleft()
        if current_game.is_goal():
            return [start.get_info() for start, move in path] + [current_game.get_info()]
        for next_game, move in current_game.get_next_states():
            next_state_tuple = next_game.get_state()
            if next_state_tuple not in visited:
                visited.add(next_state_tuple)
                
                new_path = path + [(current_game, move)]
                queue.append((new_path, next_game))
                
    return None 