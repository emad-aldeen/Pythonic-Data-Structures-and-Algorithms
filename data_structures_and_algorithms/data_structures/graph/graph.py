from data_structures_and_algorithms.data_structures.graph.queue import Queue, Node

class Graph:
    '''
    one of the famouses data structures the graph:
        * [method] - add_node: adds a new vertex to the graph, returns the added vertex
        * [method] - add_edge: adds new edge between two virtices, takes in two verticies, has ability to add weight
        * [method] - get_neighbors: returns a collection of vertices (with weights) connected to a vertex, takes in a vertex
        * [method] - get_nodes: returns the value from a given vertex
        * [method] - size: returns number of vertices in Graph; integer
        * [method] - breadth_first: traverses the graph starting from the given vertex, returns a list of nodes visited during traversal
    '''
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, value):
        """
        Method to add new node to the graph:
            inp ---> node value you want to add
            out >>> the node that already added
        """
        node = Node(value)
        self.adjacency_list[node] = []
        return node

    def add_edge(self, start_node, end_node, weight=1):
        """
        Method to add an edge between tow nodes in the graph:
            inp ---> start node you want to start from
            inp2 ---> end node that want to reach
        """

        if start_node not in self.adjacency_list:
            raise KeyError('Start Node not in Graph')

        if end_node not in self.adjacency_list:
            raise KeyError('End Node not in Graph')

        adjacencies = self.adjacency_list[start_node]

        adjacencies.append((end_node,weight))

    def get_nodes(self):
        """
        Method to Returns all of the nodes in the graph as a collection:
            out >>> all nodes in the graph
        """
        return self.adjacency_list.keys()

    def get_neighbors(self, node):
        """
        Method to Returns a collection of nodes connected to the given node with the weights of their connections:
            inp ---> node you want connected
            out >>> all nodes connected to inputed node & there weights
        """
        return self.adjacency_list[node]

    def size(self):
        """
        Method to Returns the total number of nodes in the graph:
            out >>> integer representing the graph size
        """
        return len(self.adjacency_list)

    def breadth_first(self, start_node):
        """
        Method to do breadth-first traversal on a graph:
            inp ---> node you want to start traversing from
            out >>> list contain all graph nodes value
        """
        output = []
        q = Queue()
        q.enqueue(start_node)

        while len(q):
            cur = q.dequeue()
            output.append(cur)

            neighbors = self.adjacency_list[cur]
            for n in neighbors:
                if not n[0].visited:
                    n[0].visited = True
                q.enqueue(n[0])

        for node in self.adjacency_list:
            node.visited = False
        
        return output

    def add_nondirectional_edge(self, start_node, end_node, weight=0):
        '''
        methoud only used to add nondirectional edge(its only for testing perposes):
            inp ---> start node you want to add edge
            inp2 ---> end node you want to add edge betwin
        '''
        self.add_edge(start_node,  end_node, weight)
        self.add_edge( end_node, start_node, weight)


    def get_edge(self, v_lst):

        def contains_vertex(value, lst):
            for vertex in lst:
                if isinstance(vertex, tuple):
                    if vertex[0].value == value:
                        return vertex
                    continue
                if vertex.value == value:
                    return vertex
            return False, 0
        current = contains_vertex(v_lst[0], self.adjacency_list.keys())
        if isinstance(current, Node):
            tsum = 0
            for index in range(1, len(v_lst)):
                current, cost = contains_vertex(v_lst[index], self.get_neighbors(current))
                tsum += cost
                if not current:
                    return (False, '$0')
            return (True, f'${tsum}')
        return (False, '$0')

