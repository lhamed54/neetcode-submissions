class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n-1:
            return False
        
        visited = set()
        
        graph = {i: [] for i in range(n)}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, parent):

            visited.add(node)

            for neighbour in graph[node]:

                if neighbour == parent:
                    continue
                
                if neighbour in visited:
                    return False

                if not dfs(neighbour, node):
                    return False
            return True

        if not dfs(0, -1):
            return False

        return len(visited) == n
