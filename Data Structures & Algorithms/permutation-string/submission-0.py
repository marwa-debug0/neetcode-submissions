class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        letters = {}
        for c in s1:
            letters[c] = letters.get(c, 0) + 1

        start = 0
        n = len(s2)

        while start <= n - len(s1):

            if s2[start] not in letters:
                start += 1
                continue

            counter = dict(letters)
            end = start

            while end < n and s2[end] in counter and counter[s2[end]] > 0:
                counter[s2[end]] -= 1
                end += 1

            if all(v == 0 for v in counter.values()):
                return True

            # Try the next starting position
            start += 1

        return False