from HillClimbing import HillClimbing
from State import State
from random import randint
from copy import deepcopy as copy

class NQueens(HillClimbing):
    def __init__(self, n):
        HillClimbing.__init__(self,n)


    def generateInitialState(self):
        #the y positions is fixed where as the x postion is picked randomly. This is done to minimize the number of steps
        queenpositions = []
        for y in range(self.noOfQueens):
            x = randint(0,self.noOfQueens-1)
            queen = [x,y]
            queenpositions.append(queen)
        #print(*queenpositions, sep=", ")
        initialState = State(self.noOfQueens,queenpositions)
        self.initialState = initialState
        return initialState

    def generateSuccessor(self,CurrentState):
        for index,[x,y] in enumerate(CurrentState.queenpositions):
            for xcord in range(self.noOfQueens):
                    if CurrentState.board[xcord][y] != 1:
                        successor = copy(CurrentState.queenpositions)
                        successor[index] = [xcord,y]
                        successorState = State(self.noOfQueens,successor)
                        yield successorState


    def compareHValues(self,state1,state2):
        if state1.hvalue < state2.hvalue:
            return -1
        elif state1.hvalue > state2.hvalue:
            return 1
        else:
            return 0
