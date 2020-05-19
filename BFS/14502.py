import collections
import copy

dx=[1,-1,0,0]
dy=[0,0,1,-1]

N, M=map(int, input().split())
maps=[list(map(int, input().split())) for _ in range(N)]
arrived=[[0]*M for _ in range(N)]
safe=list()
temp=list()
maxx=0

def calcv(mapss):
    count=0
    for i in range(N):
        for j in range(M):
            if mapss[i][j] == 0:
                count += 1
    return count

def bfs(mapsss):
    q=collections.deque()
    for i in range(N):
        for j in range(M):
            if mapsss[i][j] == 2:
                q.append([i,j])
    while q:
        s=q.popleft()
        mapsss[s[0]][s[1]]=2
        for i in range(4):
            xx=s[0]+dx[i]
            yy=s[1]+dy[i]
            if 0<=xx<=N-1 and 0<=yy<=M-1 and mapsss[xx][yy] == 0:
                q.append([xx,yy])





for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:
            safe.append([i,j])

for i in range(len(safe)-2):
    for j in range(i+1, len(safe)-1):
        for k in range(j+1, len(safe)):
            temp=copy.deepcopy(maps)
            temp[safe[i][0]][safe[i][1]] = 1
            temp[safe[j][0]][safe[j][1]] = 1
            temp[safe[k][0]][safe[k][1]] = 1
            bfs(temp)
            maxx=max(maxx,calcv(temp))
            
print(maxx)

