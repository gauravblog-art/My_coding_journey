class Solution:
    def romanToInt(self, s: str) -> int:
      roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
      
      s=s.replace('IV', 'IIII')
      s=s.replace('XL', 'XXXX')
      s=s.replace('CD', 'CCCC')
      s=s.replace('IX', 'VIIII')
      s=s.replace('XC', 'LXXXX')
      s=s.replace('CM', 'DCCCC')
      
      ans=0
      
      for i in s:
        ans+=roman[i]
      return ans  