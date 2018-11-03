from NQueens import NQueens
from math import ceil
if __name__ == '__main__':
    print("Enter the number of queens:",end=" ")
    noOfQueens = int(input())
    minIters = 100
    maxIters = 500
    nQueensHillClmbing = NQueens(noOfQueens)
    print("Hill Climbing with Steepest-Ascent Hill Climbing:")
    print("-"*50)
    success, successSteps, failures, failureSteps, noOfTimes = nQueensHillClmbing.steepestHillClimbingStats(minIters,maxIters)
    try:
        print("Success Rate:",(success/noOfTimes)*100)
        print("Failure Rate:",(failures/noOfTimes)*100)
        print("Average Number of Steps for Success:",ceil(successSteps/success))
        print("Average Number of Steps for Failures:",ceil(failureSteps/failures))
    except ZeroDivisionError:
        pass
    print()
    nQueensHillClmbing.steepesHillclimbingSequences()

    print("*"*50)
    print("*"*50)
    print()
    print("")
    print("Hill Climbing with Sideways Move")
    print("-"*50)
    success, successSteps, failures, failureSteps, noOfTimes = nQueensHillClmbing.SidewaysMoveStats(minIters,maxIters)
    try:
        print("Success Rate:",(success/noOfTimes)*100)
        print("Failure Rate:",(failures/noOfTimes)*100)
        print("Average Number of Steps for Success:",ceil(successSteps/success))
        print("Average Number of Steps for Failures:",ceil(failureSteps/failures))
    except ZeroDivisionError:
        pass
    print()
    for i in range(3):
        print("Search Sequence for RandomState: ",i+1)
        nQueensHillClmbing.sidewaysHillclimbingSequences()

    print("*"*50)
    print("*"*50)
    print()
    print("")
    print("Hill Climbing with Random Restarts")
    print("-" * 50)
    AvgRandomRestarts, avgSteps = nQueensHillClmbing.RandomRestartsWithSidewaysMoveStats(minIters,maxIters)
    print("The Average Number of Random Restarts used With Sideways Move:",AvgRandomRestarts)
    print("The Average Number of Steps used With Sideways Move:",avgSteps)

    AvgRandomRestarts, avgSteps = nQueensHillClmbing.RandomRestartsWithOutSidewaysMoveStats(minIters, maxIters)
    print("The Average Number of Random Restarts used WithOut Sideways Move:", AvgRandomRestarts)
    print("The Average Number of Steps used WithOut Sideways Move:", avgSteps)
    print("*" * 50)
    print("*" * 50)
    print("The End. :)")
    print("-----------")


