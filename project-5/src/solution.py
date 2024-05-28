# Politechnika Poznańska
# Konrad Ceglarski

from utils import *
from dynamic import ad
from brute_force import ab

if __name__ == "__main__":
    print("\033[35m"+"algorytmy i struktury danych\n".lower()+"\033[0m"+"problem plecakowy\n".lower())

    # load items as [n, c, items] | none (couldn't load)
    print("--- wczytywanie przedmiotow ---")
    data = load_items()
    if data == None: exit(-1)
    n, c, items = data

    # show items
    if n != len(items): exit(-1)
    print("\033[32msuc:\033[0m wczytano przedmioty")
    print(f"wczytane dane:\nn = {n}, c = {c},\nitems = {items}\n")

    # algorithms
    print("--- szukanie rozwiazan ---")
    print(f"#\033[35m1\033[0m - algorytm programowania dynamicznego")
    dynamic_solution = ad(n, c, items, show=True) # show -> shows cost matrix
    backpack_cost, backpack_items = dynamic_solution
    print(f"plecak: {backpack_items}")
    print(f"wartosc plecaka: {backpack_cost}")
    print(f"#\033[35m2\033[0m - algorytm brute force")
    brute_solution = ab(n, c, items, show=True) # show -> shows all possible solutions as binary numbers
    backpack_cost, backpack_items = brute_solution
    print(f"plecak: {backpack_items}")
    print(f"wartosc plecaka: {backpack_cost}")
