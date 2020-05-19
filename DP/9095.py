a=int(input())
b=list()
for _ in range(0,a):
    b.append(int(input()))
dp=[0]*11
dp[0]=0
dp[1]=0
dp[2]=1
dp[3]=2
for i in range(4,11):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
dp2=[0]*11
dp2[1]=1
dp2[2]=2
for i in range(3,11):
    dp2[i]=dp[i]+dp2[i-1]
for i in range(0, a):
    print(dp2[b[i]])

