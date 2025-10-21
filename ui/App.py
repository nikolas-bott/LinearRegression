import tkinter as tk
from ui.Graph import Graph as GraphView


class App(tk.Tk):
    def __init__(self, points, n, m):
        super().__init__()
        
        self.title("Linear Regression ")
        self.geometry("500x500")
        
        graph = GraphView(self, points, n, m)
     
        graph.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)