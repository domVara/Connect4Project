import random
from Knowledge import Knowledge


class Agent():

    def insertValue(self,state):
        k = Knowledge();
        val = k.searchThreat(state)
        print(val)
        if(val['threat']):
            if(val['loc1']):
                return val['loc1']
            else:
                return val['loc2']

        return random.randint(0, 5)
