class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) ;  n = len(matrix[0])

        k = 0 ; l = m*n - 1

        while k <= l:
            mid = (k+l) // 2
            i = mid//n
            j = mid % n

            if target < matrix[i][j]:
                l = mid - 1
            elif target > matrix[i][j]:
                k = mid + 1
            else:
                return True
        
        return False
        
       