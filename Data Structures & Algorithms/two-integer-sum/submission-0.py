class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        seen = set()
        sol = []

        for i in range(n):
            if i in seen: 
                continue
            for j in range(i + 1, n):
                if j in seen:
                    continue
                if nums[i] + nums[j] == target: 
                    sol.append(i)
                    sol.append(j)

        return sol
                    
