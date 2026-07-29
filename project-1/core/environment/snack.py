class Snack:
    def __init__(self, x, y, typeOfSnack, exists = True):
        self.x = x
        self.y = y
        self.type = typeOfSnack 
        self.exists = exists

    def get_info(self):
        return self.x,self.y, self.type, self.exists
