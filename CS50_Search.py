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

    def containsState(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0
    
    # Pop first element
    def removeNodeBreadth(self):
        node = self.toExploreNodes[0]
        self.searchedNodes.append(node)
        self.toExploreNodes = self.toExploreNodes[1:]
        return node

    # Pop last element
    def removeNodeDepth(self):
        node = self.toExploreNodes[-1]
        self.searchedNodes.append(node)
        self.toExploreNodes = self.toExploreNodes[:-1]
        return node

class Maze:
    def __init__(self,maze,start,goal):
        self.maze = maze
        self.startState = start
        self.goalState = goal
        self.width = None
        self.height = None
    
    def getWidth(self):
        if self.width == None:
            self.width = len(self.maze)
        return self.width

    def getWidth(self):
        if self.height == None:
            self.height = len(self.maze)
        return self.height

    def isStartState(self, el):
        return el == 'A'

    def isGoalState(self, el):
        return el == 'B'

    def isWall(self, el):
        return el == '#'

    def isSpace(self, el):
        return el == ' '  # or '' if that is truly your design
        

class MazeSolver:
    def __init__(self,maze):
        self.maze = maze

    # def ations(self):

    def neighbours(self,state):
        print('TO DO')

    # def results(self):

    def solveMaze(self):

        Start = Node(self.maze.startState, None, None, 1)
        
        Frontier = FrontierExplored()
        Frontier.appendNode(Start)

        while not Frontier.empty():
            nextNode = Frontier.removeNodeBreadth()

            if nextNode == self.maze.isGoalState():
                Frontier.appendNode(nextNode)
                break
            else:
                Frontier.appendNode(self.neighbours(nextNode))

        if Frontier.searchedNodes[-1] == self.maze.isGoalState():
            print('Solution Found!')
            print(Frontier.searchedNodes)
        else:
            print('Error')
        

def Main():

    ## create maze as an array with #,  , A and B

    ## create the Maze object

    print('MazeSolver')


if __name__ == "__main__":
    Main()

