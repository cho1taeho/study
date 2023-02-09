import sys

sys.stdin = open("input.txt", "r")
#   1
# 3   4
#   2
# a =     4, 5 /              1 4
# b =     0, 3  /             3,2
# c =     8, 0 /              2,8
# 내위    3, 0 /              2 3

w, h = map(int, input().split())
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
me =list(map(int,input().split()))
ans = 0
c = 0
lst = []
p = 2 * (w + h)

def mm(a):
    if a[0] == 1:
        an = w + h + w - a[1]
    elif a[0] == 2:
        an = a[1]
    elif a[0] == 3:
        an = w + h + w + a[1]
    elif a[0] == 4:
        an = w + h - a[1]
    return an
c = mm(me)

for i in range(n):
    lst.append(mm(arr[i]))
    if abs(c - lst[i]) > w+h:
        ans += (p - abs(c- lst[i]))
    else:
        ans += abs(c - lst[i])
print(ans)


