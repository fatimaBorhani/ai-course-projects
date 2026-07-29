from copy import deepcopy
from .ghost import Ghost
from .snack import Snack

class PacmanGame:
    def __init__(self, player : tuple[int, int], ghosts : list[Ghost], snacks : list[Snack], is_wall, move_direction = None):
        self.player = player 
        self.ghosts = deepcopy(ghosts)
        self.snacks = deepcopy(snacks)
        self.is_wall = is_wall
        self.height = len(is_wall)
        self.width = len(is_wall[0])
        self.move_direction = move_direction

    def get_info(self):
        return (self.move_direction, [self.player] + [ghost.get_info() for ghost in self.ghosts] + [snack.get_info() for snack in self.snacks])

    def determine_goal(self):
        has_A = any(s.type == 'A' and s.exists for s in self.snacks)
        if has_A: return 'A'
        has_B = any(s.type == 'B' and s.exists for s in self.snacks)
        if has_B: return 'B'
        return None

    def in_bounds(self, y, x):
        return 0 <= y < self.height and 0 <= x < self.width

    def is_valid(self, y, x):
        return self.in_bounds(y, x) and not self.is_wall[y][x]

    def is_goal(self):
        return all(not s.exists for s in self.snacks)

    def _get_ghost_positions_at_time(self, time):
        positions = set()
        for ghost in self.ghosts:
            radius = ghost.radius
            period = 4 * radius
            if period == 0:
                positions.add(ghost.center)
                continue
            
            time_in_period = time % period
            
            if time_in_period <= radius: displacement = time_in_period
            elif time_in_period <= 2 * radius: displacement = radius - (time_in_period - radius)
            elif time_in_period <= 3 * radius: displacement = -(time_in_period - (2 * radius))
            else: displacement = -(radius - (time_in_period - 3 * radius))

            gy, gx = ghost.center
            if ghost.is_horizontal():
                positions.add((gy, gx + displacement))
            else: 
                positions.add((gy + displacement, gx))
        return positions
    def get_next_states(self):
     next_states = []
     moves = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

     for move, (dx, dy) in moves.items():
        next_game_state = deepcopy(self)
        next_game_state.move_direction = move
        
        player_prev_pos = self.player
        px, py = player_prev_pos
        new_px, new_py = px + dx, py + dy

        if not self.is_valid(new_px, new_py):
            continue
        
        next_game_state.player = (new_px, new_py)
        
        ghost_prev_positions = {i: (g.x, g.y) for i, g in enumerate(self.ghosts)}
        
        for ghost in next_game_state.ghosts:
            ghost.update_position()

        collision = False
        for i, ghost in enumerate(next_game_state.ghosts):
            ghost_current_pos = (ghost.x, ghost.y)
            ghost_prev_pos = ghost_prev_positions[i]
            
            if next_game_state.player == ghost_current_pos:
                collision = True
                break
            
            if next_game_state.player == ghost_prev_pos and player_prev_pos == ghost_current_pos:
                collision = True
                break
        
        if collision:
            continue

        can_eat_b = all(not s.exists for s in self.snacks if s.type == 'A')
        for snack in next_game_state.snacks:
            if snack.exists and (snack.x, snack.y) == next_game_state.player:
                if snack.type == 'A':
                    snack.exists = False
                    break
                elif snack.type == 'B' and can_eat_b:
                    snack.exists = False
                    break
        
        next_states.append((next_game_state, move))
        
     return next_states

    def get_state(self):
        existing_snacks = frozenset((s.x, s.y, s.type) for s in self.snacks if s.exists)
        ghost_states = tuple((g.x, g.y, g.direction) for g in self.ghosts)
        
        return (self.player, existing_snacks, ghost_states)