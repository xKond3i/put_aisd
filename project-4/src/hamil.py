# Politechnika Poznańska
# Konrad Ceglarski
# * Algorytm z powracaniem (Robertsa-Floresa) znajdujący cykl Hamiltona w grafie nieskierowanym (na macierzy sąsiedztwa)

# src:
# https://ekursy.put.poznan.pl/pluginfile.php/825746/mod_resource/content/2/Szachniuk-ASD-temat-4-ws.pdf - slide 15
# + https://www.geeksforgeeks.org/hamiltonian-cycle/

def is_path_member_valid(graph, path, u, pos):
    if graph[path[pos-1]][u] == 0: # no connection with the last one on the path
        return False
    if u in path: # already in path
        return False
    return True # path is still valid :)

# it is pretty much bool Hamiltonian(int v) from the slide
def find_cycle(graph, path, pos):
    n = len(graph)
    # CHECK: does the last vertex connect with the first? YES: cycle found! NO: 404
    if pos == n:
        if graph[path[pos-1]][path[0]] == 1:
            return True
        return False

    # SEARCH: look for the next vertex to be a part of a path
    for v in range(1, n):
        if is_path_member_valid(graph, path, v, pos):
            path[pos] = v
            if find_cycle(graph, path, pos+1): # <- returning occurs here!
                return True
            path[pos] = None # <- clear if it doesn't lead to a solution

    return False

def hamil_cycle(graph, display=True):
    n = len(graph) # number of verticies
    path = [None for _ in range(n)]
    path[0] = 0 # start with the first vertex in the graph

    if not find_cycle(graph, path, 1):
        if display: print("nie znaleziono cyklu hamiltona.")
        return None

    if display:
        print("znaleziono cykl hamiltona:")
        for v in path: print((v+1), end=", ")
        print(path[0]+1)
    return path
