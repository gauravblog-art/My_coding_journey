
from heapq import heapify, heappop, heappush
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        
        dist=[float("inf")]*V
        dist[S]=0
        heap=[]
        heapify(heap)
        heappush(heap, [0,S])
        # print(dist)
        while heap:
            
            no=heappop(heap)
            distance=no[0]
            node=no[1]
            # print(distance, node)
            
            for it in adj[node]:
                # print(it)
                wg=it[1]
                new_node=it[0]
                total_dis=distance+wg
                # print(dist)
                
                if distance+wg<dist[new_node]:
                    # print(dist)
                    dist[new_node]=total_dis
                    # print(dist)
                    heappush(heap, [dist[new_node], new_node])
        return dist
                
                 
               
            
            
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends