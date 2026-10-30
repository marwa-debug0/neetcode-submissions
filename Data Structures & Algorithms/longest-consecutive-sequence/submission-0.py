class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {x : x + 1 for x in set(nums)}
        max_sequence = 1

        if nums == []:
            return 0
        
        for key in dic.keys():
            if key - 1 not in dic:
                max_key = 1
                current_key = key
                
                while dic[current_key] in dic.keys():
                    current_key = dic[current_key]
                    max_key += 1
                
                max_sequence = max(max_key, max_sequence)
        
        return max_sequence