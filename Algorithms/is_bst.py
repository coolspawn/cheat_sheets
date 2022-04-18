# check if tree is BST

def is_bst(root):
    if not root or (root.left == None and root.right == None):
        return True
    if root.right == None:
        return root.left.value < root.value and is_bst(root.left)
    if root.left == None:
        return root.right.value > root.value and is_bst(root.right)
    if root.value <= root.left.value or root.value >= root.right.value:
        return False
    return is_bst(root.left) and is_bst(root.right)