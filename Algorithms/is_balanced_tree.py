from __dataset import get_tree


def height(root):
    if not root:
        return 0
    return max(height(root.left), height(root.right)) + 1


def is_balanced_tree(root):
    if root is None:
        return True
    hl = height(root.left)
    hr = height(root.right)
    if abs(hl - hr) <= 1 and is_balanced_tree(root.left) and is_balanced_tree(root.right):
        return True
    return False


t = get_tree()
res = is_balanced_tree(t)
print(res)
