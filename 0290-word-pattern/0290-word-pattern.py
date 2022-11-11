class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
      s=s.split(' ')
      d1=dict()
      d2=dict()
      
      if len(s)!=len(pattern):
        return False
      
      for i in range(len(s)):
        
        c1=s[i]
        c2=pattern[i]
        
        if (c1 in d1 and d1[c1]!=c2) or (c2 in d2 and d2[c2]!=c1):
          return False
        else:
          
          d1[c1]=c2
          d2[c2]=c1
      return True