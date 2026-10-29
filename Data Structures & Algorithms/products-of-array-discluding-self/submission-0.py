class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = []
        
        seen_left = 1
        seen_right = 1
    
        # i is for the prefix and j for the suffix
        i = 0 ; j = n - 1
        
        while ( i < n ):
            x1 = nums[i] 
            answer.append(seen_left)
            seen_left *= x1
            i += 1
            
        
        while ( j > -1):
            x2 = nums[j]
            answer[j] *= seen_right
            seen_right *= x2
            j -=1
        
        
        return answer
        