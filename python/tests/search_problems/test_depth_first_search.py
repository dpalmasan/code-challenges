"""Test cases for depth first search module."""
from sols.search_problems.depth_first_search import WordSearchRecursive


def test_sample_case():
    """Sample case 1."""
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    assert WordSearchRecursive().exist(board, word)


def test_sample_case_2():
    """Sample case 2."""
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "SEE"
    assert WordSearchRecursive().exist(board, word)


def test_sample_case_3():
    """Test repeated letters not allowed."""
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCB"
    assert not WordSearchRecursive().exist(board, word)


def test_impossible_search():
    """Test impossible search, string longer than total chars."""
    board = [["A", "A", "A"], ["A", "A", "A"]]
    word = "AAAAAAA"
    assert not WordSearchRecursive().exist(board, word)
