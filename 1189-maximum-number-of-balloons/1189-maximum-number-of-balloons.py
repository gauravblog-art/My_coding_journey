class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
      lst=['b','a','l','o','n']
      
      count=[0]*5
      
      for i in range(len(lst)):
        
        count[i]=text.count(lst[i])
      
      count[2]=count[2]//2
      count[3]=count[3]//2
      
      return min(count)
      
        
        
      
      
      