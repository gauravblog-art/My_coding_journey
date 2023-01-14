#User function Template for python3
from collections import defaultdict
from typing import List

class Solution:
    
    def toposort(self, m, adj, visited, stack):
        
        visited[m]=1
        for i in adj[m]:
            node=i[0]
            if visited[node]==0:
                self.toposort(node, adj, visited, stack)
        
        stack.append(m)
        
    def shortestPath(self, n : int, m : int, edge : List[List[int]]) -> List[int]:
        
        adj=defaultdict(list)
        
        for i in range(m):
            
            u=edge[i][0]
            v=edge[i][1]
            wt=edge[i][2]
            adj[u].append([v,wt])
        
        # now I am going to perform a topo sort
        
        visited=[0]*n
        stack=[]
        for i in range(n):
            if visited[i]==0:
                self.toposort(i, adj, visited, stack)
        ans_dist=[float('inf')]*n
        
        ans_dist[0]=0
        
        while stack:
            node=stack.pop()
            
            for i in adj[node]:
                first=i[0]
                wgt=i[1]
                dist=ans_dist[node]
                putt=dist+wgt
                # print(putt)
                if putt<ans_dist[first]:
                    # print(putt)
                    if putt=="inf":
                        print(putt)
                        ans_dist[first]=-1
                    else:
                        ans_dist[first]=putt
                    
        pure_ans=[-1]*n
        
        for i in range(len(ans_dist)):
            
            if ans_dist[i]!=float("inf"):
                pure_ans[i]=ans_dist[i]
                
        return pure_ans
        
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

from typing import List




class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()



class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,m=map(int,input().split())
        
        
        edges=IntMatrix().Input(m, 3)
        
        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        
        IntArray().Print(res)
# } Driver Code Ends