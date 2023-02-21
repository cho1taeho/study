import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    msm = 0
    for i in range(len(arr)):  # 모든 합
        msm += sum(arr[i])
    arrt = arr[:]
    n = N // 2
    for i in range(len(arrt)):
        arrt[i].pop(n)  # 사분할
    arrt.pop(n)

    nopil = 0

    for i in range(len(arrt)):
        for j in range(len(arrt) // 2):
            arrt[i][j] = arrt[i][j] + arrt[i][len(arrt) - j - 1]  # 십자로 자른 판중 세로를 기준으로 반접는다
        arrt[i] = arrt[i][0:2]  # 앞에 두개만 필요

    for i in range(len(arrt) // 2):
        arrt[i] = [x + y for x, y in zip(arrt[i], arrt[len(arrt) - i - 1])]  # 다시 가로로 합친다
    arrt = arrt[0:2]  # 앞에 두개만 필요

    arrt = arrt[::-1]

    for i in range(len(arrt)):
        for j in range(i + 1):
            nopil += arrt[i][j]
    ans = msm - nopil
    print(f'#{t} {ans}')