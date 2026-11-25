class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0 ; j = n - 1

        while i <= j:
            if nums[i] <= nums[j]:
                return nums[i]

            k = (i+j) // 2
            if nums[k] < nums[i]:
                j = k 
            elif nums[k] > nums[j]:
                i = k + 1 
            else : 
                return nums[k]
        


        