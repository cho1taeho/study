import sys
sys.stdin = open("input.txt", "r")

N = int(input())
lst = []
ans = 0
for i in range(1,N+1):
    fst = N
    sec = i
    tmp = [N, i]
    while True:
        nex = fst - sec
        i