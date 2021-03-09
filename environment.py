# goal_state = [[7,3,4],[6,5,1],[8,2,0]]          # 0 is blank 
# initial_state = [[6,7,3],[0,5,4],[8,2,1]]
goal_state = [[1,7,0],[6,8,5],[4,3,2]]
initial_state = [[0,1,3],[7,6,8],[4,2,5]]

from copy import deepcopy

class Node:
    def __init__(self, parent = None, state = None ,cost = 0, visited=[]):  # visited = [] for storing the path taken by the current node 
        self.cost = cost
        self.parent = parent
        self.state = state
        self.visited = [*visited]
   
    def goal_test(self):
        # print(type(self.state),type(goal_state))
        if (self.state == goal_state):
            return True
        else:
            return False

    def validate(self, i, j):
        if(i>=0 and i<=2 and j>=0 and j<=2):
            return True
        else:
            return False

    def __lt__(self, other):
        return self.cost < other.cost

    def successor(self):
        
        current_state = self.state
        x,y = 0,0

        final_states = []

        for i in range(len(goal_state)):
            for j in range(len(goal_state[0])):
                if current_state[i][j] == 0:
                    x = i
                    y = j
                    break
        
        a = [0,0,1,-1]
        b = [1,-1,0,0]

        for i in range(4):
            if (self.validate(x+a[i],y+b[i])):
                new_state = deepcopy(current_state)
                new_state[x][y] = new_state[x+a[i]][y+b[i]]
                new_state[x+a[i]][y+b[i]] = 0

                final_states.append(new_state)

        return final_states
                












