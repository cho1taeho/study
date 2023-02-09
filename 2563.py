import sys
sys.stdin = open("input.txt", "r")

ans = []
dic = {}
T = int(input())
for t in range(T):
    a,b = list(map(int,input().split()))
    lst = []

    for i in range(a,a+10):
        for j in range(b,b+10):
            lst.append([i,j])

    ans += lst

ans = set(map(tuple, ans))

print(len(ans))
