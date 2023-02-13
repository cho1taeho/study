import sys
sys.stdin = open("input.txt", "r")

N = int(input())
lst = []
ans = 0
for i in range(1,N+1):
    fst = N       #첫번쨰
    sec = i       # 두번쨰
    tmp = [N, i]  # 수 저장
    while True:
        nex = fst - sec  # 다음은 첫 - 두
        if nex >= 0:       # 뺀수가 0 보다 크거나 같다면
            tmp.append(nex)   #리스트에 더해라
            fst, sec = sec, nex   #그리고 수를 바꿔라
        else:                       # 0보다 작아진다면
            if len(tmp) > len(lst): # tmp의 최대값을 구해라
                lst = tmp
            break

print(len(lst))
print(*lst)