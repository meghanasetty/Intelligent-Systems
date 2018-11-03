from Astar import Astar
from node import node
import heapq
import copy

'''
    The eightPuzzle class is derived from the Astar class.
    
    goalState – The goal State given by the user
    dim – The row/column of 8 puzzle board
    isManhattanDistance – true, if the heuristic to be considered is ManhattanDistance. Else, misplaced heuristic is taken into consideration.
    noofNodesGenerated – The number of nodes that are generated
'''
class eightPuzzle(Astar):
    def __init__(self,inputState,goalState,isManhattanDistance):
        Astar.__init__(self,inputState)
        self.goalState = goalState
        self.dim = 3
        self.isManhattanDistance = isManhattanDistance
        self.noofNodesGenerated = 0
        n = self.createNode()
        heapq.heappush(self.fringe,(n.f, n))

    def createNode(self,state=None,parent=None):
        self.noofNodesGenerated += 1
        if state is None:
            state = self.inputState
            n = node(state)
            n.g = 0
            n.h = self.calculateH(state)
            n.f = self.calculateF(n)
            return n
        else:
            n = node(state, parent)
            n.g = self.calculateG(parent)
            n.h = self.calculateH(state)
            n.f = self.calculateF(n)
            return n

    def calculateG(self, parent):
        return parent.g+1

    def isGoalState(self,state):
        for i in range(self.dim):
            for j in range(self.dim):
                if state[i][j] != self.goalState[i][j]:
                    return False
        return True

    def isTwoStatesEqual(self,state1,state2):
        for i in range(self.dim):
            for j in range(self.dim):
                if state1[i][j] != state2[i][j]:
                    return False
        return True
    def findIndex(self,state,number):
        for i, row in enumerate(state):
            try:
                j = row.index(number)
            except ValueError:
                continue
            return i, j

    def calculateH(self,state):
        if(self.isManhattanDistance):
            return self.calculateHvalueManhattan(state)
        else:
            return self.calculateHvalueMisplacedTiles(state)
    def calculateHvalueMisplacedTiles(self,state):
        hvalue = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if ((state[i][j] !=0) and  (state[i][j] != self.goalState[i][j])):
                    hvalue +=1
        return hvalue


    def calculateHvalueManhattan(self,state):
        hvalue = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if (state[i][j] != 0):
                    (goalRow,goalColumn) = self.findIndex(self.goalState,state[i][j])
                    hvalue += abs(goalColumn - j) + abs(goalRow - i)
        return hvalue

    def printstate(self,state):
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == 0:
                    print(' ',end=' ')
                else:
                    print(state[i][j], end=' ')
            print()
        print()

    def printNode(self,n):
        print('The values are g=',n.g,' f=',n.f,' h=',n.h,' state = ',n.state)

    def printPath(self,n):
        path = []
        while(True):
            if(n is None):
                break
            else:
                path.append(n.state)
                n = n.parent
        print('The Path length = ',len(path))
        print('Path Trace')
        for state in reversed(path):
            self.printstate(state)


    def generateChilds(self,n):
        childs = []
        i,j = self.findIndex(n.state,0)
        #generate the valid indexes
        #The sequence is up,left,down,right
        validindexes = []
        if i-1 >=0:
            validindexes.append((i-1,j))
        if j-1 >=0:
            validindexes.append((i,j-1))
        if i+1 <3:
            validindexes.append((i+1,j))
        if j+1 <3:
            validindexes.append((i,j+1))
        for index,(row,col) in enumerate(validindexes):
            state = copy.deepcopy(n.state)
            temp = state[i][j]
            state[i][j] = state[row][col]
            state[row][col] = temp
            childs.append(self.createNode(state,n))
        return childs

    def checkifSameStateExistswithLowerFvalue(self,lists,n):
        for i,l in lists:
            if self.isTwoStatesEqual(l.state,n.state):
               if(l.f>n.f):
                    l = n
                    return True
               else:
                   return True
        return False

