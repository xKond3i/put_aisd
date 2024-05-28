# Politechnika Poznańska
# Konrad Ceglarski

from utils import Item

def ad(n, c, items, show=False):
    V = [] # cost matrix - maicerz kosztów
    rows = n+1
    cols = c+1
    V = [[0] * cols for _ in range(rows)] # fill cost matrix with 0s

    for i in range(1, rows):     # skip first row (it's always filled with 0s)
        for j in range(1, cols): # skip first column
            item = items[i-1]
            wi = item.weight
            pi = item.price
            x0 = V[i-1][j]
            if wi > j:
                V[i][j] = x0
            elif wi <= j: # else
                x1 = V[i-1][j-wi]+pi
                V[i][j] = max([x0, x1])

    # display cost matrix
    if show:
        print("macierz kosztow:")
        for row in V: print(row)

    # find max cost
    backpack_cost = V[rows-1][cols-1]

    # find items in the max cost result
    backpack_items = []
    j = cols-1
    for i in range(n, 0, -1):
        item = items[i-1]
        wi = item.weight
        if V[i][j] > V[i-1][j]:
            backpack_items.append(item.id)
            j = j-wi # element i-ty nie zabrany

    return (backpack_cost, backpack_items)
