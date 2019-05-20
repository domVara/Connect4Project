import numpy


class Knowledge():

    def __init__(self):
        self.threat = []

    def searchThreat(self,state):
        for i in range(7):
            for j in range(3):
                if(j == 0):
                    if((state[i][j] == state[i][j+1] == state[i][j+2])
                    and state[i][j+3] == 0):
                        if(state[i][j] == 1):
                            d = {'threat': True,'loc1':j+3, 'WinningMove': False}
                            return d
                        elif(state[i][j] == 2):
                            d = {'threat': False,'loc1':j+3, 'WinningMove': True}
                            return d

                elif(j == 5):
                    if((state[i][j] == state[i][j+1] == state[i][j+2])
                    and state[i][j-1] == 0):
                        if(state[i][j] == 1):
                            d = {'threat': True,'loc1':j+3, 'WinningMove': False}
                            return d
                        elif(state[i][j] == 2):
                            d = {'threat': False,'loc1':j+3, 'WinningMove': True}
                            return d
                else:
                    if((state[i][j] == state[i][j+1] == state[i][j+2])
                    and (state[i][j+3] == 0 or state[i][j-1] == 0)):
                        if(state[i][j] == 1 and state[i][j+3] == 0):
                            d = {'threat': True,'loc1':j+3, 'WinningMove': False}
                            return d
                        elif(state[i][j] == 2):
                            d = {'threat': False,'loc1':j+3, 'WinningMove': True,}
                            return d
                        if(state[i][j] == 1 and state[i][j-1] == 0):
                            d = {'threat': True,'loc1':j-1, 'WinningMove': False}
                            return d
                        elif(state[i][j] == 2):
                            d = {'threat': False,'loc1':j-1, 'WinningMove': True,}
                            return d

        for i in range(4):
            for j in range(6):
                if(state[i][j] == state[i + 1][j] == state[i+2][j] and state[i+3][j] == 0):
                    if(state[i][j] == 1):
                        d = {'threat': True,'loc1':j, 'WinningMove': False}
                        return d
                    elif(state[i][j] == 2):
                        d = {'threat': False,'loc1':j, 'WinningMove': True}
                        return d


        for i in range(4):
            for j in range(3):
                if(i == 0):
                    if(state[i][j] == state[i+1][j+1] == state[i+2][j+2]
                    and state[i+3][j+3] == 0):
                        if(state[i][j] == 1):
                            d = {'threat': True,'loc1':j, 'WinningMove': False}
                            return d
                        elif(state[i][j] == 2):
                            d = {'threat': False,'loc1':j, 'WinningMove': True}
                            return d
                if(j == 5):
                    if(state[i][j] == state[i+1][j+1] == state[i+2][j+2]
                    and state[j-1][j-1] == 0):
                        if(state[i][j] == 1):
                            d = {'threat': True,'loc1':j, 'WinningMove': False}
                            return d
                        elif(state[i][j] == 2):
                            d = {'threat': False,'loc1':j, 'WinningMove': True}
                            return d

        return {'threat': False, 'WinningMove': False}

    def checkEmptyBoard(self,state):
        if(numpy.count_nonzero(state == 0) > 36):
            return True
        else:
            False

    # def buildCentralThreat(self,state):
    #     for
