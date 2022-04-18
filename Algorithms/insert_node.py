from __dataset import Node, get_tree


def insert_node(root, value):
    if value < root.value:
        if not root.left:
            root.left = Node(value, None, None)
        else:
            insert_node(root.left, value)
    if value >= root.value:
        if not root.right:
            root.right = Node(value, None, None)
        else:
            insert_node(root.right, value)

    return root


t = get_tree()

res = insert_node(t, 10)
res.walk()
