"""Graph implementation using Adjency List"""

class Graph:
    """Graph class"""
    def __init__(self):
        self.vertex_dict = dict()

    def add_edge(self, vertex, destination, weight):
        """Add new edge."""
        # vertex existence check
        if vertex not in self.vertex_dict:
            self.vertex_dict[vertex] = set()
        # destination existence check
        if destination not in self.vertex_dict:
            self.vertex_dict[destination] = set()
        # add new edge to dictionary
        vertex_set = self.vertex_dict.get(vertex)
        vertex_set.add((destination, weight))

    def delete_edge(self, vertex, destination, weight) -> bool:
        # vertex existence check
        if vertex not in self.vertex_dict:
            return False

        vertex_set = self.vertex_dict.get(vertex)
        if (destination, weight) not in vertex_set:
            return False
        else:
            vertex_set.discard((destination, weight))

    def print_graph(self):
        """Display graph."""
        graph_string_list = []
        for vertex in self.vertex_dict.keys():
            vertex_string = f'vertex {vertex}:'
            for edge in self.vertex_dict.get(vertex):
                vertex_string += f' -> {edge}'
            print(f'{vertex_string}')


def main():
    temp = Graph()
    temp.add_edge('us', 'china', '500')
    temp.add_edge('us', 'russia', '100')
    temp.add_edge('us', 'spain', '250')
    temp.add_edge('spain', 'china', '50')
    temp.add_edge('russia', 'china', '200')
    temp.add_edge('china', 'us', '500')
    temp.add_edge('china', 'africa', '300')
    temp.add_edge('china', 'france', '280')
    temp.add_edge('us', 'mexico', '90')
    temp.add_edge('france', 'us', '178')
    print('\n\n')
    temp.print_graph()
    temp.delete_edge('us', 'china', '500')
    temp.delete_edge('russia', 'china', '200')
    temp.delete_edge('bolivia', 'us', '100')
    temp.delete_edge('us', 'bolivia', '100')
    print('\n\n')
    temp.print_graph()


if __name__ == '__main__':
    main()


"""
Example output from above

vertex us: -> ('spain', '250') -> ('china', '500') -> ('mexico', '90') -> ('russia', '100')
vertex china: -> ('us', '500') -> ('africa', '300') -> ('france', '280')
vertex russia: -> ('china', '200')
vertex spain: -> ('china', '50')
vertex africa:
vertex france: -> ('us', '178')
vertex mexico:



vertex us: -> ('spain', '250') -> ('mexico', '90') -> ('russia', '100')
vertex china: -> ('us', '500') -> ('africa', '300') -> ('france', '280')
vertex russia:
vertex spain: -> ('china', '50')
vertex africa:
vertex france: -> ('us', '178')
vertex mexico:
"""