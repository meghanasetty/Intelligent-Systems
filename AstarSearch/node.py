'''
This class is for storing the properties of the state.

g – g value
h – h value
f – f value
parent – the parent  of the node. Initial state will have parent as None
state - the state of the node

'''

class node:
    def __init__(self,state,parent = None):
        self.g = 0
        self.h = 0
        self.f = 0
        self.parent = parent
        self.state = state

    def __lt__(self,ob1):
        return ob1.f

    def setParent(self,p):
        self.parent = p

    def getParent(self):
        return self.parent
