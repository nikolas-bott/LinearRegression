from LinearRegression import LinearRegression
from PointCollection import PointCollection
from ui.App import App


class Main:
    def __init__(self):
        self.points = PointCollection()
        self.point_a = (22,11)
        self.point_b = (12,32)
        self.point_c = (1,42)
        self.point_d = (32,23)
        self.point_e = (54,23)


    def main(self):
        
        self.points.addPoint(self.point_a)
        self.points.addPoint(self.point_b)
        self.points.addPoint(self.point_c)
        self.points.addPoint(self.point_d)
        self.points.addPoint(self.point_e)
        
        lr = LinearRegression(self.points)
        lr.calculate()
        lr.printFunction()
        n = lr.n
        m = lr.m
        
        app = App(self.points.getPoints(), n, m)
        app.mainloop()
        
        return

    def get_point_collection(self):
        return self.points

if __name__ == "__main__":
    main_program = Main()
    main_program.main()