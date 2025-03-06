class Grid:
    xDimension: int
    yDimension: int

    def __init__(self, x, y):
        self.xDimension = x
        self.yDimension = y
    
    def getXDimension(self):
        return self.xDimension

    def getYDimension(self):
        return self.yDimension
    
