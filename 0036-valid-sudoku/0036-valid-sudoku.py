class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
      s= set()
      for i in range(len(board)):
        for j in range(len(board)):
          # for condition 
          if board[i][j]!='.':
            if 'row'+str(i)+board[i][j] in s :
              return False
              # print("g")
            if 'col'+str(j)+board[i][j] in s:
              return False
              # print('m')
            if 'box'+str(((i//3)*3)+(j//3))+board[i][j] in s:
              # print('k')
              return False
            else:
              s.add('row'+str(i)+board[i][j])
              s.add('col'+str(j)+board[i][j])
              s.add('box'+str(((i//3)*3)+(j//3))+board[i][j])
      print(s)       
      return True
        