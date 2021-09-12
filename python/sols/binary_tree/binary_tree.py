"""Binary tree utilities."""
from  typing import Optional, Tuple, Union

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def paren_notation_to_binary_tree(tree: Optional[Tuple[int, Optional[Tuple], Optional[Tuple]]]) -> Optional[TreeNode]:
    def build_tree(node: TreeNode, tree: Optional[Tuple[int, Optional[Tuple], Optional[Tuple]]]) -> Optional[TreeNode]:
        left = tree[1]
        right = tree[2]
        if left is not None:
            node.left = TreeNode(left[0])
            build_tree(node.left, left)

        if right is not None:
            node.right = TreeNode(right[0])
            build_tree(node.right, right)

    root = TreeNode(tree[0])
    build_tree(root, tree)
    return root


def traverse_tree(root: Optional[TreeNode]):
    if root is not None:
        print(root.val)
        traverse_tree(root.left)
        traverse_tree(root.right)


# Test client
if __name__ == "__main__":
    tree = (3, (9, None, None), (20, (15, None, None), (7, None, None)))
    root = paren_notation_to_binary_tree(tree)
    traverse_tree(root)