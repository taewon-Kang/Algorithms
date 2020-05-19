n=int(input())
cost=[[0,0,0] for _ in range(1001)]
for i in range(1, n+1):
    cost[i][0], cost[i][1], cost[i][2]=map(int, input().split())

dp=[[0,0,0] for _ in range(1001)]
dp[1][0]=cost[1][0]
dp[1][1]=cost[1][1]
dp[1][2]=cost[1][2]
for i in range(2,n+1):
    dp[i][0]=min(cost[i][0]+dp[i-1][1],cost[i][0]+dp[i-1][2])
    dp[i][1]=min(cost[i][1]+dp[i-1][0],cost[i][1]+dp[i-1][2])
    dp[i][2]=min(cost[i][2]+dp[i-1][0],cost[i][2]+dp[i-1][1])
print(min(dp[n]))
