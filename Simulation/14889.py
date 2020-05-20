import itertools, sys, copy
input = sys.stdin.readline
N = int(input())
stat = [list(map(int, input().split())) for _ in range(N)]
people = [ ]
for i in range(N):
    people.append(str(i))
people_com = [ ]
people_com = copy.deepcopy(list(map(''.join, itertools.combinations(people, N//2))))
sums = [ ]
for i in range(len(people_com)//2):
    start=0
    link=0
    deff=0
    start_com = [ ]
    link_com = [ ]
    start_com = copy.deepcopy(list(map(''.join, itertools.combinations(people_com[i],2))))
    link_com = copy.deepcopy(list(map(''.join, itertools.combinations(people_com[len(people_com)-1-i],2))))
    for j in range(len(start_com)):
        start += stat[int(start_com[j][0])][int(start_com[j][1])]
        start += stat[int(start_com[j][1])][int(start_com[j][0])]
        link += stat[int(link_com[j][1])][int(link_com[j][0])]
        link += stat[int(link_com[j][0])][int(link_com[j][1])]
    deff=abs(start-link)
    sums.append(deff)
print(min(sums))
