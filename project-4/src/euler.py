# Politechnika Poznańska
# Konrad Ceglarski
# * Algorytm z powracaniem (Fleury’ego) znajdujący cykl Eulera w grafie nieskierowanym (na macierzy sąsiedztwa)

# src:
# https://ekursy.put.poznan.pl/pluginfile.php/825746/mod_resource/content/2/Szachniuk-ASD-temat-4-ws.pdf - slide 23
# + https://www.geeksforgeeks.org/eulerian-path-and-circuit/
# + https://cp-algorithms.com/graph/euler_path.html

# PSEUDOKOD:
# DFS_Euler(v)
#   Dla każdego sąsiada(następnika) u wierzchołka v
#       usuń krawędź v-u w grafie (w obie strony)
#       DFS_Euler(u)
#   Odłóż v na stos wynikowy

def find_start(graph):
    # look for a first vertex with at least 1 neighbour
    for v, row in enumerate(graph):
        if 1 in row:
            return v
    return -1 # 404 such a vertex not found

def euler_cycle_exists(graph):
    # 1. parzystosc stopni wierzcholkow (SEARCH: find odd degree verticies)
    for v, row in enumerate(graph):
        if (row.count(1) - graph[v][v]) % 2 != 0:
            return False # even one odd-degree vertex disqualifies the graph from being euler (it might be semi-euler though)

    # 2. spojnosc (CHECK: graph coherence)
    vstart = find_start(graph)
    if vstart == -1:
        print("edge case: brak krawedzi.")
        return True
    visited = []
    return len(euler_dfs(graph, vstart, visited)) == len(graph)

def euler_dfs(graph, u, visited):
    # add zero-degree verticies to visited
    for v in range(len(graph)):
        if v not in visited and graph[v].count(1) == 0:
            visited.append(v)

    # quit if all verticies are 0-degree (no edges)
    if len(visited) == len(graph): return visited

    # else start with our chosen zero degree
    visited.append(u)

    # actual DFS
    for v in range(len(graph)):
        if v not in visited and graph[u][v] == 1:
            euler_dfs(graph, v, visited)

    return visited

def check_bridge(graph, u, v):
    # * BRIDGE (MOST) - an edge, that when missed makes the graph disjointed
    # remove an edge from the graph!
    graph[u][v] = 0
    graph[v][u] = 0
    visited = []
    if len(euler_dfs(graph, v, visited)) != len(graph):
        graph[u][v] = 1
        graph[v][u] = 1
        return False
    return True

def find_ec(graph, u, cycle):
    joined, bridge, x = False, False, -1
    for v in range(len(graph)):
        if graph[u][v] == 1:
            x = v
            joined = True
            bridge = check_bridge(graph, u, v)
            if bridge:
                find_ec(graph, v, cycle)
                break
    # if not a bridge, look for another edge
    if joined and not bridge and x != -1:
        find_ec(graph, x, cycle)
    cycle.append(u+1)
    return cycle

def euler_cycle(graph): # -> euler cycle | none
    if euler_cycle_exists(graph) <= 0:
        print("nie znaleziono cyklu eulera.")
        return None
    print("znaleziono cykl eulera:")
    cycle = []
    cycle = find_ec(graph, find_start(graph), cycle)
    for i, v in enumerate(cycle):
        if i == len(cycle)-1: print(v)
        else: print(v, end=", ")
    return cycle
