from eightPuzzle import eightPuzzle

def parseInput():
    r1 = input()
    r2 = input()
    r3 = input()
    inputlist = [list(map(int, r1.split(' '))),list(map(int, r2.split(' '))),list(map(int, r3.split(' ')))]
    return inputlist


if __name__ == '__main__':
    print('Enter the input state:')
    inputState = parseInput()
    print('Enter the goal state:')
    goalState = parseInput()
    checkinglenInputList = inputState[0]+inputState[1]+inputState[2]
    checkinglenGoalList = goalState[0]+goalState[1]+goalState[2]
    #validation of initial and goal states.
    if len(checkinglenInputList) != 9 or len(checkinglenGoalList) !=9:
        print('bad input')
    elif len(set(checkinglenInputList) - set([0,1,2,3,4,5,6,7,8])) != 0 or len(set(checkinglenGoalList) - set([0,1,2,3,4,5,6,7,8])) != 0:
        print('bad input')
    else:
        isManhattanDistance = False
        hueristic = input('hueristic function?\n1.Manhattan Distance \n2.Misplaced Tiles\n(1/2) :')
        hueristic = int(hueristic)
        if hueristic == 1:
            isManhattanDistance = True
        puzzle = eightPuzzle(inputState,goalState,isManhattanDistance)
        #A* algorithm
        goalNode = puzzle.AstarSearch()

        #print the path from the input state to the goal state
        puzzle.printPath(goalNode)


        print('The number of nodes generated ', puzzle.noofNodesGenerated)
        print('The number of nodes expanded ', len(puzzle.expanded)+1)