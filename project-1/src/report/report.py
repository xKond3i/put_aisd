# Allow importing from parent
import sys
import os
cwd = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(cwd)
sys.path.append(parent)

# Increase Recursion Depth Limit
sys.setrecursionlimit(2500)

# * Modules
from sort import merge, r_quick, it_quick
from addons import gen_ds_rnd, gen_ds_asc, gen_ds_desc, gen_ds_as, gen_ds_vs
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import csv

# * Variables
ITERATIONS = 3
N_AXIS = list(range(100, 1000 + 1, 100))
ALGORITHMS = {
    'merge sort': merge.sort,
    'recursive quick sort': r_quick.sort,
    'iterative quick sort': it_quick.sort
}
DATA_TYPES = {
    'random (losowe)': gen_ds_rnd,
    'ascending (rosnące)': gen_ds_asc,
    'descending (malejące)': gen_ds_desc,
    'a-shaped (a-kształtne)': gen_ds_as,
    'v-shaped (v-kształtne)': gen_ds_vs
}

# * Definitions
def measure_time(func, args):
    start = timer()
    func(args)
    end = timer()
    return (end - start) * 1000 # times 1000 -> ms

# * Main Execution
if __name__ == '__main__':
    for algorithm_name, algorithm_func in ALGORITHMS.items():
        times: dict = {ds_name: [] for ds_name in DATA_TYPES.keys()}

        for n in N_AXIS:
            tmp_times = {ds_name: 0 for ds_name in DATA_TYPES.keys()}

            for ds_name, gen_func in DATA_TYPES.items():
                for _ in range(ITERATIONS):
                    ds = gen_func(n)
                    tmp_times[ds_name] += measure_time(algorithm_func, ds)

                times[ds_name].append(tmp_times[ds_name] / ITERATIONS)

        plt.figure()
        for ds_name, data_times in times.items():
            plt.plot(N_AXIS, data_times, label=ds_name)

        plt.title(f'$t=f(n)$ {algorithm_name.upper()}')
        plt.xlabel('n')
        plt.ylabel('t [ms]')
        plt.legend(loc='upper left')
        plt.grid()
        plt.savefig(f'{algorithm_name}.png')
        plt.draw()

        # Save data to CSV
        data_to_save = [['n'] + N_AXIS]
        for ds_name, data_times in times.items():
            data_to_save.append([ds_name] + data_times)
        with open(f'{algorithm_name}.csv', 'w', encoding='utf-8', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data_to_save)

    plt.show()
