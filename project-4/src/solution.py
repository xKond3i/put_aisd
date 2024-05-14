# Politechnika Poznańska
# Konrad Ceglarski
# ! DISCLAIMER: as it is a lab class program there are little to none protections against invalid data [NOT PRODUCTION READY]

from utils import *
from euler import euler_cycle
from hamil import hamil_cycle

if __name__ == "__main__":
    # load graph as [v, e, edges] | none (couldn't load)
    graph = wczytaj_graf()
    if graph == None: exit() # exit if graph not loaded
    v, e, edges = graph

    # create adjacency matrix
    ms = stworz_ms(v, e, edges)
    print("macierz sasiedztwa wybranego grafu:")
    for row in ms: print(row)

    hc = hamil_cycle(ms)
    ec = euler_cycle(ms)
