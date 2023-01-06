class Solution:
    
    
    def bipartite(self,v,col, adj, color):
        
        color[v]=col
        for ad_node in adj[v]:
            # print(color[ad_node])
            if color[ad_node]==-1:
                # self.bipartite(ad_node, not(col), adj, color)
                if col==0:
                    if self.bipartite(ad_node, 1, adj, color)==False:
                        return False
                else:
                    if self.bipartite(ad_node, 0, adj, color)==False:
                        return False
            elif color[ad_node]==col:
                # print(True)
                return False
        return True
                    
                
                
	def isBipartite(self, v, adj):
	    
		#code here
		color=[-1]*v
# 		print(color,v)
		for i in range(v):
		    
		    if color[i]==-1:
		        
    		    if self.bipartite(i,0, adj, color)== False:
    		        
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