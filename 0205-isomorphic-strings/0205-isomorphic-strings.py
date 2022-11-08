class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
      
      if len(s)!=len(t):
        return False
      
      d1=dict()
      d2=dict()
      
      for i in range(len(s)):
        c1=s[i]
        c2=t[i]
        
        if (c1 in d1 and d1[c1]!=c2) or (c2 in d2 and d2[c2]!=c1):
          return False
        
        else:
          d1[c1]=c2
          d2[c2]=c1
          
      return True
      
          
        
      
      
      
      