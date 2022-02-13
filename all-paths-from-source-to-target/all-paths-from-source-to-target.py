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
                
        def bfs():
            currPath = queue.popleft()
            node = currPath[-1]
            for val in graph[node]:
                tempPath = currPath.copy()
                tempPath.append(val)
                if val == len(graph)-1:
                    paths.append(tempPath)
                else:
                    queue.append(tempPath)
        
        if not graph or len(graph)==0:
            return paths
        queue = collections.deque()
        qPath =[0]
        queue.append(qPath)
        while(queue):
            bfs()
        return paths
    
    
#        def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
#         paths = []
#         if not graph or len(graph) == 0:
#             return paths

#         queue = deque()
#         path = [0]
#         queue.append(path)

#         while queue:
#             current_path = queue.popleft()
#             node = current_path[-1]
#             for next_node in graph[node]:
#                 temp_path = current_path.copy()
#                 temp_path.append(next_node)

#                 if next_node == len(graph) - 1:
#                     paths.append(temp_path)
#                 else:
#                     queue.append(temp_path)
#         return paths
        
                
            
        