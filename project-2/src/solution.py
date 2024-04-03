# Poznań University of Technology 🎓
# Algorithms and Data Structures
# Exercise #2 — Complex Data Structures
# Executed by @ Konrad Ceglarski

# * Modules
import tree as BST # Binary Search Tree
from config import Config
from addons import get_arg, gen_numbers, header, point

# * Main Execution
if __name__ == '__main__':
    header() # print header

    CONFIG = Config() # instatiate Config
    n: int = get_arg(CONFIG) # get argument value for Random List Size
    numbers: list[int] = gen_numbers(n, CONFIG) # generate Random Numbers List
    numbers = sorted(numbers)

    # Create Binary Search Tree
    # idx: int = len(numbers)//2 # middle index
    # root: BST.Node = BST.Node(numbers[idx]) # root stands for our BST
    # for i, num in enumerate(numbers):
    #     if (i == idx): continue
    #     root.insert(num)
        
    # EXAMPLE TREE
    # root: BST.Node = BST.Node(4)
    # root.insert(2)
    # root.insert(6)
    # root.insert(1)
    # root.insert(3)
    # root.insert(5)
    # root.insert(7)

    numbers = list(range(7, 1, -1))
    idx: int = len(numbers) // 2 # middle index
    root: BST.Node = BST.Node(numbers[idx]) # root stands for our BST
    for i, num in enumerate(numbers):
        if (i == idx): continue
        root.insert(num)

    # # BST FROM THE BOARD
    # root: BST.Node = BST.Node(7)
    # # left branches
    # root.insert(2)
    # root.insert(1)
    # root.insert(6)
    # root.insert(4)
    # root.insert(3)
    # root.insert(5)
    # # right branches
    # root.insert(12)
    # root.insert(8)
    # root.insert(13)
    # root.insert(10) 
    # root.insert(9)
    # root.insert(11)

    print('\ngenerated binaray search tree:') # straight from the sorted list - not balanced
    root.display()
            
    # ! (a) wyszukanie w drzewie elementu o najmniejszej i największej wartości i
    # ! wypisanie ścieżki poszukiwania (od korzenia do elementu szukanego, element
    # ! szukany również wypisujemy),
    point('a')
    print('minimum search path: ', end='')
    tree_min: int = root.find_min(show = True)
    print(f'minimum value found: {tree_min}')
    print('maximum search path: ', end='')
    tree_max: int = root.find_max(show = True)
    print(f'maximum value found: {tree_max}')

    # ! (b) wypisanie wszystkich elementów drzewa w porządku malejącym
    # ! (wykorzystać do tego jedną z metod trawersowania drzewa binarnego),
    point('b')
    print('descending values: ', end='')
    inorder = root.travel(mode = BST.Node.INORDER)
    print(*list(reversed(inorder)))

    # ! (c) wypisanie w porządku pre-order podrzewa, ktorego korzeń (klucz) podaje
    # ! użytkownik oraz podanie wysokości tego poddrzewa,
    point('c')
    try:
        x = int(input('provide the key to find in the tree: '))
    except Exception as e:
        print('invalid value')
    else:
        found = root.find(x)
        if found is None:
            print(f'value `{x}` not found')
        else:
            print(f'height of subtree: {found.height()}')
            print('preorder of subtree: ', end='')
            found.travel(mode = BST.Node.PREORDER, show = True)

    # ! (d) równoważenie drzewa przez rotacje (algorytm DSW) lub przez usuwanie
    # ! korzenia (należy wybrać jedną metodę); elementy drzewa należy wypisać w
    # ! porządku pre-oder przed i po zrównoważeniu drzewa.
    # * wybrałem DSW
    point('d')
    print('tree preorder before balancing: ')
    root.travel(mode = BST.Node.PREORDER, show = True)
    # root.vineify()
    # root = root.find_new_root()
    # root.display()
    print('tree preorder after balancing (using DSW algorithm): ')
    root = root.balance()
    root.travel(mode = BST.Node.PREORDER, show = True)

    print('\nfinal tree representation:')
    root.display()
