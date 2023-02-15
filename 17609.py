import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1,T+1):
    st = list(input())
    st1 = st[:]        # 유사회문이 둘중에 멀뺼지 모르니 두개준비
    st2 = st[:]
    if st == st[::-1]:      # 회문이되면 회문이고
        print(0)
    else: # 그게아니면
        for i in range(len(st)):    # 앞뒤로 비교해서
            if st[i] != st[len(st)-i-1]:  # 다른문자가 나온 시점에 멈추고
                del st1[i]     # 하나는 앞에걸
                del st2[len(st)-i-1] #하나는 뒤에걸 뺸다
                break
                # 나는 어차피 반복문이 한바퀴를 다돌아도 회문이니 상관이없다고생각 # 이걸 반만돌면 시간이 줄어드는지?

        if st1 == st1[::-1] or st2 == st2[::-1]:  #둘중에 하나라도 회문이되면 유사회문
            print(1)
        else:  # 다 안되면 회문이 아니다
            print(2)
