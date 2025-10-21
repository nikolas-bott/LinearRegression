import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class Graph(tk.Frame):
    def __init__(self, master, points, n, m):
        super().__init__(master)
        self.n = n
        self.m = m
        #Draw Points And Graph
        self.points = points  # save the PointCollection instance
        
        self.fig = Figure(figsize=(5,5), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
    
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True) 
        
        self.draw_points()
        self.draw_function()
        
        #display function in graph f(x) = mn+n => f(x) = 13x+12
        
        self.pack()
        
        
        
    def draw_points(self):
        
        print("Points:", self.points)

        for point in self.points:
            self.ax.plot(point[0], point[1], color="blue", marker='o')
        
        self.canvas.draw()
        
    def draw_function(self):
        x_vals = [p[0] for p in self.points]
        x_min = min(x_vals) - 1
        x_max = max(x_vals) + 1
        x = np.linspace(x_min, x_max, 200)
        
        y = self.m * x +self.n
        
        self.ax.plot(x, y, color="#7F00FF", label=f"y = {self.m}x + {self.n}")
        self.ax.legend()
        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")
        self.ax.grid(True)

        # Refresh the canvas
        self.canvas.draw()
        
        
    