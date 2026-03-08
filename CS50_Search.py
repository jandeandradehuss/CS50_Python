# 
class Node:
    def __init__(self, state, parent = None, actions = None, pathCost = 1):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.pathCost = pathCost

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

    def isEmpty(self):
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
    def __init__(self,maze):
        
        if len(maze) <= 0:
            raise Exception("maze must be a 2D-ARRAY")
        else:
            if len(maze) != len(maze[0]):
                raise Exception("maze must be a quadratic 2D-ARRAY")
        if not any('A' in row for row in maze):
            raise Exception("maze must have exactly one START point")
        if not any('B' in row for row in maze):
            raise Exception("maze must have exactly one END point")

        self.maze = maze
        self.startState = start
        self.goalState = goal
        self.width = None
        self.height = None

    def createMazeOfNodes(self,mazeArr):
        mazeOfNodes = []
        mazeRow = []

        coords = [(r, c) for r, row in enumerate(mazeArr) 
          for c, val in enumerate(row) Node([(r, c)])]

        

    
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

