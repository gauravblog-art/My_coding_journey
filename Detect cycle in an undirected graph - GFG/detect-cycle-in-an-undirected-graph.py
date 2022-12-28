from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
    
    def cycle(self,v, adj, visited):
        
        visited[v]=True
        
        queue=[]
        
        queue.append([v,-1])
        
        while queue:
            
            node=queue[0][0]
            parent=queue[0][1]
            
            queue.pop(0)
            for i in adj[node]:
                
                if visited[i]==False:
                    visited[i]=True
                    queue.append([i, node])
                    
                elif i!=parent:
                    return True
        return False
                    
        
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		
		visited=[False for i in range(V)]
		
		for i in range(V):
		    
		    if visited[i]==False:
		        
    		    if self.cycle(i, adj, visited)==True:
    		        
    		        return True
    		        
		return False
		        
		    
		
		
		


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends