from Connect import Connect

class Search:
    def __init__(self):
        self.c = Connect()
        self.searchList = []
        self.state = self.c.array

    def expand(self,state,player):
        tempList = []
        tempState = state

        for i in range(10):
            for j in range(10):
                if(tempState[j,i] == 0.0):
                    tempState[j,i] = player
                    tempList.append(tempState.copy())
                    tempState[j,i] = 0
                    break

        return tempList

    def run(self):
        self.state = self.c.array
        temp = self.expand(self.state,1)
        temp2 = self.expand(temp[0],2)



    def checkWin(self,state):
        for i in range(7):
            for j in range(7):
                if((state[i][j] == state[i][j+1] == state[i][j+2] == state[i][j+3])):
                    if(1 == state[i][j+1] or 2 == state[i][j]):
                        return True
                if((state[i][j] == state[i+1][j] == state[i+2][j] == state[i+3][j])):
                    if(1 == state[i][j] or 2 == state[i][j]):
                        return True
                if((state[i][j] == state[i+1][j+1] == state[i+2][j+2] == state[i+3][j+3])):
                    if(1 == state[i][j] or 2 == state[i][j]):
                        return True
                if((state[i][j] == state[i+1][j-1] == state[i+2][j-2] == state[i+3][j-3])):
                    if(1 == state[i][j] or 2 == state[i][j]):
                        return True
        return False

    def dls(self,state,depth):
        if(self.checkWin(state)):
            return True
        if(depth <= 0) : return False

        adjacentList = self.expand(state)
        for i in adjacentList:
            if(self.dls(i,depth-1)):
                return True
        return False

    def IDDFS(self,startState,depth):
        for i in range(depth):
            if(self.dls(startState,i)):
                return True
        return False


def main():
    search = Search()
    search.run()




main()
