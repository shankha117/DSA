from itertools import product
def rod_cutting(prices: list[int], n: int):

    N = len(prices)
    length = [x for x in range(1, N+1)]

    dp = [[0]*(n+1) for _ in range(N+1)]


    for i,j in product(range(1, N+1), range(1, n+1)):

        # if the last item is more than the remianing length then skip that item
        if length[i-1] > j:
            dp[i][j] = dp[i-1][j]

        else:
            include = prices[i-1] + dp[i][j-length[i-1]]

            exclude = dp[i-1][j]


            dp[i][j] = max(include, exclude)


## position of the cuts
    pos = []
    i,j = N,n
    while i > 0 and j > 0:
        if dp[i][j] == dp[i-1][j]:
            i -= 1
        else:
            pos.append(j)
            j -= i
    return pos

    ## if asked size of the cuts
    pos = []
    i,j = N,n
    while i > 0 and j > 0:
        if dp[i][j] == dp[i-1][j]:
            i -= 1
        else:
            pos.append(i)   # this is changed , so insted of the column we take the rows
            j -= i
    return pos


    """
    Lets See Why does this work !!!
    """

    # if st[i][j] == st[i-1][j]:
    #     i -= 1
    #
    """
    This means: "Item i was not used in the optimal solution for this subproblem."

    Why? Because the optimal profit didn’t change when item i was considered.

    So, we move up the table (i.e., exclude item i) and check the previous item.

    and then
    """

    # else:
    #     # Item i was used at least once
    #     pos.append(...)  # either size or position
    #     j -= i  # reduce capacity by the item's weight (length)

    """

    If the value did change (st[i][j] != st[i-1][j]), it means we included item i in the solution.

    So, you:

    Record the choice (i or j)

    Subtract the weight (length i) from capacity j (since that much is used up)

    Continue with the same item i (because it can be reused in unbounded knapsack)

    """
