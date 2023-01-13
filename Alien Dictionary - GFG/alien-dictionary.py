#User function Template for python3

from collections import defaultdict
class Solution:
    def findOrder(self,dict, N, K):
    # code here
    
        adj=defaultdict(list)
        
        for i in range(N-1):
            str1=dict[i]
            str2=dict[i+1]
            min_node=min(str1,str2)
            
            for j in range(len(min_node)):
                
                if str1[j]!=str2[j]:
                    adj[ord(str1[j]) - ord("a")].append(ord(str2[j]) - ord("a"))
                    break
        
        # now i have to find the totposort
        
        incoming_degree=[0]*K
        
        for i in range(K):
            
            for j in adj[i]:
                
                incoming_degree[j]+=1
                
        queue=[]
        
        for i in range(len(incoming_degree)):
            
            if incoming_degree[i]==0:
                queue.append(i)
        topo_lst=[]      
        while queue:
            node=queue.pop(0)
            topo_lst.append(node)
            
            for i in adj[node]:
                
                incoming_degree[i]-=1
                if incoming_degree[i]==0:
                    queue.append(i)
        ans=''
        
        for i in topo_lst:
            
            ans+=chr(i+ord("a"))
            
        return ans
        
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends