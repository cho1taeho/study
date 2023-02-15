import sys
sys.stdin = open("input.txt", "r")

w, h = map(int,input().split())
n = int(input())
ga = []
se = []
for _ in range(n):
    lst = list(map(int,input().split()))
    if lst[0] == 0:
        ga.append(lst[1])
    else:
        se.append(lst[1])

ga.append(h)
ga.append(0)
se.append(w)
se.append(0)

g = sorted(ga,reverse=True)
s = sorted(se,reverse=True)

g1 = []
s1 = []
for i in range(len(g)-1):
    g1.append(g[i]-g[i+1])
for j in range(len(s)-1):
    s1.append(s[j]-s[j+1])
ans = max(g1)*max(s1)
print(ans)


