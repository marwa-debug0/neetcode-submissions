class Solution:
    from collections import Counter
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1) ; n2 = len(s2)
        freq = Counter(s1)
        start = 0 ; end = n1 - 1

        if n1 > n2: 
            return False

        window = s2[start: end+1]
        wind_freq = Counter(window)

        while end < n2: 
            if wind_freq == freq: 
                return True
            else:
                if end == n2-1:
                    break 
                
                wind_freq[s2[start]] -= 1 

                if wind_freq[s2[start]] == 0:
                    del wind_freq[s2[start]]

                start += 1 
                end += 1
                wind_freq[s2[end]] += 1 

            
        return False


        