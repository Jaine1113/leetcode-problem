class Solution:
    def minTime(self, n, edges, hasApple):
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, parent):
            time = 0

            for child in graph[node]:
                if child != parent:
                    t = dfs(child, node)
                    if t > 0 or hasApple[child]:
                        time += t + 2

            return time

        return dfs(0, -1)