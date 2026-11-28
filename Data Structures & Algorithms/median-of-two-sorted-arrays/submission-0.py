
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A

        m, n = len(A), len(B)
        half = (m + n + 1) // 2

        low, high = 0, m

        while low <= high:
            i = (low + high) // 2
            j = half - i

            leftA = A[i - 1] if i > 0 else float("-inf")
            rightA = A[i] if i < m else float("inf")

            leftB = B[j - 1] if j > 0 else float("-inf")
            rightB = B[j] if j < n else float("inf")

            if leftA <= rightB and leftB <= rightA:
                if (m + n) % 2:
                    return max(leftA, leftB)

                return (max(leftA, leftB) + min(rightA, rightB)) / 2

            elif leftA > rightB:
                high = i - 1

            else:
                low = i + 1
