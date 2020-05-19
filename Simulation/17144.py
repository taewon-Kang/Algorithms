import copy

dx=[-1,1,0,0]
dy=[0,0,1,-1]

R, C, T=map(int, input().split())
maps=[list(map(int, input().split())) for _ in range(R)]
acloc=list()
#공기청정기 찾기
for i in range(R):
    if maps[i][0] == -1:
        acloc.append(i)
        acloc.append(i+1)
        break
#미세먼지 확산
def mm(mapss):
    temp=[[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            cnt=0
            qtt=0
            addlist=list()
            if mapss[i][j] >= 1:
                for k in range(4):
                    xx=i+dx[k]
                    yy=j+dy[k]
                    if 0<=xx<=R-1 and 0<=yy<=C-1 and  mapss[xx][yy] != -1:
                        cnt += 1
                        addlist.append([xx,yy])
                qtt=int(mapss[i][j]/5)
                temp[i][j]+=mapss[i][j] - qtt*cnt
                while addlist:
                    gogo=addlist.pop()
                    temp[gogo[0]][gogo[1]] += qtt
    mapss=copy.deepcopy(temp)
    return mapss
#공기청정기
def ac(mapsss):
    acl=acloc[0]
    acl2=acloc[1]
    for i in range(acl-1,0,-1):
        mapsss[i][0] = mapsss[i-1][0]
    for i in range(C-1):
        mapsss[0][i] = mapsss[0][i+1]
    for i in range(0,acl):
        mapsss[i][C-1] = mapsss[i+1][C-1]
    for i in range(C-1,1,-1):
        mapsss[acl][i] = mapsss[acl][i-1]
    
    for i in range(acl2+1,R-1):
        mapsss[i][0] = mapsss[i+1][0]
    for i in range(C-1):
        mapsss[R-1][i] = mapsss[R-1][i+1]
    for i in range(R-1, acl2, -1):
        mapsss[i][C-1] = mapsss[i-1][C-1]
    for i in range(C-1,1,-1):
        mapsss[acl2][i] = mapsss[acl2][i-1]
    mapsss[acl][1]=0
    mapsss[acl2][1]=0
    mapsss[acl][0]=-1
    mapsss[acl2][0]=-1

    return mapsss

for _ in range(T):
    maps=mm(maps)
    maps=ac(maps)
summ=0
for i in range(R):
    for j in range(C):
        if maps[i][j] >= 1:
            summ += maps[i][j]
print(summ)
    
