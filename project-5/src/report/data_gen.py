# Wygeneruj dane wejściowe dla problemu plecakowego:
# n-elementowy zbiór przedmiotów, każdemu z nich przyporządkuj rozmiar r(i) oraz wartość w(i).
# Parametry rozmiar i wartość przyjmują wartości ze zbioru liczb naturalnych.
# Każdy przedmiot jest unikatowy (ma inny identyfikator), ale w zbiorze może istnieć wiele przedmiotów o takim samym rozmiarze / wartości.
# Ustal pojemność plecaka b, do którego zapakujesz przedmioty ze zbioru.

import random as rnd

# import parent modules
import os, sys 
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import Item

def gen_items(n):
    items = []
    for i in range(n): items.append(Item(rnd.randint(1, n+1), rnd.randint(1, n+1)))
    return items
