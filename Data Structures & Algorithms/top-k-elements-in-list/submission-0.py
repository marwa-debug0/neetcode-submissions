class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for x in nums:
            if x in freq:
                freq[x] += 1
            else : 
                freq[x] = 1
        
        return sorted(freq, key=freq.get, reverse = True)[:k]