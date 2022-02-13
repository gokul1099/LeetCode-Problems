class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        tempPath = []
        def dfs(index):
            tempPath.append(index)
            if index== len(graph)-1:
                paths.append(tempPath.copy())
                return
            for nodes in graph[index]:
                dfs(nodes)
                tempPath.pop()
        dfs(0)
        return paths
                
            
        