class Graph:
    def __init__(self, n, colors, rocket, lucky, edges):
        self.nodes = []
        self.rocket = rocket - 1
        self.lucky = lucky - 1
        nodes_edges = []
        for i in range(n):
            nodes_edges.append([])
        for edge in edges:
            nodes_edges[edge[0]].append(edge)
        for i in range(n):
            self.nodes.append(Node(i, colors[i], 'n', nodes_edges[i]))
        self.nodes[rocket - 1].spec = 'r'
        self.nodes[lucky - 1].spec = 'l'

    def show(self):
        for node in self.nodes:
            node.show()

    def goal_check(self):
        if self.nodes[self.rocket].color == 'goal' or self.nodes[self.lucky].color == 'goal':
            return True
        return False

    def actions(self):
        actions = []
        r_actions = self.nodes[self.rocket].destination(self.nodes[self.rocket].color, self.nodes[self.lucky].color)
        l_actions = self.nodes[self.lucky].destination(self.nodes[self.rocket].color, self.nodes[self.lucky].color)
        for action in r_actions:
            actions.append([action, 'r'])
        for action in l_actions:
            actions.append([action, 'l'])
        return actions

    def do(self, action):
        if action[1] == 'r':
            self.rocket = action[0]
        else:
            self.lucky = action[0]


class Node:
    def __init__(self, number, color, spec, edges):
        self.id = number
        self.color = color
        self.spec = spec
        self.edges = edges

    def destination(self, corridor_color1, corridor_color2):
        dest = []
        for edge in self.edges:
            if edge[2] == corridor_color1 or edge[2] == corridor_color2:
                dest.append(edge[1])
        return dest

    def show(self):
        print("NODE NUMBER: ", self.id)
        print("WITH COLOR: ", self.color)
        print("WITH SPEC: ", self.spec)
        print("AND EDGES: ", self.edges)
        print("=========================")
