# znalezc najwieksza mozliwa wartosc dla plecaka o pojemonosci
# * Algorytm PD dla problemu plecakowego (https://ekursy.put.poznan.pl/pluginfile.php/825750/mod_resource/content/2/Szachniuk-ASD-temat-5-ws.pdf str 20)

items = [{"weight": 3, "price": 3},
         {"weight": 3, "price": 4}, 
         {"weight": 1, "price": 2}, 
         {"weight": 4, "price": 4},
         {"weight": 2, "price": 3},
         {"weight": 5, "price": 5}]

# items = [{"weight": 2, "price": 4},
#          {"weight": 1, "price": 3}, 
#          {"weight": 4, "price": 6}, 
#          {"weight": 4, "price": 8}]

n = len(items) # number of elements
c = 8 # capacity
V = [] # cost matrix - maicerz kosztów

rows = n+1
cols = c+1
V = [[0] * cols for _ in range(rows)] # fill cost matrix with 0s

for i in range(1, rows):     # skip first row (it's always filled with 0s)
    for j in range(1, cols): # skip first column
        item = items[i-1]
        wi = item["weight"]
        pi = item["price"]
        x0 = V[i-1][j]
        if   wi > j:
            V[i][j] = x0
        elif wi <= j: # else
            x1 = V[i-1][j-wi]+pi
            V[i][j] = max([x0, x1])

# display cost matrix
for row in V: print(row)

# find max cost
max_cost = V[rows-1][cols-1]
print(f"max possible cost: {max_cost}")

# find items in the max cost result
max_possible_items = []
j = cols-1
for i in range(n, 0, -1):
    item = items[i-1]
    wi = item["weight"]
    if V[i][j] > V[i-1][j]:
        max_possible_items.append(i)
        j = j-wi # element i-ty nie zabrany
print(f"items in backpack: {max_possible_items}")
