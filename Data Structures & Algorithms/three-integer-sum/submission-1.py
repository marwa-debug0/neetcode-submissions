class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        n = len(nums)

        for k in range(n):
            i = k+1
            j = n-1
            while (i < j):
                x = -nums[k]; y = nums[i]; z = nums[j]
                sum = y + z

                if (sum == x):
                    res.add((-x,y,z))
                if sum > x: 
                    j -= 1
                else : 
                    i += 1


        
        return list(res) 

        
        







        