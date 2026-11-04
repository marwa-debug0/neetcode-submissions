class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0 
        n = len(height)
        l = 0 ; r = n - 1 
        l_max = 0 ; r_max = 0

        while (l < r):
            l_max = max(l_max, height[l])
            r_max = max(r_max, height[r])

            if l_max < r_max : 
                total += l_max - height[l]
                l += 1
            else : 
                total += r_max - height[r]
                r -= 1 


        
        return total 



    
        

        