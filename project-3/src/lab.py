# in:
# n - liczba wierzchołków
# łuki (graf skierowany) -> m = n(n-1)

# out:
# lista wierzchołków (DFS)

# przykład
# n = m = 6
# łączenia: 0, 3    2, 1    2, 3    2, 4    4, 0    4, 3

from typing import Optional

class Node:
    def __init__(self, value: int,
                 wchodzace: Optional[list['Node']] = None,
                 wychodzace: Optional[list['Node']] = None):
        self.value = value
        self.wchodzace: list['Node'] = [] if wchodzace is None else wchodzace
        self.wychodzace: list['Node'] = [] if wychodzace is None else wychodzace

    def __repr__(self) -> str:
        return str(self.value)

def create_am(nodes: list['Node']) -> list[list[int]]: # adjacency matrix
    """creates [adjacency matrix] from given nodes (node objects have pointers to their inputs and outputs)"""
    am = []
    for y in range(len(nodes)):
        row_node = nodes[y]
        temp_row = []
        for x in range(len(nodes)):
            column_node = nodes[x]
            temp_row.append(1 if column_node in row_node.wychodzace else 0)
        am.append(temp_row)
    return am

def create_sl(nodes: list['Node']) -> dict[int, list[int]]: # successor list
    """creates [successor list] from given nodes (node objects have pointers to their inputs and outputs)"""
    sl: dict[int, list[int]] = {}
    for node in nodes:
        sl[node.value] = [nastepnik.value for nastepnik in node.wychodzace]
    return sl

def DFS(nodes: list['Node']):
    odwiedzone = []
    for node in nodes:
        if (node not in odwiedzone): odwiedzone.append(node)
        for child in node.wychodzace:
            if (child not in odwiedzone): odwiedzone.append(child)

    # Jeśli wszystkie następniki v są odwiedzone oraz odwiedzono
    # już wszystkie wierzchołki grafu to koniec.
    # 5. Jeśli wszystkie następniki v są odwiedzone ale nie
    # odwiedzono jeszcze wszystkich wierzchołków grafu zdejmij ze
    # stosu ostatni wierzchołek.
    # 6. Jeśli stos nie jest pusty to v  bieżący wierzchołek na
    # szczycie stosu, w przeciwnym razie v  dowolny
    # nieodwiedzony jeszcze wierzchołek grafu. Idź do pkt. 3.

#     # IMPL z wiki:
# #     function VisitNode(u):
# #        oznacz u jako odwiedzony
# #        dla każdego wierzchołka v na liście sąsiedztwa u:
# #            jeżeli v nieodwiedzony:
# #                VisitNode(v)
# #    function DepthFirstSearch(Graf G):
# #        dla każdego wierzchołka u z grafu G:
# #            oznacz u jako nieodwiedzony
# #        dla każdego wierzchołka u z grafu G:
# #            jeżeli u nieodwiedzony:
# #                VisitNode(u) 
    
#     return odwiedzone

if __name__ == "__main__":
    # n = int(input('podaj liczbę wierzchołków (n): '))
    n = 6 # przykład

    # zróbmy listę wierzchołków
    nodes: list['Node'] = [Node(i) for i in range(n)]

    # zróbmy dowiązania (łączenie węzłów)
    m = n*(n-1)
    m = 6 # z treści przykładu
    
    # for i in range(m):
    for polaczenie in ['0, 3','2, 1','2, 3','2, 4','4, 0','4, 3']:
        # od, do = [int(x) for x in input('podaj dowiazanie: ').split(',')]
        od, do = [int(x) for x in polaczenie.split(',')]
        nodes[do].wchodzace.append(nodes[od])
        nodes[od].wychodzace.append(nodes[do])

    print('macierz sąsiedztwa: ')
    ms = create_am(nodes)
    for row in ms:
        print(row)

    print('lista następników: ')
    ln = create_sl(nodes)
    print('{')
    for key, successors in ln.items():
        print(f'{key}: {successors}')
    print('}')

    print('\ndfs:')
    dfs = DFS(nodes)
    print(dfs)
