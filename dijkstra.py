import math

from pqueue import PriorityQueue

from graph2 import Graph


def dijkstra(graph: Graph, source: object) -> tuple:
    """
    calcule les plus courts chemins entre les sommets d'un graphe à partir d'une origine source
    :param graph: le graphe
    :param source: le sommet d'origine
    :return: une tuple avec les distance stockés dans la variable dist
                et le tableau de routage
    """
    dist: dict = {source: 0}            # initialization
    prev: dict = {}                     # routing table
    Q: PriorityQueue = PriorityQueue()  # create vertex priority queue Q
    for v in graph.get_vertices():
        if v != source:
            dist[v] = math.inf          # unknown distance from source to v
        prev[v] = None                  # predecessor of v
        Q.add(v, priority=dist[v])

    #### à coder ###












    return dist, prev


def main():
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print("%s , %s, %3d" % (vid, wid, v.get_weight(w)))

    for v in g:
        print("g.vert_dict[%s]=%s" % (v.get_id(), g.vert_dict[v.get_id()]))


def test_dijkstra(graph):
    print(dijkstra(graph, "b"))


if __name__ == "__main__":
    g = Graph()

    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_vertex('f')

    g.add_edge('a', 'b', 7)
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)

    test_dijkstra(g)
