"""Test cases for depth first search module."""
from code_challenges.search_problems.depth_first_search import (
    WordSearchRecursive,
    MaxAreaOfIslandProblem,
    WordSearchProblem,
)


def test_word_search_test_sample_case():
    """Sample case 1."""
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    assert WordSearchRecursive().exist(board, word)


def test_word_search_test_sample_case_2():
    """Sample case 2."""
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "SEE"
    assert WordSearchRecursive().exist(board, word)


def test_word_search_test_sample_case_3():
    """Test repeated letters not allowed."""
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCB"
    assert not WordSearchRecursive().exist(board, word)


def test_word_search_test_impossible_search():
    """Test impossible search, string longer than total chars."""
    board = [["A", "A", "A"], ["A", "A", "A"]]
    word = "AAAAAAA"
    assert not WordSearchRecursive().exist(board, word)


def test_word_search_it_test_sample_case():
    """Sample case 1."""
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    assert WordSearchProblem().exist(board, word)


def test_word_search_it_test_sample_case_2():
    """Sample case 2."""
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "SEE"
    assert WordSearchProblem().exist(board, word)


def test_word_search_it_test_sample_case_3():
    """Test repeated letters not allowed."""
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCB"
    assert not WordSearchProblem().exist(board, word)


def test_word_search_it_test_impossible_search():
    """Test impossible search, string longer than total chars."""
    board = [["A", "A", "A"], ["A", "A", "A"]]
    word = "AAAAAAA"
    assert not WordSearchProblem().exist(board, word)


def test_area_of_island_valid_move():
    """Test valid move function."""
    mip = MaxAreaOfIslandProblem()
    grid = [[1, 0, 1], [0, 0, 0]]
    visited = [False] * 6
    assert not mip.valid_move(grid, -1, 0, visited)
    assert not mip.valid_move(grid, 3, 0, visited)
    assert not mip.valid_move(grid, 0, -1, visited)
    assert not mip.valid_move(grid, 0, 4, visited)
    assert mip.valid_move(grid, 0, 0, visited)
    assert not mip.valid_move(grid, 0, 1, visited)
    visited[0] = True
    assert not mip.valid_move(grid, 0, 0, visited)


def test_area_of_island():
    """Test max area of island."""
    mip = MaxAreaOfIslandProblem()
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]
    assert mip.max_area_of_island(grid) == 6
    assert mip.max_area_of_island([[0, 0, 0, 0, 0, 0, 0, 0]]) == 0
