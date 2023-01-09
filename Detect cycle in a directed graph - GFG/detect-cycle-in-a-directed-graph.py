#User function Template for python3


class Solution:
    

    def isCyclic(self, v, adj):
        # code herr
        coming_degree=[0]*v
        
        for i in range(v):
            
            for j in adj[i]:
                coming_degree[j]+=1
        
        queue=[]
        
        for i in range(v):
            if coming_degree[i]==0:
                queue.append(i)
        
        count=0
        
        while queue:
            
            node=queue.pop(0)
            count+=1
            
            for i in adj[node]:
                coming_degree[i]-=1
                
                if coming_degree[i]==0:
                    queue.append(i)
        if count==v:
            return False
        else:
            
            return True

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