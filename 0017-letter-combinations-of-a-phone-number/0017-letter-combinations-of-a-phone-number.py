class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
      
      if digits=='':
        return []
      
      ans=[]
      def phonepad(digits,output,mapping):
        
        if not digits:
          ans.append(output)
          return
        
        ch=mapping[digits[0]]
        
        for c in ch:
          
          phonepad(digits[1:], output+c, mapping)
          
      mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
      phonepad(digits,'',mapping)
        
      return ans