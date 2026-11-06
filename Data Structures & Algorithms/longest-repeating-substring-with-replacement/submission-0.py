class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        start = 0 
        maxFreq = 0 
        count = {}
        max_length = 0 

        for end in range(n):
            count[s[end]] = count.get(s[end], 0) + 1
            maxFreq = max(maxFreq, count[s[end]])

            window_length = end - start + 1

            if window_length - maxFreq > k:
                count[s[start]] -= 1
                start += 1
            
            max_length = max(max_length, end - start + 1)

        return max_length



        
            
        