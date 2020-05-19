import collections

dx=[-1,0,0,1]
dy=[0,-1,1,0]
cnt=0
cnt2=0
lis=list()

def bfs(a, b):
    global cnt2
    q=collections.deque()
    if maps[a][b]==0 and arrived[a][b]!=1:
        lis.append(1)
        arrived[a][b]=1
        for i in range(4):
                xx=a+dx[i]
                yy=b+dy[i]
                if 0<=xx<=N-1 and 0<=yy<=M-1 and arrived[xx][yy] != 1 and maps[xx][yy]==0:
                    q.append([xx,yy])
        while q:
            lis[cnt2]+=1
            xy=list(q.popleft())
            arrived[xy[0]][xy[1]]=1
            for i in range(4):
                xx=xy[0]+dx[i]
                yy=xy[1]+dy[i]
                if 0<=xx<=N-1 and 0<=yy<=M-1 and arrived[xx][yy] != 1 and maps[xx][yy]==0:
                    arrived[xx][yy] = 1
                    q.append([xx,yy])
        cnt2+=1
        return 1
    else:
        return 0


M, N, K=map(int, input().split())
sqs=[list(map(int, input().split())) for _ in range(K)]
maps=[list([0]*M) for _ in range(N)]
arrived=[list([0]*M) for _ in range(N)]


for i in range(K):
    for j in range(sqs[i][0],sqs[i][2]):#0~4
        for k in range(sqs[i][1],sqs[i][3]):#2~4
            maps[j][k]=1
for i in range(N):
    for j in range(M):
        cnt+=bfs(i,j)
print(cnt)
ans=""
lis.sort()
for i in range(len(lis)):
    ans+=str(lis[i])+" "
print(ans)
