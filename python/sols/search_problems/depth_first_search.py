"""Implement solution for search problems using Depth First Search."""
from typing import List


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
