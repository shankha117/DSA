# https://leetcode.com/problems/zero-array-transformation-i/description/

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:

        n = len(nums)
        diff = [0]* (n+1)

        # create the difference array
        for l,r in queries:
            diff[l] += 1
            diff[r+1] -= 1

        # Step 3: Build the prefix sum to get the number of times each index was covered
        # so prefix[i] => how many time the index i has occured in the range queries

        # prefix = list(accumulate(diff))

        prefix = [0]*(n+1)
        cur = 0
        for i in range(n):
            cur += diff[i]
            prefix[i] = cur

        # so at any given index i if nums[i] > prefix[i]
        # lets say , nums = [4,3,2,1] ; prefix = [1,2,2,1,0]; i = 0
        # it means , we can only reduce the number 4 , 1 time .
        # so 4 can not be transformed to 0 ; hence False is returned
        for i in range(n):
            if nums[i] > prefix[i]:
                return False

        return True

# Great question! The use of `r + 1` instead of `r` is the **core idea of the line sweep (or difference array) technique** — it's what makes it efficient and elegant.

# ---

# ### 🧠 Intuition Behind `r + 1`:

# We want to **apply a range update** efficiently:
# When a query says "decrement all values in the range `[l, r]` by 1", we don't want to iterate from `l` to `r`. Instead, we:

# * **Increment** the effect at index `l` (start of range)
# * **Decrement** the effect **after** index `r` (i.e., at `r + 1`), to cancel out the earlier increment beyond the range

# This way, when we compute a prefix sum later, only the range `[l, r]` will be affected.

# ---

# ### 🔍 Visual Example:

# Suppose `nums = [0, 0, 0, 0, 0]` and query = `[1, 3]` (i.e., affect indices 1 through 3):

# ```python
# diff = [0, 0, 0, 0, 0, 0]  # Size = len(nums) + 1

# diff[1] += 1   # Mark start of range
# diff[4] -= 1   # Mark end+1 of range
# ```

# Now `diff = [0, 1, 0, 0, -1, 0]`

# When we do a prefix sum:

# ```python
# coverage[0] = 0
# coverage[1] = 1  ← start of the range
# coverage[2] = 1
# coverage[3] = 1  ← end of the range
# coverage[4] = 0  ← back to zero, unaffected
# ```

# So only indices 1 to 3 are affected — exactly what we want.

# ---

# ### 🔁 If We Used `r` Instead of `r + 1`?

# We'd incorrectly cancel the effect **at** index `r`, so the range would become `[l, r-1]`, **excluding `r`**.

# ---

# ### ✅ Conclusion:

# We use `r + 1` so that:

# * The prefix sum applies the update from index `l` **up to and including** index `r`
# * Index `r + 1` cancels the effect **just after** the range

# This is what makes the **difference array / line sweep** technique both fast and correct.

# Let me know if you'd like an animation or deeper visual explanation!
