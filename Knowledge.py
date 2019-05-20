class Knowledge():

    def __init__(self):
        self.threat = []

    def searchThreat(self,state):
        for i in range(7):
            for j in range(3):
                if(j == 0):
                    if((state[i][j] == state[i][j+1] == state[i][j+2])
                    and state[i][j+3] == 0):
                        if(state[i][j] == 1 or state[i][j] == 2):
                             d = {'threat': True,'loc1':j+3}
                             return d
                elif(j == 5):
                    if((state[i][j] == state[i][j+1] == state[i][j+2])
                    and state[i][j-1] == 0):
                        if(state[i][j] == 1 or state[i][j] == 2):
                            d = {'threat': True,'loc1':j-1}
                            return d
                else:
                    if((state[i][j] == state[i][j+1] == state[i][j+2])
                    and (state[i][j-1] == 0)):
                        if(state[i][j] == 1 or state[i][j] == 2):
                            d = {'threat': True,'loc1':j-1, 'loc2':j+3}
                            return d
        return {'threat': False}
