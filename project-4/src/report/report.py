from timeit import default_timer as timer
import csv

import graph_gen as gg

# parent modules
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from euler import euler_cycle
from hamil import hamil_cycle

avg = lambda l: sum(l)/len(l)

if __name__ == "__main__":
    sat = [30, 50, 70] # saturation levels
    nov = list(range(10, 51, 2)) # number of verticies
    header = ["n"] + [f"{s}%" for s in sat]
    results_e = [] # euler results
    results_h = [] # hamilton results
    time_scale = 1000 # from ms -> s (x1000)
    repeat_cnt = 5

    results_cnt = len(sat) * len(nov)
    for i, n in enumerate(nov):
        re = [n]
        rh = [n]
        for j, s in enumerate(sat):
            print(f"\033[34m[{i*len(sat) + j+1}/{results_cnt}] badamy grafy dla n={n}, s={s}%\033[0m")
            # build the graphs
            tmpe = []
            tmph = []
            for k in range(repeat_cnt):
                eg = gg.gen_euler(n, s)
                hg = gg.gen_hamil(n, s)

                # measure times
                start = timer() # * time start
                euler_cycle(eg, display=False)
                end = timer() # * time end
                period = end - start

                tmpe.append(period * time_scale)

                start = timer() # * time start
                hamil_cycle(hg, display=False)
                end = timer() # * time end
                period = end - start

                tmph.append(period * time_scale)
            rh.append(avg(tmph))
            re.append(avg(tmpe))
            print(f"hamil: avg {avg(tmph)}ms")
            print(f"euler: avg {avg(tmpe)}ms")
        results_e.append(re)
        results_h.append(rh)

    # ! save the results
    with open("euler.csv", "w", newline="") as f:
        fw = csv.writer(f, delimiter=";")
        fw.writerow(header)
        fw.writerows(results_e)
    with open("hamil.csv", "w", newline="") as f:
        fw = csv.writer(f, delimiter=";")
        fw.writerow(header)
        fw.writerows(results_h)
