def MinCostClimbStairs(cost):
    # DP array T[i] will store the minimum cost to reach the top 
    n = len(cost)
    T = [0]*n

    # starting from back (bottoms up approach) guessing minimum cost either from last or second last step
    T[n-1] = cost[n-1]
    T[n-2] = cost[n-2]
    # 
    for i in range(n-3,-1,-1):
        cost_1 = T[i+2]
        cost_2 = T[i+1]
        # Choose the cheaper option and add current step cost
        T[i] = (min(cost_1,cost_2) + cost[i])
    return min(T[0],T[1])


import random
cost = [random.randint(1,100) for _ in range(100)]
print(MinCostClimbStairs(cost))