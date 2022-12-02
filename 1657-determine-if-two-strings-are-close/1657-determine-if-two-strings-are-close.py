class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
      
      if len(word1)!=len(word2):
        
        return False
      
      
      dic1=Counter(word1)
      dic2=Counter(word2)
      
      # print(dic1.keys())
      # print(dic2.keys())
      

      if (dic1.keys()==dic2.keys()) and sorted(dic1.values())==sorted(dic2.values()):
        return True
      
      else:
        
        False
        