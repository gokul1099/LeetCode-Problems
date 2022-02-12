class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjList = [[] for i in range(n)]
        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        stack = [source]
        seen=set()
        while(stack):
            node = stack.pop()
            if node == destination:
                return True
            if node in seen:
                continue
                print("Continue")
            seen.add(node)
            for val in adjList[node]:
                stack.append(val)
        return False        
            
        