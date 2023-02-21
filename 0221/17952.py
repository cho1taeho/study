import sys
# sys.stdin = open("input.txt", "r")

T = int(sys.stdin.readline())
stk = []
ans = 0
for t in range(T):
    lst = list(map(int,sys.stdin.readline().split()))
    if lst[0] == 1:                                # 과제를 받앗을 떄
        if lst[-1] == 1:                           # 과제 시간이 1이면
            ans += lst[1]                          # 정답에  점수를 더하고
        else:                                      # 그게 아니면 과제의 점수와 시간-1을 스택에 저장한다
            stk.append([lst[1],lst[-1]-1])         #(-1은 받자마자 1분이 흐르므로)
        continue                                   # 0이 나오면 넘어가라
    if stk:                                        # 스택이 있을경우
        stk[-1][-1] = stk[-1][-1]-1                # 스택 탑의 시간을 1분씩 뺴라
        if stk[-1][-1] == 0:                       # 그러다 시간이 0이 되면
            s = stk.pop()                          # 스택을 팝하고
            ans += s[0]                            # 정답에 점수를 더한다
print(ans)