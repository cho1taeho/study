import sys
sys.stdin = open("input.txt", "r")
#   1
# 3   4
#   2
# a =     4, 5 /              1 4
# b =     0, 3  /             3,2
# c =     8, 0 /              2,8
# 내위    3, 0 /              2 3
def dst(arr):                # 구해준 값을 좌표로 바꾼다
    whi = []
    if arr[0] == 1:          # 북
        whi = (arr[1], h)
    elif arr[0] == 2:        # 남
        whi = (arr[1], 0)
    elif arr[0] == 3:        # 서
        whi = (0, h-arr[1])
    elif arr[0] == 4:        # 동
        whi = (w, h-arr[1])
    return whi
w, h = map(int, input().split())
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]   # 건물의 위치
me = list(map(int, input().split()))        # 나의 위치
ans = 0
art = []
p = 2 * (h + w)   # 블록 전체의 둘레

for i in range(n):
    art.append(dst(arr[i]))  # 건물들의 위치를 좌표로 변환
mee = dst(me)   # 나도 변환
for i in range(n):
    if arr[i][0] == me[0]:              # 나와 건물의 방향이 같다면
        ans += abs(arr[i][1] - me[1])   # 두 위치를 뺴서 절대값
    elif art[i][0] - mee[0]== w or art[i][1] - mee[1]==h:  #나와 맞은편에 있다면
        if sum(art[i])+sum(mee) <= h+w:  # 좌표들의 합이 둘레의 절반이 안될때
            ans += sum(art[i])+sum(mee)
        else : # 절반을 넘을때
            ans += (p - (sum(art[i])+sum(mee)))   # 전체둘레에서 뺴라
    else: # 같지도 않고 마주보지도 않는다면
        ans += (abs(art[i][0]-mee[0])+abs(art[i][1]-mee[1])) # 각축의 차의 합을 더해라
print(ans)   # 실패





