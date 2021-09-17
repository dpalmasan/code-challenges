from typing import List, Optional
from sols.binary_tree.binary_tree import TreeNode


def zigzag_level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """Traverse tree in zig-zag order.

    Returns a list where each element is a list of nodes in a given
    depth of the tree, in Zig-Zag order, starting from left to right
    and alternating.

    :param root: Root of the binary tree
    :type root: Optional[TreeNode]
    :return: A list of list of nodes in each depth.
    :rtype: List[List[int]]
    """
    if root is None:
        return []
    
    queue = []
    queue.append((root, 0))
    result = []
    left = True
    nodes_in_level = []
    curr_level = 0
    while queue:
        node, level = queue.pop()
        if level == curr_level:
            if not left:
                nodes_in_level.insert(0, node.val)
            else:
                nodes_in_level.append(node.val)
        else:
            left = not left
            result.append(nodes_in_level)
            nodes_in_level = [node.val]
            curr_level = level
        if node.left is not None:
            queue.insert(0, (node.left, level + 1))
        if node.right is not None:
            queue.insert(0, (node.right, level + 1))
    if nodes_in_level:
        result.append(nodes_in_level)
    return result
