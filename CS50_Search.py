# 
class Node:
    def __init__(self, state, parent, actions, pathCost):
        self.state = state
        self.parent = parent
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
    
    # Pop first element
    def removeNodeBreadth(self):
        node = self.toExploreNodes[0]
        self.searchedNodes.append(self.toExploreNodes[0])
        self.toExploreNodes = self.toExploreNodes[1:]
        return node

    # Pop last element
    def removeNodeDepth(self):
        node = self.toExploreNodes[-1]
        self.searchedNodes.append(self.toExploreNodes[-1])
        self.toExploreNodes = self.toExploreNodes[:-1]
        return node

class Maze:
    def __init__(self):
        self.startState = None
        self.goalState = None

    def isStartState(self, el):
        return el == 'A'

    def isGoalState(self, el):
        return el == 'B'

    def isWall(self, el):
        return el == '#'

    def isSpace(self, el):
        return el == ' '  # or '' if that is truly your design

    def setStartState(self, el):
        if self.isStartState(el):
            self.startState = el

    def setGoalState(self, el):
        if self.isGoalState(el):
            self.goalState = el
        

class MazeSolver:
    def __init__(self,maze):
        self.maze = maze

    # def ations(self):

    # def results(self):

    # def solveMaze(self):

def Main():

    ## create maze as an array with #,  , A and B

    ## create the Maze object

    print('MazeSolver')


if __name__ == "__main__":
    Main()

