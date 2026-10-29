class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Lines and columns
        N = 9
        num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

        # For rows 
        for i in range (N):
            seen = []
            for j in range (N):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen or board[i][j] not in num:
                    return False 
                else : 
                    seen.append(board[i][j])
        #For columns 
        for j in range(N):
            seen = []
            for i in range(N):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen or board[i][j] not in num:
                    return False 
                else : 
                    seen.append(board[i][j])
        
        # For 9x9 matrix 
        
        for x in [0, 3, 6]:
            for y in [0,3,6]: 
                seen = []
                for i in range (x, x+3):
                        for j in range (y, y+3):
                            if board[i][j] == ".":
                                continue
                            if board[i][j] in seen or board[i][j] not in num:
                                return False 
                            else : 
                                seen.append(board[i][j])
            
        return True