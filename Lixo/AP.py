class AccessPoint:

    #Base comum para todos os APS

    
    def __init__(self, bssi, essid):

        self.bssi = str(bssi)
        self.essid = str(essid)
        self.valores = {}
        self.variancia = {}
        self.media = {}
        self.ptp = {}
        
    def addValues(self, position,values):
        import numpy as np
        if self.valores.get(position):
            self.valores[position].extend(values)
        else:
            self.valores[position] = values
            
        self.variancia[position] = np.var(values)
        self.media[position] = np.average(values)
        self.ptp[position] = np.ptp(values)
        return true

        
    def apCount(self):
        print "Total Employee %d" % Employee.apCount

    def name(self):
        print "BSSI : "+ str(self.bssi)+" ESSID: "+ str(self.essid)

    def printValues(self, position = False):
        if not position:
            for i in self.valores:
                print self.valores[i]
        else:
            print self.valores[position]
    
    def printVariance(self, position = False):
        if not position:
            for i in self.media:
                print self.media[i]
        else:
            print self.media[position]

    def printAverage(self, position = False):
        if not position:
            for i in self.variancia:
                print self.variancia[i]
        else:
            print self.variancia[position]
 
    def printPointToPoint(self, position = False):
        if not position:
            for i in self.ptp:
                print self.ptp[i]
        else:
            print self.ptp[position]
    
if __name__ == '__main__':
        
    cenas = AccessPoint("123123","44444")
    cenas.name()
    cenas.addValues((0,0),[-1,-2,-3,-4])
    cenas.addValues((0,1),[-9,-8,-7,-6])
    cenas.printValues()
    cenas.name()
    cenas.printValues((0,0))
    cenas.printAverage()
    cenas.printPointToPoint((0,0))
    cenas.printVariance((0,1))
    cenas.addValues((0,0),[-9,-8,-7,-6])
    cenas.printValues((0,0))
    print "cenas"