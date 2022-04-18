from __dataset import get_tree


def find_max(root):
    if not root:
        return float('-inf')
    res = root.value
    lres = find_max(root.left)
    rres = find_max(root.right)
    if lres > res:
        res = lres
    if rres > res:
        res = rres
    return res


t = get_tree()
r = find_max(t)
print(r)
