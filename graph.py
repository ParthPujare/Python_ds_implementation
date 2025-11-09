class Graph:

    def __init__(self, directed = False):
        self.directed = directed
        self.adj_list = dict()

    def __repr__(self):
        graph_string = ""
        for node, neighbour in self.adj_list.items():
            graph_string += f"{node}->{neighbour}\n"
        return graph_string

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:
            raise ValueError("Node already exists")

    def remove_node(self, node):
        if node not in self.adj_list:
            raise ValueError("Node does not exist")
        
        for neighbour in self.adj_list.values():
            neighbour.discard(node)

        del self.adj_list[node]

    def add_edge(self, from_node, to_node, weight = None):
        if from_node not in self.adj_list:
            self.add_node(from_node)
        if to_node not in self.adj_list:
            self.add_node(to_node)
        if weight is None:
            self.adj_list[from_node].add(to_node)
            if not self.directed:
                self.adj_list[to_node].add(from_node)
        else:
            self.adj_list[from_node].add((to_node, weight))
            if not self.directed:
                self.adj_list[to_node].add((from_node, weight))

    def remove_edge(self, from_node, to_node):
        if from_node in self.adj_list:
            if to_node in self.adj_list[from_node]:
                self.adj_list[from_node].remove(to_node)
            else:
                raise ValueError("No connection between the nodes")
            if not self.directed:
                if from_node in self.adj_list[to_node]:
                    self.adj_list[to_node].remove(from_node)
        else:
            raise ValueError("Node does not exist in the graph")

    def get_neighbours(self, node):
        return self.adj_list.get(node, set())

    def has_node(self, node):
        return node in self.adj_list

    def has_edge(self, from_node, to_node):
        if from_node in self.adj_list:
            return to_node in self.adj_list[from_node]
        return False

    def get_nodes(self):
        return list(self.adj_list.keys())

    def get_edges(self):
        edges = []
        for from_node, neighbour in self.adj_list.items():
            for to_node in neighbour:
                edges.append((from_node, to_node))
        return edges

    def bfs(self, start):
        visited = set()
        queue = [start]
        order = []

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                order.append(node)
                neighbours = self.get_neighbours(node)
                for neighbour in sorted(neighbours):
                    if isinstance(neighbour, tuple):
                        neighbour = neighbour[0]
                    if neighbour not in visited:
                        queue.append(neighbour)

        return order

    def dfs(self, start):
        visited = set()
        stack = [start]
        order = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                order.append(node)
                neighbours = self.get_neighbours(node)
                for neighbour in sorted(neighbours, reverse=True):
                    if isinstance(neighbour, tuple):
                        neighbour = neighbour[0]
                    if neighbour not in visited:
                        stack.append(neighbour)

        return order

if __name__ == "__main__":
    g = Graph(directed=True)

    g.add_edge('A','B', 1)
    g.add_edge('A','C', 10)
    g.add_edge('B','C', 1)
    g.add_edge('B','D', 1)
    g.add_edge('D','C', 1)
    g.add_edge('A','E', 1)
    g.add_edge('E','F', 1)
    g.add_edge('G','F', 1)
    g.add_edge('F','H', 1)
    g.add_edge('H','I', 1)
    g.add_edge('I','G', 100)


    print(g)

    print("BFS from A:", g.bfs("A"))
    print("DFS from A:", g.dfs("A"))