class PointCollection:
    def __init__(self):
        self.points = []
        
    def addPoint(self, point):
        self.points.append(point)
        
    def getPoints(self):
        print("Called",self.points)
        return self.points
    
    def sigma_x(self):
        sigma_x = 0
        
        for point in self.points:
            sigma_x += point[0]
            
        return sigma_x
    
    def sigma_y(self):
        sigma_y = 0
        
        for point in self.points:
            sigma_y += point[1]
            
        return sigma_y
    
    def sigma_xy(self):
        sigma_xy = 0
        
        for point in self.points:
            sigma_xy += point[0] * point[1]
            
        return sigma_xy
    
    def sigma_x_squared(self):
        sigma_x_squared = 0
        
        for point in self.points:
            sigma_x_squared += point[0] ** 2
            
        return sigma_x_squared
    
    def count(self):
        return len(self.points)