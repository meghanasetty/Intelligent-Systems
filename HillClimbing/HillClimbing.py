from random import randint
from math import ceil

class HillClimbing:
    def __init__(self,noOfQueens):
        self.noOfQueens = noOfQueens
        self.initialState = None

    def isGoalState(self,state):
        if state.hvalue == 0:
            return True
        return False

    def compareHValues(self, state1, state2):
        pass

    def generateInitialState(self):
        pass

    def generateSuccessor(self,CurrentState):
        pass

    def steepestHillClimbingStats(self,minIters=100,maxIters=500,Seq=False):
        if Seq:
            iterations = 3
        else:
            iterations = randint(minIters,maxIters)
        success = 0
        successsteps = 0
        failuresteps = 0
        totalsteps = 0
        failures = 0
        for i in range(iterations):
            iniState = self.generateInitialState()
            if(self.isGoalState(iniState)):
                continue
            currstate = iniState
            if Seq:
                print("Search Sequence for RandomState: ", i + 1)
                currstate.printState()
            loopsteps = 0
            while(True):
                isnotCurrState = False

                for successor in self.generateSuccessor(currstate):
                    if self.compareHValues(currstate,successor) == 1:
                        #currstate is greater than successor
                        currstate = successor
                        isnotCurrState = True
                loopsteps +=1
                if Seq and isnotCurrState:
                    currstate.printState()

                if self.isGoalState(currstate) and isnotCurrState:
                    successsteps += loopsteps
                    success += 1
                    totalsteps += loopsteps
                    if Seq:
                        print("Goal Reached")
                    break
                if isnotCurrState == False:
                    failuresteps += loopsteps
                    failures += 1
                    totalsteps +=loopsteps
                    if Seq:
                        print("Goal Not Reached")
                    break

        return success, successsteps, failures, failuresteps, iterations

    def steepesHillclimbingSequences(self):
        self.steepestHillClimbingStats(Seq=True)

    def SidewaysMoveStats(self,minIters=100,maxIters=500,Seq=False):
        if Seq:
            iterations = 3
        else:
            iterations = randint(minIters, maxIters)
        success = 0
        successsteps = 0
        failuresteps = 0
        totalsteps = 0
        failures = 0
        for i in range(iterations):
            iniState = self.generateInitialState()
            if (self.isGoalState(iniState)):
                continue
            currstate = iniState
            if Seq:
                print("Search Sequence for RandomState: ", i + 1)
                currstate.printState()
            isnotCurrState = False
            loopsteps = 0
            sidewayiterations = 100
            while (True):
                isnotCurrState = False
                equalsuccstates = []
                for successor in self.generateSuccessor(currstate):
                    compval = self.compareHValues(currstate, successor)
                    if compval == 1:
                        # currstate is greater than successor
                        currstate = successor
                        isnotCurrState = True
                        sidewayiterations = 100
                    elif compval == 0:
                        equalsuccstates.append(successor)
                loopsteps += 1
                if Seq and isnotCurrState:
                    currstate.printState()
                if self.isGoalState(currstate) and isnotCurrState:
                    successsteps += loopsteps
                    success += 1
                    totalsteps += loopsteps
                    if Seq:
                        print("Goal Reached")
                    break
                if isnotCurrState == False:
                    if len(equalsuccstates) == 0 or sidewayiterations == 0:
                        failuresteps += loopsteps
                        failures += 1
                        totalsteps += loopsteps
                        if Seq:
                            print("Goal Not Reached")
                        break
                    else:
                        i = randint(0,len(equalsuccstates)-1)
                        currstate = equalsuccstates[i]
                        if Seq:
                            currstate.printState()
                        sidewayiterations -=1
        return success, successsteps, failures, failuresteps, iterations

    def sidewaysHillclimbingSequences(self):
        self.SidewaysMoveStats(Seq=True)

    def RandomRestartsWithOutSidewaysMoveStats(self,minIters,maxIters):
        iterations = randint(minIters, maxIters)
        totalrestarts = 0
        totalsteps = 0
        for i in range(iterations):
            iniState = self.generateInitialState()
            if (self.isGoalState(iniState)):
                continue
            currstate = iniState

            while(True):
                loopsteps = 0
                while (True):
                    isnotCurrState = False
                    for successor in self.generateSuccessor(currstate):
                        if self.compareHValues(currstate, successor) == 1:
                            #currstate is greater than successor
                            currstate = successor
                            isnotCurrState = True
                    loopsteps += 1
                    if self.isGoalState(currstate) and isnotCurrState:
                        totalsteps += loopsteps
                        break
                    if isnotCurrState == False:
                        totalsteps += loopsteps
                        break
                if not self.isGoalState(currstate):
                    currstate = self.generateInitialState()
                    totalrestarts += 1
                else:
                    break
        return ceil(totalrestarts/iterations), ceil(totalsteps/iterations)

    def RandomRestartsWithSidewaysMoveStats(self,minIters,maxIters):
        iterations = randint(minIters, maxIters)
        totalrestarts = 0
        totalsteps =  0
        for i in range(iterations):
            iniState = self.generateInitialState()
            if (self.isGoalState(iniState)):
                continue
            currstate = iniState

            while (True):
                sidewayiterations = 100
                loopsteps = 0
                while (True):
                    isnotCurrState = False
                    equalsuccstates = []
                    for successor in self.generateSuccessor(currstate):
                        compval = self.compareHValues(currstate, successor)
                        if compval == 1:
                            # currstate is greater than successor
                            currstate = successor
                            isnotCurrState = True
                            sidewayiterations = 100
                        elif compval == 0:
                            equalsuccstates.append(successor)
                    loopsteps += 1
                    if self.isGoalState(currstate) and isnotCurrState:
                        totalsteps += loopsteps
                        break
                    if isnotCurrState == False:
                        if len(equalsuccstates) == 0 or sidewayiterations == 0:
                            totalsteps += loopsteps
                            break
                        else:
                            i = randint(0, len(equalsuccstates) - 1)
                            currstate = equalsuccstates[i]
                            sidewayiterations -= 1

                if not self.isGoalState(currstate):
                    currstate = self.generateInitialState()
                    totalrestarts += 1
                else:
                    break
        return ceil(totalrestarts / iterations), ceil(totalsteps / iterations)
