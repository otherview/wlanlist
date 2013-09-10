import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random
import numpy as np
import sys
import Tkinter as tk
import time

def superPlot(fig, ax, spacing):
  ax.cla()
  ax.axis([-12, 12,-90, 0])
  ax.plot([0, 5], [-90,-90+spacing],'b-')
  return fig

class App():
    def key(self, event):
            print "cenas"
            print("Clicked at: ", repr(event.char))
    

        
    def __init__(self):
        
        self.root = tk.Tk()
        self.root.wm_title("Embedding in TK")
        self.frame = tk.Frame(self.root, width=100, height=100)

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.spacing = 0
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        
        self.fig = function1(self.fig, self.ax, self.spacing)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.toolbar = NavigationToolbar2TkAgg( self.canvas, self.root )
        self.toolbar.update()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.label = tk.Label(text="")
        self.frame.bind("<Key>", self.key)
        self.frame.bind("<1>", lambda event: self.frame.focus_set())
        
        self.frame.pack()
        self.label.pack()

        
        self.update_clock()
        self.root.mainloop()

    
    def update_clock(self):
        self.spacing +=1
        self.fig = superPlot(self.fig,self.ax,self.spacing)
        self.canvas.show()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.root.after(500, self.update_clock)

app=App()