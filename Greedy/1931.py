import sys
N = int(sys.stdin.readline())
schedule = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
sort_schedule=sorted(schedule, key=lambda x:(x[1],x[0]))

cnt = 1
init = sort_schedule[0][1]
for i in range(1, N):
    if sort_schedule[i][0] >= init:
        init = sort_schedule[i][1]
        cnt += 1
print(cnt)
