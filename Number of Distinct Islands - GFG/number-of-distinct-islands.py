#User function Template for python3

import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        # code here
        
        def DFS(r,c,r0,c0,visited,lst):
            
            
            visited.add((r,c))
            lst.append((r-r0,c-c0))
            
            for i,j in direction:
                row=r+i
                col=c+j
                
                if 0<=row<len(grid) and 0<=col<len(grid[0]) and grid[row][col]==1 and (row,col) not in visited:
                    
                    DFS(row,col,r0,c0,visited,lst)
        n=len(grid)
        m=len(grid[0])
        visited=set()
        ans=set()
        direction=[(0,-1),(-1,0),(0,1),(1,0)]
        for i in range(n):
            
            for j in range(m):
                
                if (i,j) not in visited and grid[i][j]==1:
                    
                    lst=[]
                    DFS(i,j,i,j, visited, lst)
                    ans.add(tuple(lst))
                    
        return len(ans)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.countDistinctIslands(grid))
# } Driver Code Ends