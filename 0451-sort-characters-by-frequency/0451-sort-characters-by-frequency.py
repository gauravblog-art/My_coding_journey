class Solution:
    def frequencySort(self, s: str) -> str:
      
      
      dic=Counter(s)
      dic=dict(sorted(dic.items(), key=lambda x:x[1], reverse=True ))

      a=''
      
      for k , v in dic.items():
        
        a+=k*v
      return a