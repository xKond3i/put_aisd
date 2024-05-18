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

# * Definitions
avg = lambda lst: sum(lst) / len(lst)

# * Main Execution
if __name__ == '__main__':
    # k: int = 100_000 # how many test cases
    # n_axis: list[int] = list(range(10, k + 1, 5))
    n_axis: list[int] = [*list(range(10, 100, 5)), *list(range(100, 1000, 10)), *list(range(1000, 10_000, 100)), *list(range(10_000, 10_000+1, 500))]
    repeats = 3 # how many tries to repeat the tests
    times = []

    length = len(n_axis)
    for i, n in enumerate(n_axis):
        print(f'Generating results for n = {n}... [{i+1}/{length}] ({(i+1)/length*100:.2f}%)')

        for k in range(repeats):
            numbers: list[int] = random.sample(range(0, 100_000), n) # generate Random Numbers List
            numbers = sorted(numbers)
            tmp_times: list[float] = [] # to make it more consistent

            start = timer() # ! time start

            # Create Binary Search Tree
            idx: int = len(numbers)//2 # middle index
            root: BST.Node = BST.Node(numbers[idx]) # root stands for our BST
            for i, num in enumerate(numbers):
                if (i == idx): continue
                root.insert(num)
            
            # balance BST
            root = root.balance()

            end = timer() # ! time end
            period = end - start
            tmp_times.append(period * 1000)

        times.append(avg(tmp_times))

    # PLOT
    print('\nGenerating plots...')
    plt.plot(n_axis, times)
    plt.title('$t=f(n)$ równoważenie')
    plt.xlabel('n')
    plt.ylabel('t [ms]')
    plt.grid()
    plt.savefig('rownowazenie.png')
    plt.show()
