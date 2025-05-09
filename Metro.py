from friendsbalt.acs import MinPQ

class Graph():
    adjList = []
    edgeList = []
    edgeWeights = [] # in minutes
    """
    Graph class represents an undirected graph using an adjacency list.
    Attributes:
        vertex_count (int): The number of vertices in the graph.
        edge_count (int): The number of edges in the graph.
        adjacency_list (dict): A dictionary where keys are vertex indices and values are lists of adjacent vertices.
    Methods:
        __init__(v):
            Initializes a graph with a specified number of vertices and no edges.
        add_edge(u, v):
            Adds an undirected edge between vertices `u` and `v`.
            Raises:
                ValueError: If either `u` or `v` is out of bounds.
        E:
            Returns the number of edges in the graph.
        V:
            Returns the number of vertices in the graph.
        adjacent(u):
            Returns a list of vertices adjacent to vertex `u`.
            If `u` has no adjacent vertices, returns an empty list.
        __str__():
            Returns a string representation of the graph, including the number of vertices and edges.
        from_input_string(input_string):
            Creates a Graph instance from an input string.
            The input string should contain the number of vertices on the first line,
            followed by lines of edges in the format "u v", where `u` and `v` are vertex indices.
        """
    def __init__(self, v: int):
        self.vertex_count = v
        self.edge_count = 0
        self.adjacency_list = {}

    def add_edge(self, u: int, v: int, w: float):
        """
        Adds an edge between two vertices in the graph.
        This method updates the adjacency list to include the edge between
        the vertices `u` and `v`. If the vertices do not exist in the adjacency
        list, they are added. The graph is treated as undirected, so the edge
        is added in both directions. The edge count is incremented accordingly.
        Args:
            u (int): The first vertex of the edge.
            v (int): The second vertex of the edge.
        Raises:
            ValueError: If either `u` or `v` is out of bounds of the graph's
                        vertex count.
        """
        if v >= self.vertex_count or u >= self.vertex_count:
            raise ValueError("Vertex out of bounds.")
        
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []
        self.adjacency_list[u].append(edgeWeighted(v,w)) # append the object (edgeWeighted class) instead
        self.adjacency_list[v].append(edgeWeighted(u,w))  # comment this if you need it to be a digraph
        
        self.edge_count += 1

    @property
    def E(self):
        """
        int: The number of edges in the graph.
        """
        return self.edge_count
    
    @property
    def V(self):
        return self.vertex_count

    def adjacent(self, u):
        """
        Retrieve the list of nodes adjacent to a given node.

        Args:
            u: The node for which to find adjacent nodes.

        Returns:
            A list of nodes that are adjacent to the given node `u`.
            If the node `u` is not present in the adjacency list, an empty list is returned.
        """
        return list(self.adjacency_list.get(u, []))
    
    def __str__(self):
        """
        Returns a string representation of the graph.
        The string contains the number of vertices and edges, followed by
        the adjacency list for each vertex.

        Returns:
            str: A string representation of the graph.
        """
        result = f"Graph with {self.vertex_count} vertices and {self.edge_count} edges:\n"
        for vertex, edges in self.adjacency_list.items():
            result += f"{vertex}: {edges}\n"
        return result.strip()
    
    def from_input_string(input_string: str) -> 'Graph':
        """
        Creates a Graph instance from an input string.

        Args:
            input_string (str): The input string containing the number of vertices
                                and the edges.

        Returns:
            Graph: A Graph instance created from the input string.
        """
        lines = input_string.strip().split('\n')
        v = int(lines[0])
        graph = Graph(v)
        for line in lines[1:]:
            u, v = map(int, line.split())
            graph.add_edge(u, v)
        return graph

class DFS:
    """
    Class to perform Depth First Search (DFS) on a graph.
    Attributes:
        graph (Graph): The graph on which DFS is performed.
        visited (set): A set to keep track of visited vertices.
    Methods:
        __init__(graph):
            Initializes the DFS with the given graph.
        dfs(start):
            Performs DFS starting from the given vertex `start`.
            Returns a list of vertices in the order they were visited.
    """
    def __init__(self, graph: Graph):
        self.graph = graph
        self.visited = set()

    def dfs(self, start: int) -> list:
        """
        Perform DFS starting from the given vertex.

        Args:
            start (int): The starting vertex for DFS.

        Returns:
            list: A list of vertices in the order they were visited.
        """
        # remember- cost to v + cost of edge(v, u) < cost to u
        
        queue = MinPQ()
        queue.insert(10000, start)
        result = []

        while queue.is_empty() != True:
            vertex = queue.del_min()
            if vertex not in self.visited:
                self.visited.add(vertex)
                result.append(vertex)
                
                #queue.extend(reversed(self.graph.adjacent(vertex)))

        return result

class edgeWeighted:
    """""
        Methods
        getWeight -> return edge weight

    """""
    def __init__(self,v: int, w: float):
        self.vertex = v
        self.weight = w

    def getWeight(self):
        return self.weight # finsihed?