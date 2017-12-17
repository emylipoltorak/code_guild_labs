class Token:
    def __init__(self, x, y, color=None):
        self.x = x
        self.y = y
        self.color = color
        self.location = (x, y)


    def __str__(self):
        if not self.color:
            return 'O'
        else:
            return self.color
