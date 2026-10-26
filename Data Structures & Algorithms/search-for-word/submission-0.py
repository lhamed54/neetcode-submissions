class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # get the size of the board
        rows = len(board)
        cols = len(board[0])

        # this checks if we can find the word
        # starting from this row and column
        # i = which letter of the word we are looking for
        def backtrack(row, col, i):

            # we found every letter in the word
            if i == len(word):
                return True

            # we walked outside the board
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False

            # this board letter is not the letter we need
            if board[row][col] != word[i]:
                return False

            # remember the letter
            letter = board[row][col]

            # mark this square as used
            board[row][col] = "#"

            # try going down, up, right, or left
            found = (
                backtrack(row + 1, col, i + 1) or
                backtrack(row - 1, col, i + 1) or
                backtrack(row, col + 1, i + 1) or
                backtrack(row, col - 1, i + 1)
            )

            # put the letter back
            board[row][col] = letter

            return found

        # try starting the word from every square
        for row in range(rows):
            for col in range(cols):

                # 0 means start with the first letter of word
                if backtrack(row, col, 0):
                    return True

        # we tried every square and could not find the word
        return False