import marble_solitire_env as environment
from collections import defaultdict
from queue import PriorityQueue
import heapq

inital_state = environment.initial_state
explored = defaultdict(tuple)
frontier = PriorityQueue()

root_node = environment.Node(state=inital_state)
frontier.put((root_node.cost,root_node))

current_node = environment.Node(state=inital_state)


def check_frontier(state, inital_state):        # used for updating a node with given state
    f = 0
    for i in frontier.queue:
        # print(i)
        if(i[1].state == state):
            if(i[1].cost > current_node.cost +1):
                i[1].cost = current_node.cost+1
                i[1].parent = current_node     
            
            return True

    return False




while not frontier.empty():
    # print(frontier.get()[1])
    # print("quw =",frontier.queue )
    current_node = frontier.get()[1]
    print(len(current_node.visited))
    # print("hello ",current_node.state)
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
                    # print(current_node)
                    new_node = environment.Node(parent=current_node, state=i, cost=current_node.cost+1, visited=[*current_node.visited]+[current_node])
                    # print("cost = ",new_node.cost)
                    # heapq.heappush(frontier, (new_node.cost, new_node))
                    frontier.put((new_node.cost,new_node))
                    print(frontier.queue)

# print("explored  \n\n",explored)


# for i in explored:
#     print(i)

final_states = []
if(current_node.parent != None):
    while (current_node.parent != None):
        final_states.append(list(current_node.state))
        current_node = current_node.parent

else:
    print("No possible path.")