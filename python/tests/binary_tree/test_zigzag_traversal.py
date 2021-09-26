"""Zig-zag traversal tests."""
from sols.binary_tree.zigzag_traversal import zigzag_level_order
from sols.binary_tree.binary_tree import paren_notation_to_binary_tree


def test_null_root():
    """Corner case where root is null."""
    assert zigzag_level_order(None) == []


def test_simple_case():
    """Test case provided in the example."""
    tree = (3, (9, None, None), (20, (15, None, None), (7, None, None)))
    root = paren_notation_to_binary_tree(tree)
    assert zigzag_level_order(root) == [[3], [20, 9], [15, 7]]
