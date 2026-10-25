class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # 1. Build the Trie
        root = TrieNode()

        for word in words:
            current = root

            for char in word:
                if char not in current.children:
                    current.children[char] = TrieNode()

                current = current.children[char]

            current.word = word

        rows = len(board)
        cols = len(board[0])

        result = []

        # 2. DFS on the board
        def dfs(row, col, node):

            # out of bounds
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return

            char = board[row][col]

            # already visited
            if char == "#":
                return

            # this letter is not useful for any word
            if char not in node.children:
                return

            next_node = node.children[char]

            # found a complete word
            if next_node.word is not None:
                result.append(next_node.word)

                # stop duplicate adding
                next_node.word = None

            # mark visited
            board[row][col] = "#"

            # go 4 directions
            dfs(row + 1, col, next_node)
            dfs(row - 1, col, next_node)
            dfs(row, col + 1, next_node)
            dfs(row, col - 1, next_node)

            # backtrack
            board[row][col] = char

        # 3. Start DFS from every cell
        for row in range(rows):
            for col in range(cols):
                dfs(row, col, root)

        return result