class State:
    def __init__(self,n,queenpositions):
        self.queenpositions = queenpositions
        self.n = n
        self.board = self.generateBoard()
        self.hvalue = self.calculateHValue()

    def printState(self):
        if self.board is not None:
            for i in range(self.n):
                for j in range(self.n):
                    if self.board[i][j] == 1:
                        print("Q",end=" ")
                    else:
                        print("0",end=" ")
                print()
            print()

    def generateBoard(self):
        board = []
        for i in range(self.n):
            row = [0] * self.n
            board.append(row)

        for x,y in self.queenpositions:
            board[x][y] = 1
        return board

    def calculateHValue(self):
        linecost = 0
        diagnalcost = 0

        #calculating linecost
        for x,y in self.queenpositions:
            for index in range(self.n):
                if self.board[x][index] == 1:
                    linecost +=1
                if self.board[index][y] == 1:
                    linecost +=1
            #eliminate it from counting itself
            linecost -=2

            #left- up
            index1, index2 = x - 1, y - 1
            while index1 >= 0 and index2 >= 0:
                if self.board[index1][index2] == 1:
                    diagnalcost += 1
                index1 -= 1
                index2 -= 1
            #right - down
            index1, index2 = x + 1, y + 1
            while index1 < self.n and index2 < self.n:
                if self.board[index1][index2] == 1:
                    diagnalcost += 1
                index1 += 1
                index2 += 1
            #left - down
            index1, index2 = x + 1, y - 1
            while index1 < self.n and index2 >= 0:
                if self.board[index1][index2] == 1:
                    diagnalcost += 1
                index1 += 1
                index2 -= 1
            #right - up
            index1, index2 = x - 1, y + 1
            while index1 >= 0 and index2 < self.n:
                if self.board[index1][index2] == 1:
                    diagnalcost += 1
                index1 -= 1
                index2 += 1

        return (diagnalcost+linecost)/2


