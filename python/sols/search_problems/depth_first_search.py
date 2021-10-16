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
