class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        def backtrack(i,col,z_diagonal,f_diagonal):
            if i == n:return  True
            for j in range(n):
                if j not in col and i + j not in  z_diagonal and i - j not in f_diagonal:
                    if backtrack(i+1, col | {j}, z_diagonal |{i + j} , f_diagonal |{i - j}  ) :
                        self.res += 1
            return False
        backtrack(0,set(),set(),set())    
        return self.res
