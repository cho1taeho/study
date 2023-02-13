import sys
sys.stdin = open("input.txt", "r")

def flatten(lst):    # 사회자가 부르는 빙고 평탄화
    result = []
    for item in lst:
        if type(item) == list:
            result += flatten(item)
        else:
            result += [item]
    return result
arr = [list(map(int,input().split())) for _ in range(5)]    # 내가쓴 빙고
arr_j = [list(map(int,input().split())) for _ in range(5)]  # 사회자가 부르는 빙고
cnt = 0
arr_s = []          # 사회자
arr_d = []          # 대각선
arr_bd = []         # 반대각선
arl = []            # 빙고가 되는 경우의 수
arr_s.append(arr_j)
asd = flatten(arr_s) #사회자가 부르는 순서
arr_t = list(map(list,zip(*arr))) # 열을 기준으로 되는 빙고
for i in range(5):
    arr_d.append(arr[i][i])
    arr_bd.append(arr[i][4-i])
arl = arr+arr_t      # 행과 열의 빙고를 더하고
arl.append(arr_d)   # 대각선
arl.append(arr_bd)  # 반대각선도 추가한다

ans = 0
for n in range(25):      # 총수가 25개
    ans +=1              # 하나 부를떄마다 한개씪 더하고
    for i in range(12):   # 총 빙고의 개수 12개
        for j in range(5):  # 빙고 한줄에 5칸
            if arl[i][j] == asd[n]:  # 내 빙고칸의 좌표가 사회자가 부르는 순서대로 같다먄
                arl[i][j] = 0    # 내빙고를 0 으로 바꾼다

    if arl.count([0]*5) >= 3:    # 12개의 줄중  0 0 0 0 0 으로 바뀌는 줄이 3개 이상이 되면
        break                   # 멈춘다

print(ans)
