"""Solution for spiral matrix."""
from typing import List


def traversal(output: List[List[int]], pos: int, n: int, start: int) -> int:
    """Traverse boundaries of an nxn matrix.

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
    start = traversal(output, pos, n, start)
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
