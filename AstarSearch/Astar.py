import heapq

'''
This is a base class for A* algorithm where the problem inherits this class to solve using A* algorithm
 
fringe – contains a priority queue for the all unexpanded(open) nodes.
expanded – contains a list of all the expanded(closed) nodes.
inputState – the initial state which the user provided. It is a 3*3 list.

'''
class Astar:
    def __init__(self,inputState):
        self.expanded = []
        self.fringe = []
        self.inputState = inputState

    def isGoalState(self,state):
        pass

    def calculateF(self,n):
        return n.g+n.h

    def calculateG(self,parent):
        pass

    def printPath(self,n):
        pass

    def generateChilds(self,n):
        pass

    def printNode(self, n):
        pass

    def checkifSameStateExistswithLowerFvalue(self,lists,n):
        pass

    def isTwoStatesEqual(self, state1, state2):
        pass

    def AstarSearch(self):
        if(self.isGoalState(self.inputState)):
            print('input state is the goal State')
            return None
        while len(self.fringe) != 0:
            #pop the node from the fringe
            f, n = heapq.heappop(self.fringe)
            childs = self.generateChilds(n)
            for child in childs:
                if(self.isGoalState(child.state)):
                    #got the goal
                    print('Reached the goal ',child.state)
                    return child
                if self.checkifSameStateExistswithLowerFvalue(self.fringe,child) ==False:
                    heapq.heappush(self.fringe,(child.f,child))
                elif self.checkifSameStateExistswithLowerFvalue(self.expanded,child) == False:
                    heapq.heappush(self.fringe,(child.f,child))
            #add to the expanded list
            heapq.heappush(self.expanded,(n.f,n))
        return None


