##### Search Algorithms for use in GUI. #####

from collections import deque
import config
import helper
import heapq

### For Implementation of A* Algorithm
class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def is_empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item)) # Pushing the Priority and the fValue in MinHeap
    
    def get(self):
        return heapq.heappop(self.elements)[1] # Removing and Returning the fValue from MinHeap

# Depth First Search Algorithm - Iterative Approach (LIFO Mechanism)
def dfs(board, start, goal):
    stack = [start]
    visited = set()
    path = []

    # Iterating While the Stack is not Empty
    while stack:
        current = stack.pop()
        path.append(current)
        if current == goal: # Checking is Goal is Reached
            return path

        for direction in ["up", "right","down", "left"]:    # Exploring Neighbours of Current Position in All Directions Except Diagonals
            rowOffset, columnOffset = config.offsets[direction]
            neighbour = (current[0] + rowOffset, current[1] + columnOffset)
            if helper.withInBounds(board, neighbour) and neighbour not in visited:  # Checking is Neighbour is in Bounds and Not Already Visited
                stack.append(neighbour)
                visited.add(neighbour)


# Breadth First Search Algorithm (FIFO Mechanism)
def bfs(board, start, goal):
    queue = deque()
    queue.append(start)
    visited = set()
    path = []

    # Iterating While the Queue is not Empty
    while queue:
        current = queue.popleft()   # Extracting Position from Left of the Queue
        path.append(current)
        if current == goal: # Checking is Goal is Reached
            return path
        
        for direction in ["up", "right", "down", "left"]:
            rowOffset, columnOffset = config.offsets[direction]
            neighbour = (current[0] + rowOffset, current[1] + columnOffset)
            if helper.withInBounds(board, neighbour) and neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)


# Helper Funnction to Calculate Manhattan Distance
def heuristic(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)

# A* Algorithm (Priority Expansion Mechanism)
def a_star(board, start, goal):
    pq = PriorityQueue()    # Creating Instance of Priority Queue
    pq.put(start, 0)    # Adding Start Element with Lowest Priority
    gValues = {}    # Dictionary to store position and priority i.e., 'pos' = 'gValue'
    gValues[start] = 0
    path = []

    # Iterating While the Priority Queue is not Empty
    while not pq.is_empty():
        currentPos = pq.get()   # Extracting Position with Highest Priority
        path.append(currentPos)

        if currentPos == goal: # Checking is Goal is Reached
            return path
        
        for direction in ["up", "right", "down", "left"]:
            rowOffset, columnOffset = config.offsets[direction]
            neighbour = (currentPos[0] + rowOffset, currentPos[1] + columnOffset)
            newCost = gValues[currentPos] + 1 # Cost to Reach the New Position (1 Can be Substituted for Edge-Weight)
            if helper.withInBounds(board, neighbour):
                if neighbour not in gValues or newCost < gValues[neighbour]: # Checking if neighbour is not already visited and the cost of reaching it is the lowest
                    gValues[neighbour] = newCost    # Updating the gValue of Neighbour to NewCost
                    fValue = newCost + heuristic(goal, neighbour)   # fValue Calculated using above Helper Function
                    pq.put(neighbour, fValue)   # Neighbour Added to Priority Queue i.e., Priority = fValue