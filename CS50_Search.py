# 
class Node:
    def __init__(self, state, parent, actions, pathCost):
        self.state
        self.parent
        self.actions
        self.pathCost

class FrontierExplored:
    def __init__(self):
        self.toExploreNodes = []
        self.searchedNodes = []

    # Append
    def appendNode(self, newNodes):
        if newNodes not in self.searchedNodes:
            self.toExploreNodes.append(newNodes)
    
    # Pop 
    def removeNode(self):
        node = self.toExploreNodes[0]
        self.searchedNodes.append(self.toExploreNodes[0])
        self.toExploreNodes = self.toExploreNodes[1:]
        return node

class Maze:
    def __init__(self,maze):
        self.maze
        self.goalNode
        self.startNode


    # def ations(self):

    # def results(self):

    # def solveMaze(self):

def Main():

    ## create maze as an array with #,  , A and B

    ## create the Maze object

    print('MazeSolver')