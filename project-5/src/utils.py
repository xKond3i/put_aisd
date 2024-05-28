# Politechnika Poznańska
# Konrad Ceglarski

# ! DISCLAIMER: as it is a lab class program there are little to none protections against invalid data [NOT PRODUCTION READY]

# format danych:
# pierwszy wiersz to para liczb n, c (liczba przedmiotów, pojemność plecaka),
# kolejne wiersze to pary liczb w, p (rozmiar przedmiotu, wartość przedmiotu).
# spacja jest separatorem liczb w pojedynczej linii.

import itertools

class Item:
    _ids = itertools.count(1)

    """simple class that represents an item"""
    def __init__(self, weight, price, id=None):
        if id == None: self.id = next(Item._ids)
        else: self.id = id
        self.weight = weight
        self.price = price

    def __repr__(self):
        return f"<przedmiot id={self.id} rozmiar={self.weight}, wartosc={self.price}>"

def load_file():
    """func that loads items data from file"""
    n = c = 0 # number of items, backpack capacity
    items = []
    prefix = "items/"
    suffix = ".txt"
    fname = input(f"podaj nazwe pliku (wykluczajac prefix='{prefix}'; suffix='{suffix}'): ")
    try:
        with open(prefix+fname+suffix, "r") as f:
            for i, line in enumerate(f.readlines()):
                if i == 0:
                    n, c = [int(x) for x in line.split()] # number of items, backpack capacity
                else:
                    w, p = [int(x) for x in line.split()] # item weight, item price
                    items.append(Item(w, p, i))
    except:
        print("\033[31merr:\033[0m blad przy wczytywaniu pliku.")
        return None
    return [n, c, items]

def load_keyboard():
    """func that loads items data from keyboard"""
    items = []
    n, c = [int(x) for x in input("podaj ilosc przedmiotow i pojemnosc plecaka (n c): ").split()]
    for i in range(n):
        w, p = [int(x) for x in input(f"#{i+1} podaj rozmiar i wartosc przedmiotu (w p): ").split()]
        items.append(Item(w, p, i+1))
    return [n, c, items]

def load_items():
    """func that allows to choose how to load the data and then loads it that way"""
    choices = ["plik", "klawiatura"]
    print("metody wczytania przedmiotow: ")
    for i, m in enumerate(choices): print(f"#\033[35m{i+1}\033[0m - {m}")
    choice = input("wybierz metode wczytania przedmiotow: ")
    items = None
    match choice:
        case "1": items = load_file() # choices[0] -> "plik"
        case "2": items = load_keyboard() # choices[1] -> "klawiatura"
        case _: print("\033[31merr:\033[0m bledny wybor.")
    if items == None:
        return load_items()
    return items
