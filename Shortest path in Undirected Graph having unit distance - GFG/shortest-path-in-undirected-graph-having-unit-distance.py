#User function Template for python3

from collections import defaultdict
class Solution:
    
   
        
    def shortestPath(self, edges, n, m, src):
        # code here
        
        adj=defaultdict(list)
        
        for i in range(m):
            u=edges[i][0]
            v=edges[i][1]
            adj[u].append(v)
            adj[v].append(u)
        
        
        distance=[float("inf")]*n
        distance[src]=0
        
        queue=[]
        queue.append(src)
        
        while queue:
            
            node=queue.pop(0)
            
            for it in adj[node]:
                if distance[node]+1<distance[it]:
                    distance[it]=distance[node]+1
                    queue.append(it)
                    
        pure_ans=[-1]*n
        
        for i in range(len(distance)):
            
            if distance[i]!=float("inf"):
                pure_ans[i]=distance[i]
        return pure_ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = map(int, input().strip().split())
        edges=[]
        for i in range(m):
            li=list(map(int,input().split()))
            edges.append(li)
        src=int(input())
        ob = Solution()
        ans = ob.shortestPath(edges,n,m,src)
        for i in ans:
            print(i,end=" ")
        print()
        tc -= 1
# } Driver Code Ends