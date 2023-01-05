class Solution:
    
    
    def bipartite(self,v, adj, color):
        
        queue=[]
        
        queue.append(v)
        color[0]=0
        
        while queue:
            node=queue.pop(0)
            
            for ad_node in adj[node]:
                
                if color[ad_node]==-1:
                    if color[node]==0:
                        
                        color[ad_node]=1
                    else:
                        color[ad_node]=0
                    queue.append(ad_node)
                else:
                    if color[ad_node]==color[node]:
                        
                        return False
        return True
            
        
	def isBipartite(self, v, adj):
	    
		#code here
		color=[-1]*v
		
		for i in range(v):
		    
		    if self.bipartite(i, adj, color)== False:
		        
		        return False
		return True
		    


#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().strip().split())
		adj = [[] for i in range(V)]
		for i in range(E):
			u, v = map(int, input().strip().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isBipartite(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends