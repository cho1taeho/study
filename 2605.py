import sys
sys.stdin = open("input.txt", "r")

T = int(input())
lst = list(map(int,input().split()))
a = []
ans = []
cnt = 0
for i in range(T):
    b = i - lst[i]
    a.append(b)

for i in a:
    cnt += 1
    ans.insert(i, cnt)

print(*ans)
