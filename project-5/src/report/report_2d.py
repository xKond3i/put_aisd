# Wykonaj w skali logarytmicznej wykres:
# t=f(n) zależności czasu obliczeń t od liczby n przedmiotów, przy stałej pojemności plecaka b.
# Na wykresie przedstaw 3 krzywe (jedna krzywa dla każdego algorytmu).
# 
# Wykonaj dla każdego algorytmu wykres:
# t=f(b) zależności czasu obliczeń t od pojemności plecaka b, przy stałej liczbie przedmiotów n.

# Wykonaj dla każdego algorytmu wykres:
# t=f(n, b) zależności czasu obliczeń t od liczby n przedmiotów i pojemności plecaka b.
# 
# Podaj jaka jest złożoność obliczeniowa zaproponowanych algorytmów oraz do jakich klas złożoności obliczeniowej należy 0-1 problem plecakowy (wersja optymalizacyjna i decyzyjna).
# Przedstaw obserwacje związane z działaniem wszystkich algorytmów.
# Czy można ustalić w jakich przypadkach algorytm zachłanny nie daje rozwiązania optymalnego?

# * --- modules
from timeit import default_timer as timer # tool measuring time
from data_gen import gen_items # tool generating problem random data
import csv

# import parent modules
import os, sys 
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from dynamic import ad
from brute_force import ab

# * --- helper functions
avg = lambda l: sum(l)/len(l)

def get_measurement(callable):
    # measure times
    start = timer() # * time start
    callable()
    end = timer() # * time end
    return end - start

# * --- global variables
results = []
time_scale = 1000 # from ms -> s (x1000)
repeat_cnt = 5

scope = list(range(10, 26))
slen  = len(scope) 

if __name__ == "__main__":
    # * --- gather measurements
    for i, c in enumerate(scope):
        print(f"generating results for {c=}... [{i+1}/{slen}]")
        results.append([])
        results[i].append(c)
        for j, n in enumerate(scope):
            items = gen_items(n)
            results[i].append(get_measurement(lambda: ab(n, c, items)))

    # * --- save the results
    with open(f"ab t=f(n,b).csv", "w", newline="") as f:
        fw = csv.writer(f, delimiter=";")
        fw.writerow(["c/n"] + scope)
        fw.writerows(results)
