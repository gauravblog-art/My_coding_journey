#User function Template for python3


class Solution:
    
    #Function to detect cycle in a directed graph.
    
    def cycle(self,v, adj, visited, path_visited):
        
        visited[v]=1
        path_visited[v]=1
        
        for i in adj[v]:
            
            if visited[i]==0:
                if self.cycle(i, adj, visited, path_visited)==True:
                    return True
            elif path_visited[i]==1:
                return True
        path_visited[v]=0
        return False
        
        
    def isCyclic(self, v, adj):
        # code herr
        visited=[0]*v
        path_visited=[0]*v        
        for i in range(v):
            
            if visited[i]==0:
                
                if self.cycle(i,adj,visited, path_visited)==True:
                    return True
        return False
                    
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends