class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        min = 0 
        max = n - 1

        while min < max :
            if numbers[min] + numbers[max] < target: 
                min += 1
            elif numbers[min] + numbers[max] > target:
                max -= 1
            else : 
                return [min + 1, max + 1]
        