class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
      
      dic=Counter(nums)
      
      d=dict(sorted(dic.items(), key=lambda x:x[1], reverse=True))
      
      lst=list(d.keys())[:k]
      
      return lst

      
      
      
        
        

    
      
        
        
      