"""Implement solution for search problems using Depth First Search."""
from typing import List, Optional, Tuple


class WordBoardState:
    """State for the Word Search problem."""

    def __init__(
        self,
        rows: int,
        cols: int,
        pos: Tuple[int, int],
        depth: int = 0,
        visited: Optional[List[bool]] = None,
    ):
        """Constructor."""
        self.rows = rows
        self.cols = cols
        self.pos = pos
        self.depth = depth
        if visited:
            self._visited = list(visited)
        else:
            self._visited = [False] * (self.rows * self.cols)
        self.visit(pos[0], pos[1])

    @property
    def visited(self) -> List[bool]:
        """Get visited cells."""
        return self._visited

    def visit(self, i: int, j: int):
        """Visit a cell in coordinates (i, j)."""
        idx = self.cols * i + j
        self._visited[idx] = True

    def _is_visited(self, i: int, j: int):
        idx = self.cols * i + j
        return self._visited[idx]

    def get_neighbors(self) -> List["WordBoardState"]:
        """Get neighbors from a given state."""
        output = []
        i, j = self.pos
        if i > 0 and not self._is_visited(i - 1, j):
            new_pos = (i - 1, j)
            neighbor = WordBoardState(
                self.rows, self.cols, new_pos, self.depth + 1, self.visited
            )
            neighbor.visit(new_pos[0], new_pos[1])
            output.append(neighbor)
        if j > 0 and not self._is_visited(i, j - 1):
            new_pos = (i, j - 1)
            neighbor = WordBoardState(
                self.rows, self.cols, new_pos, self.depth + 1, self.visited
            )
            neighbor.visit(new_pos[0], new_pos[1])
            output.append(neighbor)
        if i < self.rows - 1 and not self._is_visited(i + 1, j):
            new_pos = (i + 1, j)
            neighbor = WordBoardState(
                self.rows, self.cols, new_pos, self.depth + 1, self.visited
            )
            neighbor.visit(new_pos[0], new_pos[1])
            output.append(neighbor)
        if j < self.cols - 1 and not self._is_visited(i, j + 1):
            new_pos = (i, j + 1)
            neighbor = WordBoardState(
                self.rows, self.cols, new_pos, self.depth + 1, self.visited
            )
            neighbor.visit(new_pos[0], new_pos[1])
            output.append(neighbor)
        return output


class WordSearchProblem:
    """Iterative solution based on State search problem."""

    def exist(self, board: List[List[str]], word: str) -> bool:
        """Check if word exist on board.

        Given a board consisting on letters and a word, searches
        the word in the board, only moving through adjacent letters. A letter
        might be used just one time.

        :param board: A grid of letters
        :type board: List[List[str]]
        :param word: Word to be searched
        :type word: str
        :return: True if word is found, False otherwise
        :rtype: bool
        """
        charset = set([c for c in word])
        candidate_charset = set()
        for row in board:
            for char in row:
                if char in charset:
                    candidate_charset.add(char)
        if charset != candidate_charset:
            return False

        rows = len(board)
        cols = len(board[0])
        for i, row in enumerate(board):
            for j, char in enumerate(row):
                if char == word[0]:
                    node = WordBoardState(rows, cols, (i, j))
                    stack = [node]
                    while stack:
                        node = stack.pop()
                        if node.depth == len(word) - 1:
                            return True
                        for child in node.get_neighbors():
                            if (
                                board[child.pos[0]][child.pos[1]]
                                == word[child.depth]
                            ):
                                stack.append(child)
        return False


class WordSearchRecursive:
    """Word search problem, recursive DFS solution."""

    def exist(self, board: List[List[str]], word: str) -> bool:
        """Check if word exist on board.

        Given a board consisting on letters and a word, searches
        the word in the board, only moving through adjacent letters. A letter
        might be used just one time.

        :param board: A grid of letters
        :type board: List[List[str]]
        :param word: Word to be searched
        :type word: str
        :return: True if word is found, False otherwise
        :rtype: bool
        """
        charset = set([c for c in word])
        candidate_charset = set()
        for row in board:
            for char in row:
                if char in charset:
                    candidate_charset.add(char)
        if charset != candidate_charset:
            return False

        for i, row in enumerate(board):
            for j, char in enumerate(row):
                if char == word[0]:
                    visited = [False] * (len(board) * len(board[0]))
                    result = self._dfs(board, word, visited, i, j, 0)
                    if result:
                        return True

        return False

    def _valid_position(self, board, i, j):
        return 0 <= i <= len(board) - 1 and 0 <= j <= len(board[0]) - 1

    def _is_valid_move(self, board, word, i, j, visited, depth) -> bool:
        cols = len(board[0])
        return (
            self._valid_position(board, i, j)
            and board[i][j] == word[depth + 1]
            and not visited[cols * i + j]
        )

    def _dfs(self, board, word, visited, i, j, depth) -> bool:
        if depth == len(word) - 1:
            return True
        cols = len(board[0])
        visited[cols * i + j] = True

        result = False
        if self._is_valid_move(board, word, i - 1, j, visited, depth):
            result = self._dfs(board, word, visited, i - 1, j, depth + 1)
            if result:
                return True
            visited[cols * (i - 1) + j] = False

        if self._is_valid_move(board, word, i + 1, j, visited, depth):
            result = self._dfs(board, word, visited, i + 1, j, depth + 1)
            if result:
                return True
            visited[cols * (i + 1) + j] = False

        if self._is_valid_move(board, word, i, j - 1, visited, depth):
            result = self._dfs(board, word, visited, i, j - 1, depth + 1)
            if result:
                return True
            visited[cols * i + j - 1] = False

        if self._is_valid_move(board, word, i, j + 1, visited, depth):
            result = self._dfs(board, word, visited, i, j + 1, depth + 1)
            if result:
                return True
            visited[cols * i + j + 1] = False

        return False


