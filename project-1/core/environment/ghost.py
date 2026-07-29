class Ghost:
    def __init__(self, x, y, axis, radius=5):
        self.center = (x, y)
        self.x = x
        self.y = y
        self.axis = axis
        self.radius = radius
        self.direction = 1
    def get_info(self):
        return self.x,self.y
    
    def is_horizontal(self):
        return self.axis == 'H'
    
    def get_position(self):
        return self.x, self.y

    def set_state(self, x, y, direction):
        self.x, self.y, self.direction = x, y, direction

    def get_next_position(self):
        dx, dy = (0, self.direction) if self.is_horizontal() else (
            self.direction, 0)
        return (self.x + dx, self.y + dy)
    def update_position(self):
        if self.axis == 'H': 
            current_offset = self.y - self.center[1]
            if abs(current_offset) >= self.radius:
                self.direction *= -1 
            self.y += self.direction
        else: 
            current_offset = self.x - self.center[0]
            if abs(current_offset) >= self.radius:
                self.direction *= -1
            self.x += self.direction