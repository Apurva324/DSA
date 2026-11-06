class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph)
        colors = [-1] * n

        def dfs(node, c):
            colors[node] = c

            for j in range(len(graph[node])):
                neighbour = graph[node][j]

                # If neighbour has not been colored
                if colors[neighbour] == -1:
                    if not dfs(neighbour, 1 - c):
                        return False

                # If neighbour has the same color
                elif colors[neighbour] == c:
                    return False

            return True

        for i in range(n):
            if colors[i] == -1:
                if not dfs(i, 0):
                    return False

        return True