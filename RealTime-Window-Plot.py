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
import API.winWlanApi as wlanAPI
import API.PhysicalAccessPoint as PhyAP
import AP_WalkMeasure_Relative_Plot as APRelPlotLib



def realTimePlot(fig, ax):
    
  
  PhysicalAPs = PhyAP.PhysicalAccessPoint()
  PhysicalAPs = wlanAPI.scan_AP_Fisicos()
  
  if not hasattr(fig,'realTimeData'):
    fig.realTimeData = {}
  
  i=-10
  APFisicoPerPiso = PhysicalAPs.getAPFisicoPerPiso('0')
  
  if APFisicoPerPiso!="cenas": 
    #for bssi in APFisicoPerPiso:
    for bssi in PhysicalAPs.physicalAPs:  
      i+=2
      tempRSSI = PhysicalAPs.getAverage(bssi,(0,0))
      if fig.realTimeData.has_key(bssi):
        fig.realTimeData[bssi]['line'][0].set_ydata(tempRSSI)
        fig.realTimeData[bssi]['annote'].xytext =(-11,tempRSSI+0.5)
        ax.lines.remove(fig.realTimeData[bssi]['line'][0])
        fig.realTimeData[bssi]['annote'].remove()
        fig.realTimeData.pop(bssi)
      else:
        fig.realTimeData[bssi] = {}
        fig.realTimeData[bssi]['line'] = ax.plot([-10, 10], [tempRSSI,tempRSSI],'b-')
        fig.realTimeData[bssi]['annote'] = ax.annotate(str(tempRSSI),fontsize='xx-small', xy=(-11, tempRSSI), xytext=(-11, tempRSSI+0.5) )
 
  else:
    print "Nao h? APs no piso."
  

  return fig

class App():
    def key(self, event):
            print "cenas"
            print("Clicked at: ", repr(event.char))
    

        
    def __init__(self):
        
        self.root = tk.Tk()
        self.root.wm_title("Embedding in TK")
        self.frame = tk.Frame(self.root, width=100, height=100)

        self.fig,self.ax,self.ax2 = APRelPlotLib.renderedRelativePlot()
        self.fig.delaxes(self.ax2)


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

        self.fig = realTimePlot(self.fig,self.ax)
        self.canvas.show()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.root.after(200, self.update_clock)

app=App()