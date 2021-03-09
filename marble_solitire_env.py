# goal_state = [[-1,-1,0,0,0,-1,-1],[-1,-1,0,0,0,-1,-1],[0,0,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[-1,-1,0,0,0,-1,-1],[-1,-1,0,0,0,-1,-1]]          

goal_state = [
 [-1,-1,1,1,1,-1,-1],
 [-1,-1,1,1,1,-1,-1],
 [1,1,1,1,1,1,1],
 [1,1,1,1,1,0,1],
 [1,1,1,1,0,1,1],
 [-1,-1,0,0,1,-1,-1],
 [-1,-1,1,1,1,-1,-1]
]
initial_state = [[-1,-1,0,1,1,-1,-1],[-1,-1,1,1,1,-1,-1],[1,1,1,1,1,1,1],[1,1,1,0,1,1,1],[1,1,1,1,1,1,1],[-1,-1,1,1,1,-1,-1],[-1,-1,1,1,1,-1,-1]]

from copy import deepcopy

class Node:
    def __init__(self,parent = None, state = [[]],cost = 0, visited = []):  # visited = [] for storing the path taken by the current node 
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
        if(i>=0 and i<7 and j>=0 and j<7):
            return True
        else:
            return False

    def __lt__(self, other):            # to resolve the problem of same priority present in out frontier
        return self.cost < other.cost

    def successor(self):
        
        current_state = self.state
        x,y = 0,0

        a = [0,0,2,-2]
        b = [2,-2,0,0]

        final_states = []

        for i in range(len(goal_state)):
            for j in range(len(goal_state[0])):
                if current_state[i][j] == 1:

                    for k in range(4):
                        if ( self.validate(i+a[k],j+b[k]) and current_state[i+a[k]][j+b[k]]==0 ):
                            new_state = deepcopy(current_state)
                            new_state[i][j] = 0
                            new_state[i+a[k]][j+b[k]] = 1
                            new_state[   ((2 * i) + a[k]) //2   ][((2 * j) + b[k]) //2] = 0

                            final_states.append(new_state)

        return final_states