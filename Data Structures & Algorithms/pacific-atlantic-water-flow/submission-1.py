class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(row, col, visited, previous_height):

            if row < 0 or row >= rows or col < 0 or col >= cols:
                return

            if (row, col) in visited:
                return None

            if heights[row][col] < previous_height:
                return

            visited.add((row, col))
            current_height = heights[row][col]

            dfs(row + 1, col, visited, current_height)
            dfs(row - 1, col, visited, current_height)
            dfs(row, col - 1, visited, current_height)
            dfs(row, col + 1, visited, current_height) 

        for col in range(cols):

            dfs(0, col, pacific, heights[0][col])
            dfs(rows - 1, col, atlantic, heights[rows - 1][col])

        for row in range(rows):
            dfs(row, 0, pacific, heights[row][0])
            dfs(row, cols - 1, atlantic, heights[row][cols - 1])

        result = []

        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific and (row, col) in atlantic:
                    result.append([row, col])

        return result