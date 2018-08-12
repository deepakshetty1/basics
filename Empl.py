class Empl:
    emplAttr = 100
    
    def __init__(self):
        print "Calling Parent constructor"
        
    def callingParent(self):
        print "Calling parent method"
        
    def setAttr(self, attr):
        Empl.emplAttr = attr
        
    def getAttr(self):
        print "getting parent attribure", Empl.emplAttr
        
class Child(Empl):
    def __init__(self):
        print "Calling child contructor"
        
    def CallingChild(self):
        print "Calling child attribute"
c = Child()
c.CallingChild()
c.callingParent()
c.setAttr(200)
c.getAttr()