# proste cykliczne i acykliczne grafy nieskierowane o:
# * n wierzchołkach z przedziału <10; 25>
# * współczynniku nasycenia krawędziami s = {10, 20, 30, 40, 50, 60, 70, 80, 90}
# - graf nieskierowany o nasyceniu X ma X% z (n*(n-1))/2 krawędzi

# src: https://math.stackexchange.com/questions/16933/generating-a-eulerian-circuit-of-a-complete-graph-with-constant-memory

import math, random

def gen_hamil(n, x):
    e_max = math.floor((n*(n-1))/2) # max edges count
    e_cnt = math.floor((x/100)*e_max) # edges count

    if e_cnt < n: raise Exception("err: niewystarczajaca ilosc krawedzi")
    graph = [[0] * n for _ in range(n)] # adjacency matrix

    # generate hamilton cycle
    h_path = list(range(n))
    random.shuffle(h_path)
    for i in range(n):
        u = h_path[i]
        v = h_path[(i+1) % n]
        graph[u][v] = 1
        graph[v][u] = 1

    # add more edges (fill the graph to get the saturation of x)
    edges_added = 0
    i = 0 # in case while loop takes too long
    while edges_added + n < e_cnt and i < 2*e_max:
        i += 1
        u = random.randint(0, n-1)
        v = random.randint(0, n-1)
        if u != v and graph[u][v] == 0:
            graph[u][v] = 1
            graph[v][u] = 1
            edges_added += 1

    # print(f"hamil: nasycenie grafu: {(edges_added+n)/e_max * 100}%")

    return graph

def gen_euler(n, x):
    e_max = math.floor((n*(n-1))/2) # max edges count
    e_cnt = math.floor((x/100)*e_max) # edges count

    graph = [[0] * n for _ in range(n)] # adjacency matrix
    deg = [0] * n # we could try to generate it uniformly (full random is just too chaotic as shown down below)

    # ! UZGODNIONY Z GRUPA LABORATORYJNA *NIEDOKLADNY* GENERATOR
    # generate euler cycle
    vstart = random.randint(0, n-1) # it has to end there too!
    estart = vstart # edge start
    e = 0 # number of edges
    i = 0 # in case while loop takes too long
    while i < e_cnt - x//10 or graph[vstart][estart] == 1 or estart == vstart:
        i += 1
        eend = random.randint(0, n-1) # edge end
        # check if edge can be added
        if(i > n**3/2): return Exception("err: losowowanie krawedzi doprowadzilo do bledu")
        if estart == eend or graph[estart][eend] == 1 or deg[eend] >= n-3 + (n % 2): continue
        # add edge
        graph[estart][eend] = 1
        graph[eend][estart] = 1
        deg[estart] += 1
        deg[eend] += 1
        e += 1
        estart = eend # new start is the old end (building continous path)

    # finally connect the last vertex on the path with the first one (finish cycle)
    graph[vstart][estart] = 1
    graph[estart][vstart] = 1

    # bit of a cheat
    deg[vstart] = 1
    deg[estart] = 1

    # print(f"euler: nasycenie grafu: {e/e_max * 100}%")

    return graph
