from multiprocessing import Process
from matplotlib.pyplot import plot, show
import matplotlib.pyplot as plt
import time,signal
import numpy as np
from pylab import *

def plot_graph(continuePlot):
    
    plt.ion()
    
    fig = plt.figure()
    
    
    ax = fig.add_subplot(111)
    ax.axis([-12, 12,-90, 0])
    
    i=0
    line2, = ax.plot([0, 5], [0,-90],'b-')
    

    
    while continuePlot: 
        
              i+=1
              
              #cenas = raw_input("Press Enter to continue...")
              
              line2.set_ydata(-90+i)
              
              fig.canvas.draw()
              
              time.sleep(1)
    
if __name__ == '__main__':
    #freeze_support()
    continuePlot = True
    p = Process(target=plot_graph, args=(continuePlot,))
    p.start()
    
    print 'yay'
    print 'computation continues...'
    print 'that rocks.'
    time.sleep(2)
    if raw_input("Enter to stop..") == 1:
        continuePlot = False
    
    print 'Now lets wait for the graph be closed to continue...:'
    p.join()
    print 'Closed'