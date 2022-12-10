def costsum(n, dp, cost):

    if n == 0:
        dp[0] = cost[0]
    elif n==1:
        dp[1] = cost[1]
    elif n==2:
        dp[2] = cost[2]
    else:
        dp[n] = min(dp[n-2]+cost[n-1], dp[n-1]+cost[n-1])
    if n == len(cost) - 1:
        return dp[n]
    return costsum(n+1, dp, cost)


num = int(input("계단의 개수 :"))
cost = list(map(int, input("각 계단을 밟을 때 비용 : ").split(" ")))

dp = [0]*num
print(costsum(0, dp ,cost))