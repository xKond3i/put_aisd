# Poznań University of Technology 🎓
# Algorithms and Data Structures
# Exercise #2 — Complex Data Structures
# Executed by @ Konrad Ceglarski

# * Modules
# import tree as BST # Binary Search Tree
import tree_iterative as BST # Binary Search Tree
import random # to generate pseudo random numbers
from timeit import default_timer as timer # for measuring time
import matplotlib.pyplot as plt

# - Wykonaj 2 wykresy (jeden wykres dla każdej z operacji: tworzenie struktury, wyszukanie minimum) t=f(n) zależności czasu obliczeń t od liczby n elementów w drzewie. Na każdym wykresie przedstaw 2 krzywe – po jednej krzywej dla każdej struktury.
# - Wykonaj wykres t=f(n) zależności czasu równoważenia t od liczby n elementów w losowym drzewie BST.

# * Definitions
avg = lambda lst: sum(lst) / len(lst)

# * Main Execution
if __name__ == '__main__':
    # k: int = 100_000 # how many test cases
    # n_axis: list[int] = list(range(10, k + 1, 5))
    n_axis: list[int] = [*list(range(10, 100, 5)), *list(range(100, 1000, 10)), *list(range(1000, 10_000, 100)), *list(range(10_000, 10_000+1, 500))]
    repeats = 3 # how many tries to repeat the tests
    bst_creating_times: list[float] = []
    avl_creating_times: list[float] = []
    bst_searching_times: list[float] = []
    avl_searching_times: list[float] = []

    length = len(n_axis)
    for i, n in enumerate(n_axis):
        print(f'Generating results for n = {n}... [{i+1}/{length}] ({(i+1)/length*100:.2f}%)')
        
        # to make it more consistent
        tmp_bst_creating_times: list[float] = []
        tmp_avl_creating_times: list[float] = []
        tmp_bst_searching_times: list[float] = []
        tmp_avl_searching_times: list[float] = []

        for k in range(repeats):
            numbers: list[int] = list(range(n, 0, -1))

            # CREATING BST
            start = timer() # time start
            root: BST.Node = BST.Node(numbers[0])
            for num in numbers[1:]: root.insert(num)
            end = timer() # time end
            period = end - start
            tmp_bst_creating_times.append(period)

            # SEARCHING BST
            start = timer()
            root.find_min()
            end = timer()
            period = end - start
            tmp_bst_searching_times.append(period * 1000) # times 1000 to make it ms

            # CREATING AVL
            start = timer() # time start
            root = BST.Node(numbers[0])
            for num in numbers[1:]: root.insert(num)
            root = root.balance()
            end = timer() # time end
            period = end - start
            tmp_avl_creating_times.append(period)  

            # SEARCHING AVL
            start = timer()
            root.find_min()
            end = timer()
            period = end - start
            tmp_avl_searching_times.append(period * 1000) # times 1000 to make it ms
            
        bst_creating_times.append(avg(tmp_bst_creating_times))
        bst_searching_times.append(avg(tmp_bst_searching_times))
        avl_creating_times.append(avg(tmp_avl_creating_times))
        avl_searching_times.append(avg(tmp_avl_searching_times))

    # PLOT
    print('\nGenerating plots...')
    plt.plot(n_axis, bst_creating_times,
             n_axis, avl_creating_times)
    plt.title('$t=f(n)$ tworzenie struktury')
    plt.xlabel('n')
    plt.ylabel('t [s]')
    plt.legend(["BST", "AVL"], loc="lower right")
    plt.grid()
    plt.savefig('tworzenie struktury.png')
    plt.draw()

    plt.figure()
    plt.plot(n_axis, bst_searching_times,
             n_axis, avl_searching_times)
    plt.title('$t=f(n)$ wyszukanie minimum')
    plt.xlabel('n')
    plt.ylabel('t [ms]')
    plt.legend(["BST", "AVL"], loc="lower right")
    plt.grid()
    plt.savefig('wyszukanie minimum.png')
    plt.draw()

    plt.show()
