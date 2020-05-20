import itertools
import copy

N = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))
oper_str=[ ]
for i in range(len(operators)):
    for j in range(operators[i]):
        if i==0:
            oper_str.append("+")
        elif i==1:
            oper_str.append("-")
        elif i==2:
            oper_str.append("*")
        elif i==3:
            oper_str.append("/")       

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
case=fact(N)
perm_oper=[ ]
perm_oper=copy.deepcopy(list(map(''.join, itertools.permutations(oper_str))))
sums=[ ]
for i in range(len(perm_oper)):
    temp=nums[0]
    for j in range(N-1):
        if perm_oper[i][j] == "+":
            temp += nums[j+1]
        elif perm_oper[i][j] == "-":
            temp -= nums[j+1]
        elif perm_oper[i][j] == "*":
            temp *= nums[j+1]
        elif perm_oper[i][j] == "/":
            if temp < 0:
                temp = abs(temp) // nums[j+1]
            else:
                temp = temp // nums[j+1]
    sums.append(temp)
sums.append(-1000000000)
print(max(sums))
sums.pop()
sums.append(1000000000)
print(min(sums))
