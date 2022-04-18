from collections import namedtuple
from functools import total_ordering


# Node = namedtuple('Node', ['value', 'left', 'right'])

@total_ordering
# class Node(namedtuple('Node', ['value', 'left', 'right'])):
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    # post_order
    def walk(self):
        if self.left:
            self.left.walk()
        if self.right:
            self.right.walk()
        print(self.value)

    def __lt__(self, other):
        if self.value < other.value:
            return True
        return False

    def __eg__(self, other):
        res = self.value = other.value
        return res

    def __str__(self):
        return f'node {self.value}'


def get_tree():
    input = open('1.txt', 'r')
    n = int(input.readline().strip())
    arr = []
    for k in range(n):
        ind, value, left_ind, right_ind = input.readline().split()
        left_ind = int(left_ind) if left_ind != 'None' else None
        right_ind = int(right_ind) if right_ind != 'None' else None
        arr.append((int(ind), int(value), left_ind, right_ind))
    root = None
    nodes = {}
    for ind, value, left_ind, right_ind in arr[::-1]:
        left_child = nodes.get(left_ind)
        right_child = nodes.get(right_ind)
        root = Node(value, left_child, right_child)
        nodes[ind] = root

    return root

# checks
# t = get_tree()
# t.walk()
