
# TODO
# Use difference_update for O(1) when removing vertices from an undirected graph.
# https://python-reference.readthedocs.io/en/latest/docs/sets/difference_update.html
#
# Modify add_vertex and add_edge to support all iterable objects
#
# Take a note of this example to edit error messages
# return 'Color(%s, %s, %s)' % (self.red, self.green, self.blue)

class Graph(object):
    """Summary of a class here.

    Long description here.

    Attributes:
        vertices: A set containing vertices of a graph
        edges: A set containing edges of a graph as tuples of length 2
        directed: A boolean indicating if a graph is directed
        adj_l: A dict containing an adjacency list

    """

    # A Graph type object
    def __init__(self, vertices, edges, directed=False, weighted=False):
        """Initializes a graph"""

        self.vertices = set()
        self.edges = set()
        self.directed = directed
        self.weighted = weighted
        self.adj_l = {}  # adjacency list

        self.add_vertex(vertices)
        self.add_edge(edges)


    def __str__(self):
        """Return a string representing a graph in a form of a set of vertices and a set of edges"""
        return '\n'.join([str(self.vertices), str(self.edges)])

    def __eq__(self, other_graph):
        """Return True if graphs have same vertices and edges"""
        if not isinstance(other_graph, Graph):
            return False
        return self.vertices == other_graph.vertices and self.edges == other_graph.edges


    def add_vertex(self, vertices):
        """Adds vertices to the graph.

        Args:
            vertices: set or a single variable containing vertices. # fix

        Raises:
            TypeError: if vertices is of incorrect type
            NameError: if vertex is already belongs to the graph. # fix

        """
        # IMPORTANT: add TypeError for vertices of incorrect type
        if isinstance(vertices, set):
            for x in vertices:
                if x in self.vertices:
                    raise NameError("vertex already belongs belongs to a graph")  # fix err msg add v name to msg
                self.vertices.add(x)
        else:
            # Try using try/excepts statement to catch TypeError
            if vertices in self.vertices:
                    raise NameError("vertex already belongs belongs to a graph")  # fix err msg add v name to msg
            self.vertices.add(vertices)

    # Test this
    def remove_vertex(self, vertices):
        """Removes vertices from the graph.

        Args:
            vertices: set or a single variable containing vertices.  # fix
        """
        '''
        # Old implementation remove in the next merge
        # Case for a set
        if isinstance(vertices, set):
            for x in vertices:
                if x in self.vertices:
                    # Fast implementation for undirected graphs
                    if not self.directed:
                        for y in self.adj_l[x]:
                            self.adj_l[y].differnce_update(x)
                    else:
                        for y in self.vertices:
                            self.adj_l[y].difference_update(x)
                    del self.adj_l[x]
        # Case for a single variable
        else:
            x = vertices
            if x in self.vertices:
                # Fast implementation for undirected graphs
                if not self.directed:
                    for y in self.adj_l[x]:
                        self.adj_l[y].differnce_update(x)
                else:
                    for y in self.vertices:
                        self.adj_l[y].difference_update(x)
                del self.adj_l[x]
        # Combine both cases together
        # Redo this function, use iteration through self.edges, also update self.edges list
        '''
        if isinstance(vertices, set):
            for x in vertices:
                if x in self.vertecies:
                    for edge in self.edges:
                        if edge[1] == x:
                            self.edges.difference_update(edge)
                            self.adj_l[edge[0]].difference_update(x)
                        elif edge[0] == x:
                            self.edges.difference_update(edge)
                    del self.adj_l[x]
        else:
            x = vertices
            if x in self.vertecies:
                for edge in self.edges:
                    if edge[1] == x:
                        self.edges.difference_update(edge)
                        self.adj_l[edge[0]].difference_update(x)
                    elif edge[0] == x:
                            self.edges.difference_update(edge)
                del self.adj_l[x]



    def is_vertex(self, vertex):
        """Returns a boolean indicating if vertex belongs to the graph.

        Args:
            vertex: Vertex.

        Returns:
            A boolean indicating if vertex belongs to the graph.

        """
        return vertex in self.vertices
        # fix name func

    def add_edge(self, edges):
        """Adds edges to the graph

        Args:
            edges: a set of edges of a single variable.  # fix

        Raises:
            TypeError: if edges is of incorrect type  # fix
            NameError: if vertex does not belong to the graph  # fix

        """
        # Case for a set of edges
        if isinstance(edges, set):
            for edge in edges:
                # Consider combining two if statements together
                if not isinstance(edge, tuple):
                    raise TypeError("each edge must be a tuple")  # fix err msg
                if len(edge) != 2:
                    raise TypeError("each edge must be a tuple of length 2")  # fix err msg
                # Adding edges to self.adj_l and self.edges
                x, y = edge
                if x not in self.vertices:
                    raise NameError("x does nto belong to a graph")  # fix err msg
                if y not in self.vertices:
                    raise NameError("y does nto belong to a graph")  # fix err msg

                if x not in self.adj_l:
                    self.adj_l[x] = {y}
                else:
                    self.adj_l[x].add(y)
                self.edges.add((x, y))

                if not self.directed:
                    if y not in self.adj_l:
                        self.adj_l[y] = {x}
                    else:
                        self.adj_l[y].add(x)
                    self.edges.add((y, x))
        # Case for a single edge
        elif isinstance(edges, tuple):
            if len(edges) != 2:
                raise TypeError("edge must by a tuple of length 2")  # fix err msg
            x, y = edges
            if x not in self.vertices:
                raise NameError("x does not belong to a graph")  # fix err msg
            if y not in self.vertices:
                raise NameError("y does not belong to a graph")  # fix err msg
            if x not in self.adj_l:
                self.adj_l[x] = {y}
            else:
                self.adj_l[x].add(y)
            if not self.directed:
                if y not in self.adj_l:
                    self.adj_l[y] = {x}
                else:
                    self.adj_l[y].add(x)
        # Fix if/else statements here
        elif not isinstance(edges, tuple):
            raise TypeError("edge must be set or single variable")  # fix err msg
        # Combine both cases into one

    def remove_edge(self, edges):
        """Removes edges from a graph

        Args:
            edges: set or a single variable representing edges
        """
        if isinstance(edges, set):
            for edge in edges:
                if edge in self.edges:
                    self.edges.difference_update(edge)
                    x, y = edge
                    self.adj_l[x].difference_update(y)
                    if not self.directed:
                        self.adj_j[y].difference_update(x)
        else:
            edge = edges
            if edge in self.edges:
                self.edges.difference_update(edge)
                x, y = edge
                self.adj_l[x].difference_update(y)
                if not self.directed:
                    self.adj_j[y].difference_update(x)

    def is_edge(self, edge):
        """Returns a boolean indicating if edge belong to the graph.  # fix

        Returns:
            A boolean indicating if edge belong to the graph.

        Raises:
            TypeError: if edge is not a tuple fo length 2  # fix

        """

        if not isinstance(edge, tuple):
            raise TypeError("edge must a tuple")  # fix err msg
        if len(edge) != 2:
            raise TypeError("edge must be a tuple of length 2 ")  # fix err msg

        return edge in self.edges
        # fix name func
        # Is error checking nece?

    # Think about err checking, maybe a write a a very nice func that catches all these...
    # def check(params):...
    # params ex: edges = Trues, vertices = False, etc...

    def adjacent(self, x, y):
        """Returns a boolean indicating adjacency of vertices.

        Args:
            x: First vertex.
            y: Second vertex.

        Returns:
            A boolean indicating adjacency of vertices.

        Raises:
            NameError: vertex1 or vertex2 do not belong to the graph  # fix
        """

        if x not in self.vertices:
            raise NameError("x does not belong to the graph")  # fix err msg
        if y not in self.vertices:
            raise NameError("y does not belong to the graph")  # fix err msg

        return y in self.adj_l[x]

    def neighbours(self, x):
        """Returns a set of all vertices adjacent with x.

         Args:
             x: Vertex.

        Returns:
            A set of all vertices adjacent with x.

        Raises:
            NameError: if x does not belong to the graph

        """
        return self.adj_l[x]

    def order(self):
        """Returns the order of the graph.

        Returns:
            The order of the graph.
        """

        return len(self.vertices)

    def size(self):
        """Returns the size of the graph.

        Returns:
            Size of a graph as int
        """

        return len(self.edges)
        # Fix for directed and undirected graphs

    def degree(self, x):
        """Returns degree of the vertex in the graph

        Args:
            x: vertex

        Returns:
            Degree of the vertex in the graph.

        Raises:
            NameError: if x does not belong to the graph.  # fix
        """

        if x not in self.vertices:
            raise NameError("x does not belong to the graph")  # fix err msg

        return len(self.adj_l[x])


