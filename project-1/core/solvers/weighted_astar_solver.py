import heapq
from ..environment.game import PacmanGame
from .heuristics import heuristic_func 
import time

def weighted_astar_solver(game: PacmanGame, weight: float = 1.0, timeout=10):
    start_time = time.time()
    priority_queue = [(0, 0, [], game)] 
    visited = {}
    visited[game.get_state()] = 0

    while priority_queue:
        if time.time() - start_time > timeout:
            print("Weighted A* solver reached the time limit!")
            return None

        f_cost, g_cost, path, current_game = heapq.heappop(priority_queue)

        if current_game.is_goal():
            return [start.get_info() for start, move in path] + [current_game.get_info()]
        if g_cost > visited[current_game.get_state()]:
            continue

        for next_game, move in current_game.get_next_states():
            new_g_cost = g_cost + 1 
            next_state_tuple = next_game.get_state()

            if next_state_tuple not in visited or new_g_cost < visited[next_state_tuple]:
                visited[next_state_tuple] = new_g_cost
                h_cost = heuristic_func(next_game)
                priority = new_g_cost + weight * h_cost
                
                new_path = path + [(current_game, move)]
                heapq.heappush(priority_queue, (priority, new_g_cost, new_path, next_game))
                
    return None