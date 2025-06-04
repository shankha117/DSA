# https://leetcode.com/problems/candy/description/

# GREEDYYYYY
# https://www.youtube.com/watch?v=1IzCRCcK17A
class Solution:
    def candy(self, ratings) -> int:

        N = len(ratings)
        candies = [1]*N

        # LEFT TO RIGHT
        # Makes sure , cur has move candy than its left neighbour
        for i in range(1, N):

            print(ratings, i, candies)
            if ratings[i] > ratings[i-1]:

                candies[i] = candies[i-1] + 1

        # RIGHT TO LEFT
        # Makes sure, cur has move candy than its right neighbour

        for i in range(N-2,-1,-1):

            print("LTR",ratings, i, candies)
            if ratings[i] > ratings[i+1]:

                candies[i] = max(candies[i+1] + 1 , candies[i])

        return sum(candies)


s = Solution()
ratings = [1,2,4,3,6]
print(s.candy(ratings))
