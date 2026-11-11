class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        answer = right

        while left <= right:
            k = (left + right) // 2

            hours = 0
            for pile in piles:
                hours += (pile + k - 1) // k

            if hours > h:
                left = k + 1
            else:
                answer = k
                right = k - 1

        return answer
