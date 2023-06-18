

class Noe:
    
    def __init__(self) -> None:
        self.pos = [0, 0]
    
    def move_pos(self, x, y):
        self.pos = [x, y]
    
    def move_up(self):
        self.pos[1] += 1
        return self.pos
        
    def move_down(self):
        self.pos[1] -= 1
        return self.pos
        
    def move_right(self):
        self.pos[0] += 1
        return self.pos
        
    def move_left(self):
        self.pos[0] -= 1
        return self.pos