class MaxAreaOfIslandProblem:
    """Max area of island problem."""

    def max_area_of_island(self, grid: List[List[int]]) -> int:
        """Get the max area of an island given a grid of 0's and 1's.

        :param grid: Grid representing the map.
        :type grid: List[List[int]]
        :return: Area of the largest island.
        :rtype: int
        """
        max_area = 0
        visited = [False] * (len(grid) * len(grid[0]))
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                area = 0
                if not visited[len(grid[0]) * i + j] and cell == 1:
                    area = self.dfs(grid, i, j, visited, 0)
                max_area = max(max_area, area)
        return max_area

    def valid_move(
        self, grid: List[List[int]], i: int, j: int, visited: List[bool]
    ) -> bool:
        """Check whether a move is valid or not.

        For a move to be valid, the position (i, j) must be in
        the limits of the grid, and the cell at position (i, j)
        should not be marked as visited, and the cell should
        contain land.

        :return: True if move is valid, False otherwise.
        :rtype: bool
        """
        rows = len(grid)
        cols = len(grid[0])
        return (
            0 <= i < rows
            and 0 <= j < cols
            and grid[i][j] == 1
            and not visited[cols * i + j]
        )

    def dfs(
        self,
        grid: List[List[int]],
        i: int,
        j: int,
        visited: List[bool],
        area: int,
    ) -> int:
        """Depth-first-search step to compute area of an island.

        :param grid: Grid representing island.
        :type grid: List[List[int]]
        :param i: Cell's row
        :type i: int
        :param j: Cell's colum
        :type j: int
        :param visited: Visited cells
        :type visited: List[bool]
        :param area: Current area found
        :type area: int
        :return: Total area of visited cells.
        :rtype: int
        """
        visited[len(grid[0]) * i + j] = True
        area += 1

        if self.valid_move(grid, i - 1, j, visited):
            area = self.dfs(grid, i - 1, j, visited, area)

        if self.valid_move(grid, i + 1, j, visited):
            area = self.dfs(grid, i + 1, j, visited, area)

        if self.valid_move(grid, i, j - 1, visited):
            area = self.dfs(grid, i, j - 1, visited, area)

        if self.valid_move(grid, i, j + 1, visited):
            area = self.dfs(grid, i, j + 1, visited, area)

        return area


class FloodFillProblem:
    """Solution for the flood fill problem."""

    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:
        """Return modified image with the new color.

        :param image: Grid representing image
        :type image: List[List[int]]
        :param sr: Starting row
        :type sr: int
        :param sc: Starting column
        :type sc: int
        :param newColor: New color for ``(sr, sc)``
        :type newColor: int
        :return: Modified grid with propagated ``newColor``
        :rtype: List[List[int]]
        """
        color = image[sr][sc]
        self.dfs(image, sr, sc, color, newColor)
        return image

    def isNeighbor(
        self,
        image: List[List[int]],
        sr: int,
        sc: int,
        color: int,
        newColor: int,
    ) -> bool:
        """Check if a given coordinate is a neighbor.

        A neighboring cell is only a neighbor if it is the same color as
        the adjacent cell.

        :param image: Grid of colors
        :type image: List[List[int]]
        :param sr: Row position
        :type sr: int
        :param sc: Col position
        :type sc: int
        :param color: Old color
        :type color: int
        :param newColor: newColor
        :type newColor: int
        :return: True if it is a neighbor, False otherwise
        :rtype: bool
        """
        rows = len(image)
        cols = len(image[0])
        return (
            0 <= sr < rows
            and 0 <= sc < cols
            and image[sr][sc] == color
            and image[sr][sc] != newColor
        )

    def dfs(
        self,
        image: List[List[int]],
        sr: int,
        sc: int,
        color: int,
        newColor: int,
    ):
        """Depth first search to propagate newColor.

        :param image: Grid of colored cells
        :type image: List[List[int]]
        :param sr: Row position
        :type sr: int
        :param sc: Col position
        :type sc: int
        :param color: Current color
        :type color: int
        :param newColor: New color
        :type newColor: int
        """
        image[sr][sc] = newColor
        if self.isNeighbor(image, sr - 1, sc, color, newColor):
            self.dfs(image, sr - 1, sc, color, newColor)

        if self.isNeighbor(image, sr + 1, sc, color, newColor):
            self.dfs(image, sr + 1, sc, color, newColor)

        if self.isNeighbor(image, sr, sc - 1, color, newColor):
            self.dfs(image, sr, sc - 1, color, newColor)

        if self.isNeighbor(image, sr, sc + 1, color, newColor):
            self.dfs(image, sr, sc + 1, color, newColor)
