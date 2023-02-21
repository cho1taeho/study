import sys
sys.stdin = open("input.txt", "r")

def dfs(start):
    stk = []
    s = start
    v[s] = 1
    while True:
        for e in adj[s]:
            if v[e] == 0:
                stk.append(s)
                s = e
                v[s] = 1
                break
        else:
            if stk:
                s = stk.pop()
            else:
                break


T =10
for t in range(1,T+1):
    _ , E = map(int,input().split())
    lst = list(map(int,input().split()))
    N = 100
    adj = [[] for _ in range(N)]
    for i in range(0, len(lst), 2):
        s, e = lst[i], lst[i+1]
        adj[s].append(e)
    print(adj)
    S, G = 0, 99
    v = [0]*N
    dfs(s)
    print(v[G])
