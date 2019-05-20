import numpy
from Agent import Agent



class Connect:
    def __init__(self):
        self.array = []
        self.createBoard()

    def createBoard(self):
        self.array = numpy.zeros((7, 6))
        '''array[2,1]=150'''

    def insertValue(self,column,player):
        for i in range(7):
            if(self.array[i,column] == 0.0):
                self.array[i,column] = player
                return


    def checkWin(self):
        #horizontal
        for i in range(7):
            for j in range(3):
                if(self.array[i][j] == self.array[i][j + 1] == self.array[i][j + 2] == self.array[i][j + 3]):
                    if(self.array[i][j] == 1 or self.array[i][j] == 2):
                        return True
        #vertical
        for i in range(4):
            for j in range(6):
                if(self.array[i][j] == self.array[i + 1][j] == self.array[i+2][j] == self.array[i+3][j]):
                    if(self.array[i][j] == 1 or self.array[i][j] == 2):
                        return True
        #+diagonal
        for i in range(4):
            for j in range(3):
                if(self.array[i][j] == self.array[i + 1][j + 1] == self.array[i+2][j+2] == self.array[i+3][j+3]):
                    if(self.array[i][j] == 1 or self.array[i][j] == 2):
                        return True
        #-diagonal
        for i in range(3,7):
            for j in range(3):
                if(self.array[i][j] == self.array[i-1][j+1] == self.array[i-2][j+2] == self.array[i-3][j+3]):
                    if(self.array[i][j] == 1 or self.array[i][j] == 2):
                        return True

        return False


def main():
    c = Connect()
    agent = Agent()
    index = 1;
    column = 0;
    win = False
    while column != 'q' or win == False :
        if(index == 1):
            column = input("column: ")
            c.insertValue(int(column),index)
        else:


            c.insertValue(agent.insertValue(c.array),index)
            #column = input("column: ")
            #c.insertValue(int(column),index)

        if(c.checkWin()):
            win = True
            print("Win")
        if(index == 1):
            index = 2
        else:
            index = 1
        print(numpy.flip(c.array,0))


main()


# c = Connect();
# index = 1;
# row = 0;
# column = 0;
# while row or column != 'q':
#     column = input("column: ")
#     c.insertValue(int(column),index)
#     if(c.checkWin()):
#         print("Win")
#     if(index == 1):
#         index = 2
#     else:
#         index = 1

# main()
