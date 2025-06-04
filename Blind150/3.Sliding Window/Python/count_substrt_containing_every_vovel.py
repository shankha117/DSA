# https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/description
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:

        vovel_list = ['a','e','i','o','u']

        vovel_dict = {x:0 for x in vovel_list}

        vovel_count = 0
        const_count = 0

        ans = 0

        l = 0

        cur = 0


        for r in range(len(word)):

            if word[r] in vovel_list:
                if vovel_dict[word[r]] == 0:
                    vovel_count += 1
                vovel_dict[word[r]] += 1
            else:
                const_count += 1
                # reset number of valid substring found in the current window since now it is no more valid
                # because if we had a vovel , the window would still be valid
                # but if I add a consonent , it can not maintain exactly k consonents condition,
                # basically the window is not valid

                cur = 0

            if const_count > k:

                while const_count > k and l < r:

                    if word[l] not in vovel_list:
                        const_count -= 1
                    else:
                        vovel_dict[word[l]] = max(0, vovel_dict[word[l]]-1)
                        if vovel_dict[word[l]] == 0:
                            vovel_count = max(0, vovel_count - 1 )

                    l += 1

            # if we have the right amount of consonants and vowels, shrink current window as much as possible
            # each step is a probable substring if we keep finding vowels on the right
            while vovel_count == 5 and const_count == k:
                cur += 1
                if word[l] not in vovel_list:
                    const_count -= 1
                else:
                    vovel_dict[word[l]] = max(0, vovel_dict[word[l]]-1)
                    if vovel_dict[word[l]] == 0:
                        vovel_count = max(0, vovel_count - 1 )
                l += 1
            ans += cur # sum the overall number of substring in the current window

        return ans
