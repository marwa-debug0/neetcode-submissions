class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

        n = len(nums)
        if k > n: 
            return []
        if n == 0:
            return []
        if n == 1 : 
            return nums
        
        
        start = 0 ; end = k - 1
        res = []
        dq = deque()

        for i in range(n):
            while dq and dq[0] <= i - k:
                dq.popleft()
            # Remove smaller numbers
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            # Add the new index
            dq.append(i)

            # Record maximum once window is complete
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res


        
        
       
        return maximums
        