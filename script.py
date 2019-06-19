import fileinput
import sys
from Graph import *
from copy import deepcopy


def algorithm():
    backup = []
    index = 0
    while not g.goal_check():
        actions = g.actions()
        if not actions:
            if not backup:
                print("NOT SOLVABLE")
                break
            else:
                this_backup = backup.pop()
                g.rocket = this_backup[0]
                g.lucky = this_backup[1]
                del output[-1]
                index = this_backup[2] + 1
        else:
            for i in range(len(actions)):
                if actions[i][0] == int(num_of_points) - 1:
                    g.do(actions[i])
                    output.append(actions[i])
                    return
            backup.append([deepcopy(g.rocket), deepcopy(g.lucky), index])
            g.do(actions[index])
            output.append(actions[index])
            index = 0


# GET INPUT FROM FILE
Input = fileinput.input(sys.argv[1])
line1 = Input[0].replace('\n', '').split(' ')
line2 = Input[1].replace('\n', '').split(' ')
line3 = Input[2].replace('\n', '').split(' ')
num_of_points = line1[0]
num_of_edges = line1[1]
colors = line2
colors.append('goal')
rocket_loc = line3[0]
lucky_loc = line3[1]
edges = []
for line in Input:
        line_numbers = [num_of_edges for num_of_edges in line.split()]
        edges.append(line_numbers)
for edge in edges:
    edge[0] = int(edge[0]) - 1
    edge[1] = int(edge[1]) - 1
g = Graph(int(num_of_points), colors, int(rocket_loc), int(lucky_loc), edges)
output = []
algorithm()
for action in output:
    print(action[1], "   ", action[0] + 1)
