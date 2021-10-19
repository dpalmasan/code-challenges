"""Implement different solutions for Good Nodes problem."""
from sols.binary_tree.binary_tree import TreeNode


def good_nodes(self, root: TreeNode) -> int:
    """Count number of good nodes in a Binary Tree.

    :param root: [description]
    :type root: TreeNode
    :return: [description]
    :rtype: int
    """
    good_nodes = 1
    max_val = root.val
    stack = [(root, max_val)]
    while stack:
        node, max_val = stack.pop()
        if node.left:
            max_val_left = max_val
            if node.left.val >= max_val:
                good_nodes += 1
                max_val_left = node.left.val
            stack.append((node.left, max_val_left))

        if node.right:
            max_val_right = max_val
            if node.right.val >= max_val:
                good_nodes += 1
                max_val_right = node.right.val
            stack.append((node.right, max_val_right))

    return good_nodes


def good_nodes_recursive(self, root: TreeNode) -> int:
    """Count number of good nodes in a Binary Tree.

    :param root: [description]
    :type root: TreeNode
    :return: [description]
    :rtype: int
    """
    # Inner function for recursive call.
    def _visit_count(node: TreeNode, max_seen: int) -> int:
        if node is None:
            return 0
        cnt = 1 if node.val >= max_seen else 0
        return (
            cnt
            + _visit_count(node.left, max(max_seen, node.val))
            + _visit_count(node.right, max(max_seen, node.val))
        )

    return _visit_count(root, root.val)
