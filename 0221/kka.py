import sys
sys.stdin = open("input.txt", "r")

def dfs(s):
    for e in arr[s]:
        if v[e] == 0:
            v[e] = 1
            dfs(e)


T = int(input())
for t in range(1,T+1):
    V,E = map(int,input().split())
    arr = [[] for _ in range(V+1)]
    for _ in range(E):
        s,e = map(int,input().split())
        arr[s].append(e)
    S,G = map(int,input().split())
    v = [0]*(V+1)
    dfs(S)
    print(v[G])