# Poznań University of Technology 🎓
# Algorithms and Data Structures
# Exercise #1 — Sorting Algorithms
# Executed by @ Konrad Ceglarski

# * Modules
from sort import merge, r_quick, it_quick
from addons import header, point, ask_for_mode, gen_ds_rnd, gen_ds_asc, gen_ds_desc, gen_ds_as, gen_ds_vs
from timeit import default_timer as timer

# * Main Execution
if __name__ == '__main__':
    header()

    out: list[int] = [] # out
    dataset: list[int] = ask_for_mode() # in
    # dataset = gen_ds_rnd(10) # in
    # dataset = gen_ds_asc(10) # in
    # dataset = gen_ds_desc(10) # in
    dataset = gen_ds_as(8) # in
    # dataset = gen_ds_vs(9) # in
    print(f'dataset [in]:', dataset)

    point('a')
    print('merge sort'.upper())
    start = timer()
    out, m  = merge.sort(dataset)
    end = timer()
    period = end - start
    print('out:', out)
    print(f'merges: {m}')
    print(f'sorting took: {period}s')

    point('b')
    print('recursive quick-sort'.upper())
    start = timer()
    out = r_quick.sort(dataset)
    end = timer()
    period = end - start
    print('out:', out)
    print(f'sorting took: {period}s')

    point('c')
    print('iterative quick-sort'.upper())
    start = timer()
    out = it_quick.sort(dataset)
    end = timer()
    period = end - start
    print('out:', out)
    print(f'sorting took: {period}s')
