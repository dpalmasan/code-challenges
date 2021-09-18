"""Solution for spiral matrix."""
from typing import List


def traversal(output: List[List[int]], pos: int, n: int, start: int) -> int:
    """Traverse boundaries of an nxn matrix ``O(4*n)``.

    :param output: Matrix to be filled
    :type output: List[List[int]]
    :param pos: Starting position (pos, pos)
    :type pos: int
    :param n: Size of the matrix to traverse
    :type n: int
    :param start: Starting value
    :type start: int
    :return: End value of the traversal
    :rtype: int
    """
    for i in range(pos, n):
        output[pos][i] = start
        start += 1

    for j in range(pos + 1, n):
        output[j][i] = start
        start += 1

    for i in range(n - 2, pos - 1, -1):
        output[j][i] = start
        start += 1

    for j in range(n - 2, pos, -1):
        output[j][i] = start
        start += 1

    return start


def optimized_traversal(output: List[List[int]], pos: int, n: int, start: int) -> int:
    """Traverse boundaries of an nxn matrix O(n).

    :param output: Matrix to be filled
    :type output: List[List[int]]
    :param pos: Starting position (pos, pos)
    :type pos: int
    :param n: Size of the matrix to traverse
    :type n: int
    :param start: Starting value
    :type start: int
    :return: End value of the traversal
    :rtype: int
    """
    offset = n - pos - 1
    top_left_corner = start
    top_right_corner = top_left_corner + offset
    bottom_right_corner = top_right_corner + offset
    bottom_left_corner = bottom_right_corner + offset
    output[pos][pos] = top_left_corner
    output[pos][n - 1] = top_right_corner
    output[n - 1][n - 1] = bottom_right_corner
    output[n - 1][pos] = bottom_left_corner
    for i in range(pos + 1, n - 1):
        top_left_corner += 1
        top_right_corner += 1
        bottom_right_corner += 1
        bottom_left_corner += 1
        output[pos][i] = top_left_corner
        output[i][n - 1] = top_right_corner
        output[n - 1][n - i + pos - 1] = bottom_right_corner
        output[n - i + pos - 1][pos] = bottom_left_corner

    return bottom_left_corner + 1


def recursive_traversal(output: List[List[int]], pos, n, start):
    """Write into the matrix in a recursive fashion.

    We have two base cases, either ``n`` is odd or even. When ``n``
    is even, we will at some point end up with a 2x2 matrix. Otherwise
    we will end up with an 1x1 matrix.

    For all the other cases, we start at the left corner and fill the
    elements of the boundatries accordingly up to ``n``.

    :param output: Matrix to be filled
    :type output: List[List[int]]
    :param pos: Starting position
    :type pos: int
    :param n: Problem size
    :type n: int
    :param start: Starting position (pos, pos)
    :type start: int
    """
    # Odd base case
    if n - pos == 1:
        output[pos][pos] = start
        return

    # Even base case
    if n - pos == 2:
        output[pos][pos] = start
        output[pos][pos + 1] = start + 1
        output[pos + 1][pos + 1] = start + 2
        output[pos + 1][pos] = start + 3
        return

    # Fill boundaries
    start = optimized_traversal(output, pos, n, start)
    recursive_traversal(output, pos + 1, n - 1, start)


def spiral(n: int) -> List[List[int]]:
    """Create an spiral square matrix.

    :param n: Dimension of the matrix
    :type n: int
    :return: Matrix of integers
    :rtype: List[List[int]]
    """
    if n <= 0:
        raise ValueError(f"n should be greater than 0, you provided: {n}")
    output = [[0]*n for _ in range(n)]
    recursive_traversal(output, 0, n, 1)
    return output



def invalid_position(output: List[List[int]], row: int, col: int) -> bool:
    """Check if position is valid, i.e. non out of limits and non visited.

    :param output: Matrix
    :type output: List[List[int]]
    :param row: Current row
    :type row: int
    :param col: Current col
    :type col: int
    :return: True if it is invalid, False otherwise
    :rtype: bool
    """
    n = len(output)
    return row < 0 or col < 0 or row >= n or col >= n or output[row][col] != 0


def iterative_spiral(n: int) -> List[List[int]]:
    """Create an spiral square matrix.

    :param n: Dimension of the matrix
    :type n: int
    :return: Matrix of integers
    :rtype: List[List[int]]
    """
    if n <= 0:
        raise ValueError(f"n should be greater than 0, you provided: {n}")

    dir_row = (0, 1, 0, -1)
    dir_col = (1, 0, -1, 0)
    cur_dir = 0
    val = 1
    row = 0
    col = 0
    limit = n*n
    output = [[0]*n for _ in range(n)]
    while val <= limit:
        output[row][col] = val
        row += dir_row[cur_dir]
        col += dir_col[cur_dir]
        if invalid_position(output, row, col):
            row -= dir_row[cur_dir]
            col -= dir_col[cur_dir]
            cur_dir = (cur_dir + 1) % 4
            row += dir_row[cur_dir]
            col += dir_col[cur_dir]
        val += 1
    return output
