"""Binary tree utilities."""
from typing import Optional, Tuple


class TreeNode:
    """Class to represent a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        """Constructor."""
        self.val = val
        self.left = left
        self.right = right


def paren_notation_to_binary_tree(
    tree: Optional[Tuple[int, Optional[Tuple], Optional[Tuple]]]
) -> Optional[TreeNode]:
    """Convert from parentheses notation to binary tree.

    For example, the following binary tree:

    .. code-block:: console

        (3) -- (9)
            |
            -- (20) -- (15)
                    |
                    -- (7)

    Can be represented as:
    ``(3, (9, None, None), (20, (15, None, None), (7, None, None)))``
    in parentheses notation. This function takes a tuple defining the tree
    and converts it into a binary tree, returning the ``TreeNode`` root.

    :param tree: Parenthesis notation of the tree
    :type tree: Optional[Tuple[int, Optional[Tuple], Optional[Tuple]]]
    :return: Root of the resulting tree
    :rtype: Optional[TreeNode]
    """
    # Inner recursive furnction to build the tree.
    def _build_tree(node: TreeNode, tree: Tuple):
        left = tree[1]
        right = tree[2]
        if left is not None:
            node.left = TreeNode(left[0])
            _build_tree(node.left, left)

        if right is not None:
            node.right = TreeNode(right[0])
            _build_tree(node.right, right)

    if tree is None:
        return None
    root = TreeNode(tree[0])
    _build_tree(root, tree)
    return root


def traverse_tree(root: Optional[TreeNode]):
    """Traverse binary tree.

    :param root: Root of the binary tree.
    :type root: Optional[TreeNode]
    """
    if root is not None:
        print(root.val)
        traverse_tree(root.left)
        traverse_tree(root.right)


# Test client
if __name__ == "__main__":
    tree = (3, (9, None, None), (20, (15, None, None), (7, None, None)))
    root = paren_notation_to_binary_tree(tree)
    traverse_tree(root)
