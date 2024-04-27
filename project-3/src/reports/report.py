from timeit import default_timer as timer
import random
import csv

from graph_gen import generate_directed_acyclic_graph as gen_graph

# parent modules

import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from lab import Node, create_am, create_sl
from impl import kahn_am, kahn_sl # @chatGPT

# ...

avg = lambda lst: sum(lst) / len(lst)

if __name__ == '__main__':
    n_axis = [*list(range(3, 10, 3)), *list(range(10, 30, 5)), *list(range(30, 100, 10)), *list(range(100, 300, 50)), *list(range(300, 501, 100))]
    repeats = 3
    times = {"ms": [], "ln": []}

    length = len(n_axis)
    for i, n in enumerate(n_axis):
        print(f'Generating results for n = {n}... [{i+1}/{length}] ({(i+1)/length*100:.2f}%)')

        for k in range(repeats):
            nodes: list['Node'] = [Node(i) for i in range(n)]
            m = random.randint(n, n*(n-1)//2)
            tmp_times = {"ms": [], "ln": []} # to make it more consistent

            # gen graph
            graph = gen_graph(n, m)
            for polaczenie in graph:
                # od, do = [int(x) for x in input('podaj dowiazanie: ').split(',')]
                od, do = [int(x) for x in polaczenie.split(',')]
                nodes[do].wchodzace.append(nodes[od])
                nodes[od].wychodzace.append(nodes[do])

            ms = create_am(nodes)
            ln = create_sl(nodes)

            start = timer() # ! time start
            kahn_am(ms)
            end = timer() # ! time end
            period = end - start
            tmp_times["ms"].append(period * 1000)

            start = timer() # ! time start
            kahn_sl(ln)
            end = timer() # ! time end
            period = end - start
            tmp_times["ln"].append(period * 1000)

        times["ms"].append(avg(tmp_times["ms"]))
        times["ln"].append(avg(tmp_times["ln"]))

    with open('result.csv', 'w', newline='') as f:
        fw = csv.writer(f, delimiter=',')
        fw.writerow(["n", "ms", "ln"]) # header
        for line_idx in range(length):
            fw.writerow([n_axis[line_idx], times["ms"][line_idx], times["ln"][line_idx]])
