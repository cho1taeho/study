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
g = sorted(ga)
s = sorted(se)
print(g,s)
g1 = []
s1 = []
while :
    ansi = w - g1[-1]


# for i in range(len(g)):
#     g1.append(w-g[i])
#     w = w-g[i]
# for j in range(len(s)):
#     s1.append(h-s[i])
#     h = h-s[i]

print(s1,g1)
print(s1*g1)