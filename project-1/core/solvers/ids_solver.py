from ..environment.game import PacmanGame
import time

def dls_solver(game: PacmanGame, limit: int, start_time, timeout, visited):
    stack = [([], game, 0)] 

    while stack:
        if time.time() - start_time > timeout:
            return "timeout", None

        path, current_game, depth = stack.pop()
        state = current_game.get_state()
        if state in visited and visited[state] <= depth:
            continue
        visited[state] = depth

        if current_game.is_goal():
            full_path_info = [start.get_info() for start, move in path] + [current_game.get_info()]
            return "found", full_path_info

        if depth < limit:
            for next_game, move in reversed(current_game.get_next_states()):
                new_path = path + [(current_game, move)]
                stack.append((new_path, next_game, depth + 1))
    
    return "not_found", None

def ids_solver(game: PacmanGame, max_limit: int = 100, timeout=10):
    start_time = time.time()
    for depth_limit in range(max_limit):
        if time.time() - start_time > timeout:
            print("IDS solver reached the time limit!")
          
            return [game.get_info()]

        visited = {} 
        result_status, path = dls_solver(game, depth_limit, start_time, timeout, visited)
        
        if result_status == "found":
            return path
        
        if result_status == "timeout":
            print("IDS solver reached the time limit!")
            return [game.get_info()]

    return None