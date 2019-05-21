from Connect import Connect
from treelib import Node, Tree
import numpy
import pdb

class Element():
    def __init__(self,state,parent):
        self.state = state
        self.parent = parent

    def __init__(self,state):
        self.state = state



class Search:
    def __init__(self):
        self.c = Connect()
        self.searchList = []
        self.state = self.c.array
        self.found = []

    def expand(self,state,player):
        tempList = []
        tempState = state
        for i in range(5, -1, -1):
            for j in range(6, 0, -1):
                if(tempState[j,i] == 0.0):
                    tempState[j,i] = player
                    tempList.append(tempState.copy())
                    tempState[j,i] = 0
                    break

        return tempList

    def run(self):
        self.state = self.c.array
        state = numpy.array(
                         [[0., 0., 0., 0., 0., 0.],
                         [0., 0., 0., 0., 0., 0.],
                         [0., 0., 0., 0., 0., 0.],
                         [0., 0., 0., 0., 0., 0.],
                         [0., 0., 0., 0., 0., 0.],
                         [0., 0., 1., 2,  2., 0.],
                         [0., 0., 2., 1., 1., 0.]])
        numpy.flip(state,0)
        print(self.IDDFS(state,6))
        print(self.found)
        self.findInsertedValue(state,self.found)


    def checkWin(self,state):
        #horizontal
        for i in range(7):
            for j in range(3):
                if(state[i][j] == state[i][j + 1] == state[i][j + 2] == state[i][j + 3]):
                    if(state[i][j] == 1 or state[i][j] == 2):
                        return True
        #vertical
        for i in range(4):
            for j in range(6):
                if(state[i][j] == state[i + 1][j] == state[i+2][j] == state[i+3][j]):
                    if(state[i][j] == 1 or state[i][j] == 2):
                        return True
        #+diagonal
        for i in range(4):
            for j in range(3):
                if(state[i][j] == state[i + 1][j + 1] == state[i+2][j+2] == state[i+3][j+3]):
                    if(state[i][j] == 1 or state[i][j] == 2):
                        return True
        #-diagonal
        for i in range(3,7):
            for j in range(3):
                if(state[i][j] == state[i-1][j+1] == state[i-2][j+2] == state[i-3][j+3]):
                    if(state[i][j] == 1 or state[i][j] == 2):
                        return True

        return False

    def dls(self,treeNode,depth,level):
        #print(treeNode.state)
        if(self.checkWin(treeNode.state)):
            current = treeNode
            while(current.parent != None):
                print(current.parent.state)
                current = current.parent
                self.found.append(current.state)
            return True
        if(depth <= 0) : return False
        if(level % 2 == 1):
            increment = 2
        else:
            increment = 1
        adjacentList = self.expand(treeNode.state,increment)
        level = level + 1
        #print(adjacentList)
        for i in adjacentList:
            child = Element(i)
            child.parent = treeNode
            if(self.dls(child,depth-1,level)):
                return True
        return False

    def IDDFS(self,state,depth):
        head = Element(state)
        head.parent = None
        #pdb.set_trace()
        level = 1
        for i in range(depth):
            if(self.dls(head,i,level)):
                return True
        return False

    def findInsertedValue(self,initialState, changeState):
        newState = initialState[len(changeState)-1]
        print(newState)
        for i in range(7):
            for j in range(6):
                if(initialState[i][j] != newState[i][j]):
                    return j



def main():
    search = Search()
    search.run()





main()
