# https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        if len(sentence) < 26: return False
        
        alpha_dict = {c:0 for c in string.ascii_lowercase}

        for s in sentence:
            alpha_dict[s] = 1
        
        return sum(alpha_dict.values()) == 26

        # for c in string.ascii_lowercase:
        #     if c not in sentence: 
        #         return False
        
        # return True