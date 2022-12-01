class Solution:
    def halvesAreAlike(self, s: str) -> bool:
      
      n=len(s)
      str1=s[:n//2]
      str2=s[n//2:]
      
      vow=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
      
      c1=0
      c2=0
      
      for i in str1:
        
        if i in vow:
          c1+=1
      for j in str2:
        
        if j in vow:
          c2+=1
      if c1==c2:
        return True
      else:
        return False
      