from LinearRegression import LinearRegression
from PointCollection import PointCollection

point_a = (22,11)
point_b = (12,32)
point_c = (1,42)
point_d = (32,23)
point_e = (54,23)



def main():
    points = PointCollection()
     
    points.addPoint(point_a)
    points.addPoint(point_b)
    points.addPoint(point_c)
    points.addPoint(point_d)
    points.addPoint(point_e)
    
    lr = LinearRegression(points)
    lr.calculate()
    lr.printFunction()
    
    return
    
if __name__ == "__main__":
    main()