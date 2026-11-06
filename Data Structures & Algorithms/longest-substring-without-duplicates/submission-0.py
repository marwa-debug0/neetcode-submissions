class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_length = 0 
        seen = set()

        start = 0 ; end = start 
        while end < n : 
            if s[end] not in seen: 
                seen.add(s[end])
                end += 1 
                max_length = max(max_length, end - start)
            else : 
                max_length = max(max_length, end - start)
                seen.remove(s[start])
                start += 1 
        
        

        if n == 1 : 
            return 1 
        if n == 0 : 
            return 0
        
        return max_length 
