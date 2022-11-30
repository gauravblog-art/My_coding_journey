class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
      dic=Counter(arr)
      
      lst=[]
      
      for k, v in dic.items():
        
        if v not in lst:
          lst.append(v)
        else:
          
          return False
      return True
    