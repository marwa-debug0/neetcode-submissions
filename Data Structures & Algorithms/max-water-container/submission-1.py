class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0 
        n = len(height)

        i = 0 ; j = n - 1
        while i < j:
            x = j - i ; y = min(height[i], height[j])
            area = x*y
            if (area > max_area):
                max_area = area
            
            if height[i] <= height[j]:
                i += 1
            else: 
                j -= 1

        
        
        return max_area
            
            
            
        