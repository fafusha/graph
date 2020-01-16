"""Description of the module


Reference:
https://en.wikipedia.org/wiki/Graph_(abstract_data_type)
http://svn.python.org/projects/python/trunk/Objects/setobject.c
https://wiki.python.org/moin/TimeComplexity
"""
# TODO
# Use difference_update for O(1) when removing vertices from an undirected graph.
# https://python-reference.readthedocs.io/en/latest/docs/sets/difference_update.html

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

        """
        # A new graph with given vertices and sets
        # Catching Type Errors Block
        if not isinstance(vertices, set):
            raise TypeError("vertices must be a set")  # fix err msg
        # A copy of this is in add_edges KEEP TRACK OF CHANGES {
        if not isinstance(edges, set):
            raise TypeError("edges must be a set")  # fix err msg
        for edge in edges:
            if not isinstance(edge, tuple):
                raise TypeError("edges must only contain tuples")  # fix err msg
            if len(edge) != 2:
                raise TypeError("edges must only contain tuples of length 2")  # fix err msg
        # }
        if not isinstance(directed, bool):
            raise TypeError("directed must be bool")  # fix err msg
        # end fo error block
        """

        self.vertices = set()
        self.edges = set()
        self.directed = directed
        self.adj_l = {}  # adjacency list

        self.add_vertices(vertices)
        self.add_edges(edges)
        # add a map of every element to its index, for simplicity?
        # tbh i think this is dumb...
        # figure out a way to do an ass map in a list
        # do this with adjacency lists
        # also add numpy on top of this
        # Add type checking for vertices edges and directed have to be set()
        # raise TypeError

    # fix
    # def __str__(self):
    #   # add a print statement do so its prints edges and vertices
    #  pass
    # fix
    # def __eq__(self, ):
        # ???
        # do equality based on vertices names and paths, look into this
        # if graphs have same vertices names and paths..., but keep in ind issue of indexing of whatever t
        # e name is, like i wanted to do a map or some shit'''
        # ???
    #   pass

    def add_vertices(self, vertices):
        """Adds vertices to the graph.

        Args:
            vertices: set or a single variable containing vertices.

        Raises:
            TypeError: if vertices is of incorrect type
            NameError: if vertex is already belongs to the graph. # fix

        """
        # IMPORTANT: add TypeError for vertices of incorrect type
        if isinstance(vertices, set):
            for v in vertices:
                if v in self.vertices:
                    raise NameError("vertex already belongs belongs to a graph")  # fix err msg add v name to msg
                self.vertices.add(v)
        else:
            if vertices in self.vertices:
                    raise NameError("vertex already belongs belongs to a graph")  # fix err msg add v name to msg
            self.vertices.add(vertices)
        # fix name func
        # a set() can be passed or a single variable
        # catch type errors
        # RAISE ERR IF VERTEX EXISTS?????

    def add_edges(self, edges):
        """Adds edges to the graph

        Args:
            edges: a set of edges of a single variable.  # fix

        Raises:
            TypeError: if edges is of incorrect type  # fix
            NameError: if vertex does not belong to the graph  # fix

        """
        # fix name func
        # a set() can be passed on or a single variable
        # add error message if sug path exists? (optional)
        # Code taken form__int__KEEPTR ACK OF CHANGES {
        if isinstance(edges, set):
            for edge in edges:
                # possibly combine two if statements together, review later
                # decided not to change because errors are different ???
                # Start of error block
                if not isinstance(edge, tuple):
                    raise TypeError("each edge must be a tuple")  # fix err msg
                if len(edge) != 2:
                    raise TypeError("each edge must have only beg and the end")  # fix err msg
                # end of error block

                # adding edges
                vertex1, vertex2 = edge
                if vertex1 not in self.vertices:
                    raise NameError("v1 does nto belong to a graph")  # fix err msg
                if vertex2 not in self.vertices:
                    raise NameError("v2 does nto belong to a graph")  # fix err msg

                if vertex1 not in self.adj_l:
                    self.adj_l[vertex1] = {vertex2}
                else:
                    self.adj_l[vertex1].add(vertex2)
                self.edges.add((vertex1, vertex2))
                if not self.directed:
                    if v2 not in self.adj_l:
                        self.adj_l[vertex2] = {vertex1}
                    else:
                        self.adj_l[vertex2].add(vertex1)
                    self.edges.add((vertex2, vertex1))
        # case for a single variable
        elif isinstance(edges, tuple):
            if len(edges) != 2:
                raise TypeError("each edge must have only beg and the end")  # fix err msg
            # adding edges
            vertex1, vertex2 = edges
            if vertex1 not in self.vertices:
                raise NameError("v1 does nto belong to a graph")  # fix err msg
            if vertex2 not in self.vertices:
                raise NameError("v2 does nto belong to a graph")  # fix err msg
            if vertex1 not in self.adj_l:
                self.adj_l[vertex1] = {vertex2}
            else:
                self.adj_l[vertex11].add(vertex2)
            if not self.directed:
                if vertex2 not in self.adj_l:
                    self.adj_l[vertex2] = {vertex1}
                else:
                    self.adj_l[vertex2].add(vertex1)
        # think about if maybe add else here
        elif not isinstance(edges, tuple):
            raise TypeError("edge must be set or single variable")  # fix err msg

    def is_vertex(self, vertex):
        """Returns a boolean indicating if vertex belongs to the graph.

        Args:
            vertex: Vertex.

        Returns:
            A boolean indicating if vertex belongs to the graph.

        """

        return vertex in self.vertices
        # fix name func

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

        # think about err checking, maybe a write a a very nice func that catches all these...
        # def check(params)...
        # params ex: edges = Trues, vertices = False, etc...

    def incident(self, vertex1, vertex2):
        """Returns a boolean indicating incidency of vertices.

        Args:
            vertex1: First vertex.
            vertex2: Second vertex.

        Returns:
            A boolean indicating incidency of vertices.

        Raises:
            NameError: vertex1 or vertex2 do not belong to the graph  # fix

        """

        if vertex1 not in self.vertices:
            raise NameError("vertex1 does not belong to the graph")  # fix err msg
        if vertex2 not in self.vertices:
            raise NameError("vertex2 does not belong to the graph")  # fix err msg

        return vertex2 in self.adj_l[vertex1]
        # possibly change name to incident?
        # one line solution may cause bugs for dir and undirected graphs look into it

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
        # size of a graph
        # add a fix for directed and undirected graphs

    def degree(self, vertex):
        """Returns degree of the vertex in the graph

        Args:
            vertex: vertex

        Returns:
            Degree of the vertex in the graph.

        Raises:
            NameError: if vertex does not belong to the graph.  # fix err msg
        """

        if vertex not in self.vertices:
            raise NameError("vertex does not belong to the graph")  # fix err msg

        return len(self.adj_l[vertex])
        # degree of a vertex
        # add error for vertex not in self.verticies

