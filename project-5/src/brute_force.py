# Politechnika Poznańska
# Konrad Ceglarski

from utils import Item

def ab(n, c, items, show=False):
    backpack_cost = 0
    backpack_items = []
    solutions = 2**n

    for ps in range(1, solutions): # ps - possible solution
        state = f"{bin(ps)[2:]:0>{n}}" # state of the backpack for current ps
        backpack = []
        bc = 0
        bw = 0
        correct = True
        # analyze possible state
        for idx, bit in enumerate(state[::-1]):
            if bit != "1": continue
            item = items[idx]
            backpack.append(item.id)
            bc += item.price
            bw += item.weight
            if bw > c:
                correct = False
                break
        # update found solution if correct
        if correct and bc > backpack_cost:
            backpack_cost = bc
            backpack_items = backpack

        if show:
            print(f"{state} - plecak: {backpack}, rozmiar: {bw}, dopuszczalne: {'+' if correct else '-'}, wartosc: {bc}")

    return (backpack_cost, backpack_items)
