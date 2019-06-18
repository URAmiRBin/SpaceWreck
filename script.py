import fileinput
import sys
from Graph import *

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
g.show()
