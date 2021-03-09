import environment
from collections import defaultdict
from queue import PriorityQueue
import heapq
from memory_profiler import profile 
from utils import track

inital_state = environment.initial_state
explored = defaultdict(tuple)
frontier = PriorityQueue()

root_node = environment.Node(state=inital_state,)
frontier.put((root_node.cost, root_node))


# current_node = environment.Node(state=inital_state)
# print(current_node)

def check_frontier(state, current_node):
    f = 0
    for i in frontier.queue:
        # print(i)
        if(i[1].state == state):
            if(i[1].cost > current_node.cost +1):
                i[1].cost = current_node.cost+1
                i[1].parent = current_node     
            
            return True

    return False

@track
def my_func():
    while not frontier.empty():
        current_node = frontier.get()[1]
        print(len(current_node.visited))
        if(environment.Node.goal_test(current_node)):
            for i in current_node.visited:
                print(i.state)
            print(current_node.state)
            break

        else:
            explored[   tuple(map(tuple, current_node.state))   ] = 1      # 1 = visited
            possible_states = environment.Node.successor(current_node)
            
            for i in possible_states:
                if (explored[ tuple(map(tuple, i))  ] == 1):
                    continue
                
                else:
                    if (check_frontier(i,current_node)):
                        continue            
                    else:
                        new_node = environment.Node(parent=current_node, state=i, cost=current_node.cost+1,visited =  [*current_node.visited]+[current_node])
                    # print("cost = ",new_node.cost)
                    frontier.put((new_node.cost, new_node))

# print("explored  ",explored)

    if(current_node.parent != None):
        while (current_node.parent != None):
            # print(list(current_node.state))
            current_node = current_node.parent

    else:
        print("No possible path.")


if __name__ == '__main__':
    my_func()
