# Poznań University of Technology 🎓
# Algorithms and Data Structures
# Exercise #3 — Graph Algorithms
# Executed by @ Konrad Ceglarski

# ! In collaboration with @chatGPT [https://chat.openai.com/]

from lab import Node, create_am, create_sl
from impl import kahn_am, kahn_sl # @chatGPT

if __name__ == '__main__':
    # Labs Example!
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
        print(f' {key}: {successors}')
    print('}')

    print('topologiczne rozwinięcie (macierz sąsiedztwa): ')
    print(kahn_am(ms))
    print('topologiczne rozwinięcie (lista następników): ')
    print(kahn_sl(ln))
