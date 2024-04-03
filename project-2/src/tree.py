# Binary Search Tree

# // Typing
from __future__ import annotations
from typing import Optional

# * Modules
from addons import NOT_IMPLEMENTED, FT # FT = Formatting
import math

# TODO - zrobić klasę BST, żeby mieć zawsze dostęp do roota (pomocne w balansowaniu)

# * Definitions
class Node:
    '''Node used by Binary Search Tree'''
    INORDER = 'INORDER'
    PREORDER = 'PREORDER'
    POSTORDER = 'POSTORDER'

    def __init__(self, value: int) -> None:
        self.value:  int              = value
        self.left:   Optional['Node'] = None
        self.right:  Optional['Node'] = None

        self.parent: Optional['Node'] = None

    def height(self):
        if self.left is None and self.right is None:
            return 0
        h_left  = 0 if self.left is None else self.left.height()
        h_right = 0 if self.right is None else self.right.height()
        return 1 + max(h_left, h_right)

    def display(self, level: int = 0, indent: str = '') -> None:
        '''Some way of representing the BST'''
        down  = '   └──'
        up    = '   ┌──'
        blank = '      '
        if self.left is not None: self.left.display(level + 1, up)
        print(f'{blank * (level-1)}{indent}{FT.BOX} {self.value:>3} {FT.RESET}')
        if self.right is not None: self.right.display(level + 1, down)

    # insert(self, child: Node) -> None:
    def insert(self, value: int) -> None:
        '''Method to add children'''
        child: Node = Node(value)
        if (child.value < self.value):
            if self.left is not None:
                self.left.insert(value)
            else:
                child.parent = self
                self.left = child
        else: # child.value >= self.value
            if self.right is not None:
                self.right.insert(value)
            else:
                child.parent = self
                self.right = child

    # ! task doesn't require such a method
    def remove(self, value: int) -> None:
        raise NOT_IMPLEMENTED

    def travel(self, mode: str = INORDER, show: bool = False, newline: bool = True) -> list[int]:
        '''Selected traversal methods (PRE, IN, POST - ORDER)'''
        lst: list[int] = []
        match mode:
            case Node.PREORDER:
                lst.append(self.value)                                                        # V
                if show: print(self.value, end=' ')                                           # show
                if self.left is not None: lst = self.left.travel(mode, show, False)         # L
                if self.right is not None: lst.extend(self.right.travel(mode, show, False)) # R
            case Node.POSTORDER:
                if self.left is not None: lst = self.left.travel(mode, show, False)         # L
                if self.right is not None: lst.extend(self.right.travel(mode, show, False)) # R
                lst.append(self.value)                                                        # V
                if show: print(self.value, end=' ')                                           # show
            case Node.INORDER | _: # INORDER or default
                if self.left is not None: lst = self.left.travel(mode, show, False)         # L
                lst.append(self.value)                                                        # V
                if show: print(self.value, end=' ')                                           # show
                if self.right is not None: lst.extend(self.right.travel(mode, show, False)) # R
        if (show and newline): print()
        return lst

    def find_min(self, show: bool = False) -> int:
        '''Find minimum value (the most left node and it's value)'''
        if self.left is None: # minimum value found
            if show: print(self.value)
            return self.value
        if show: print(self.value, end=" -> ")
        return self.left.find_min(show)

    def find_max(self, show: bool = False) -> int:
        '''Find maximum value (the most right node and it's value)'''
        if self.right is None: # minimum value found
            if show: print(self.value)
            return self.value
        if show: print(self.value, end=" -> ")
        return self.right.find_max(show)

    def find(self, key: int) -> Optional['Node']:
        '''Find Node with given key value'''
        if key == self.value:
            return self
        elif key < self.value:
            if self.left is not None: return self.left.find(key)
        elif key > self.value:
            if self.right is not None: return self.right.find(key)
        return None

    # * Day-Stout-Warren Algorithm
    def rotate_left(self) -> Node:
        '''Method performing left rotation'''
        if self.right is None:
            return self
        pivot: Node = self.right
        subtree: Optional['Node'] = pivot.left
        pivot.left = self
        self.right = subtree

        # update parents
        if subtree: subtree.parent = self
        pivot.parent = self.parent
        self.parent = pivot

        return pivot

    def rotate_right(self) -> Node:
        '''Method performing right rotation'''
        if self.left is None:
            return self
        pivot: Node = self.left
        subtree: Optional['Node'] = pivot.right
        pivot.right = self
        self.left = subtree

        # update parents
        if subtree: subtree.parent = self
        pivot.parent = self.parent
        self.parent = pivot

        return pivot

    def find_new_root(self):
        current = self
        while current.parent is not None:
            current = current.parent
        return current

    def vineify(self) -> int:
        '''Reduces tree to vine'''
        parent:  Optional['Node'] = None
        current: Optional['Node'] = self
        n: int = 0
        while current is not None:
            while current.left is not None: # loop through every child on the left and rotate them
                current = current.rotate_right()
                if parent is not None: parent.right = current # update parent
            parent = current
            current = current.right # move to the next child on the right
            n += 1
        return n

    def balance(self) -> Node:
        '''Balances BST using Day-Stout-Warren algorithm'''

        n: int = self.vineify()
        level: int = math.ceil(math.log2(n)) - 1 # optimal tree height
        bottom: int = n - level                  # number of nodes at the bottom
        
        # print(level, bottom)
        # current.display() # <- vine

        self.find_new_root().compress(bottom)

        times: int = int(((1 << level) - 1) / 2)
        while(times > 0):
            self.find_new_root().compress(times)
            times = times // 2

        return self.find_new_root()

    def compress(self, times: int) -> Node:
        '''Rotate nodes x times'''
        root: Node = Node(0)
        parent: Optional['Node'] = None
        node: Optional['Node']   = self

        for i in range(times):
            if node is None: break # extra safety

            node = node.rotate_left()

            if parent is not None: parent.right = node # ensure parents and children are linked
            else: root = node

            parent = node
            node = node.right # go to the next sibling

        return root
