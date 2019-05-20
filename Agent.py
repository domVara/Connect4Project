import random
from Knowledge import Knowledge


class Agent():

    def insertValue(self,state):
        k = Knowledge();
        val = k.searchThreat(state)
        print(val)


        # if(val['threat']):
        #     if(val['loc1']):
        #         return val['loc1']
        #     else:
        #         return val['loc2']
        #
        # if(val['WinningMove']):
        #     if(val['loc1']):
        #         return val['loc1']
        #     else:
        #         return val['loc2']

        if(k.checkEmptyBoard(state)):
            print("True")
        else:
            print("False")


        return random.randint(0, 5)
