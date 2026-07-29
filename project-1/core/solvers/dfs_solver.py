from ..environment.game import PacmanGame
import time

def dfs_solver(game: PacmanGame, timeout=10):
    start_time = time.time()
    stack = [([], game)]
    visited = set()

    while stack:
        if time.time() - start_time > timeout:
            print("DFS solver reached the time limit!")
            return None

        path, current_game = stack.pop()
        current_state_tuple = current_game.get_state()

        if current_state_tuple in visited:
            continue
        
        visited.add(current_state_tuple)

        if current_game.is_goal():
            return [start.get_info() for start, move in path] + [current_game.get_info()]
        for next_game, move in reversed(current_game.get_next_states()): 
            if next_game.get_state() not in visited:
                new_path = path + [(current_game, move)]
                stack.append((new_path, next_game))
                
    return None