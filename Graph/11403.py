import collections

n=int(input())
maps=[list(map(int, input().split())) for _ in range(n)]
final=[list([0]*n) for _ in range(n)]

def bfs(a, b):
    q=collections.deque()
    arrived=[0]*n
    arrived[a]=1

    for i in range(n):
        if maps[a][i] == 1:
            q.append(i)

    while q:
        if b in q:
            final[a][b] = 1
            break
        else:
            s=q.popleft()
            if arrived[s]==0:
                arrived[s]=1
                for i in range(n):
                    if maps[s][i] == 1:
                        q.append(i)
            else:
                continue
        

    
for i in range(n):
        for j in range(n):
            bfs(i,j)
for i in range(n):
        fstr=""
        for j in range(n):
            fstr += str(final[i][j]) + " "
        print(fstr)     

