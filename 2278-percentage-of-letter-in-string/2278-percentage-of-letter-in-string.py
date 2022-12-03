class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        
        
        n=len(s)
        dic=Counter(s)
        
        if letter in s:
          
          return int((dic[letter]/n)*100)
        else:
          
          return 0