"""Good nodes tests."""
from code_challenges.binary_tree import good_nodes
from code_challenges.binary_tree.binary_tree import (
    paren_notation_to_binary_tree,
)


def test_one_node():
    """Test one node case."""
    tree = (3, None, None)
    root = paren_notation_to_binary_tree(tree)
    assert good_nodes.good_nodes(root) == 1


def test_one_node_recursive():
    """Test when there is one node."""
    tree = (3, None, None)
    root = paren_notation_to_binary_tree(tree)
    assert good_nodes.good_nodes_recursive(root) == 1


def test_average_case():
    """Test case provided in the example."""
    tree = (
        3,
        (1, (3, None, None), None),
        (4, (1, None, None), (5, None, None)),
    )
    root = paren_notation_to_binary_tree(tree)
    assert good_nodes.good_nodes(root) == 4


def test_average_case_recursive():
    """Test case provided in the example for recursive approach."""
    tree = (
        3,
        (1, (3, None, None), None),
        (4, (1, None, None), (5, None, None)),
    )
    root = paren_notation_to_binary_tree(tree)
    assert good_nodes.good_nodes_recursive(root) == 4


def test_max_middle():
    """Test case with max in the middle."""
    tree = (2, None, (4, (10, None, None), (8, (4, None, None), None)))
    root = paren_notation_to_binary_tree(tree)
    assert good_nodes.good_nodes(root) == 4


def test_max_middle_recursive():
    """Test case with max in the middle for recursive approach."""
    tree = (2, None, (4, (10, None, None), (8, (4, None, None), None)))
    root = paren_notation_to_binary_tree(tree)
    assert good_nodes.good_nodes_recursive(root) == 4
