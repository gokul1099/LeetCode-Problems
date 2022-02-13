from collections import deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjList = [[] for i in range(n)]
        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        queue = deque([source])
        seen=set([source])
        while(queue):
            node = queue.popleft()
            if node == destination:
                return True
            
            for val in adjList[node]:
                if val not in seen:
                    seen.add(val)
                    queue.append(val)
        return False        
          
        