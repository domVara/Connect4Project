import numpy

class Connect:

    def __init__(self):
        self.array = []
        self.createBoard()
        self.win = False;

    def createBoard(self):
        self.array = numpy.zeros((10, 10))
        '''array[2,1]=150'''

    def insertValue(self,row,column,player):
        if self.array[row,column] == 0:
            self.array[row,column] = player;
        self.checkWin(row,column);
        print(self.array)
        if(self.win == True):
            print("YEET")

    def checkWin(self,row,column):
        for i in range(7):
            for j in range(7):
                if((self.array[i][j] == self.array[i][j+1] == self.array[i][j+2] == self.array[i][j+3])):
                    if(1 == self.array[i][j+1] or 2 == self.array[i][j]):
                        print("GG")
                        self.win = True;
                        return
                if((self.array[i][j] == self.array[i+1][j] == self.array[i+2][j] == self.array[i+3][j])):
                    if(1 == self.array[i][j] or 2 == self.array[i][j]):
                        print("GG")
                        self.win = True;
                        return
                if((self.array[i][j] == self.array[i+1][j+1] == self.array[i+2][j+2] == self.array[i+3][j+3])):
                    if(1 == self.array[i][j] or 2 == self.array[i][j]):
                        print("GG")
                        self.win = True;
                        return
                if((self.array[i][j] == self.array[i+1][j-1] == self.array[i+2][j-2] == self.array[i+3][j-3])):
                    if(1 == self.array[i][j] or 2 == self.array[i][j]):
                        print("GG")
                        self.win = True;
                        return

c = Connect();
index = 1;
row = 0;
column = 0;
while row or column != 'q':
    row = input("row: ");
    column = input("column: ")
    c.insertValue(int(row),int(column),index)
    if(index == 1):
        index = 2
    else:
        index = 1


print(c.array)
