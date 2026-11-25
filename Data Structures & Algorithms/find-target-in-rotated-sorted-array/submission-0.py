class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i = 0
        j = n - 1
        k = 0

        # Step 1: Find the pivot (minimum element's index)
        while i <= j:
            if nums[i] <= nums[j]:
                k = i
                break

            pivot = (i + j) // 2

            if nums[pivot] < nums[i]:
                j = pivot
            elif nums[pivot] > nums[j]:
                i = pivot + 1
            else:
                k = pivot
                break

        # Step 2: Determine which sorted half to search
        if target == nums[k]:
            return k

        if nums[0] <= target <= nums[k - 1] and k > 0:
            i = 0
            j = k - 1
        else:
            i = k
            j = n - 1

        # Step 3: Binary search
        while i <= j:
            mid = (i + j) // 2

            if nums[mid] > target:
                j = mid - 1
            elif nums[mid] < target:
                i = mid + 1
            else:
                return mid

        return -1
