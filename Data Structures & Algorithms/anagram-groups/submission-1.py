class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_dic = {}
        sol = []

        for i in range(len(strs)):
            word = strs[i]
            sorted_word = ''.join(sorted(word))

            if sorted_word in sorted_dic:
                sorted_dic[sorted_word].append(word)
            
            else:
                sorted_dic[sorted_word] = [word]
        
        
        return list(sorted_dic.values())

