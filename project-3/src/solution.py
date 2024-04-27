# Poznań University of Technology 🎓
# Algorithms and Data Structures
# Exercise #3 — Graph Algorithms
# Executed by @ Konrad Ceglarski

# ! In collaboration with @chatGPT [https://chat.openai.com/]

from lab import Node, create_am, create_sl
from impl import kahn_am, kahn_sl # @chatGPT

if __name__ == '__main__':
    # Labs Example!
    # n = 6 # przykład
    n = 6 # a)
    # n = 7 # b)

    # zróbmy listę wierzchołków
    nodes: list['Node'] = [Node(i) for i in range(n)]

    # zróbmy dowiązania (łączenie węzłów) - max
    m = n*(n-1)
    # m = 6 # z treści przykładu
    
    # for i in range(m):
    example = ['0, 3','2, 1','2, 3','2, 4','4, 0','4, 3'] # Labs Example!
    zestaw_a = ['1, 5', '2, 1', '2, 3', '2, 5', '3, 1', '3, 4', '5, 4'] # a) 7 łuków, 6 węzłów
    zestaw_b = ['0, 5', '0, 6', '1, 2', '3, 1', '3, 2', '4, 2', '5, 2', '5, 3', '5, 4', '6, 1', '6, 3'] # b) 11 łuków, 7 węzłów
    for polaczenie in zestaw_a:
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
