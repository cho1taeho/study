import sys
sys.stdin = open("input.txt", "r")

st = input()
st_idx = []
temp = []
if '<' in st:                      # st 안에 괄호가 있다면
    st1 = '>' +st+'<'              # st1 은 st 좌우에 괄호를 하나씩 더 더해준다
    for i in range(len(st1)):
        if st1[i] == '<' or st1[i] == '>':      # st에 <>의 위치를 찾는다
            st_idx.append(i)                    #st_idx 는  괄호들의 위치
    for j in range(len(st_idx)-1):
        temp.append(st1[st_idx[j]:st_idx[j+1]+1]) # 괄호 별로 잘라서 temp 에 보관

    for k in range(len(temp)):
        if temp[k][0]=='>'and temp[k][-1] == '<':   #temp에서 > < 사이에 있는 단어들은
            temp[k] = temp[k][1:-1]                 # ><를 잘라서 뽑아낸다
            temp[k] = temp[k].split()               # 저 사이에 띄어쓰기가 있는경우
            for x in range(len(temp[k])):           # 단어가 뒤집히는게 아닌 띄어쓰기를 기준으로 돌아서
                temp[k][x] = temp[k][x][::-1]       # 그후에 뒤집는다


            temp[k] = ' '.join(temp[k])

    result = ''.join(temp)
    print(result)
else:                            # st안에 괄호가 없다면
    a = st.split()               # 띄어쓰기 별로 나눠서
    for i in range(len(a)):
        b= []
        b.append(a[i][::-1])     # 뒤집는다
        print(*b, end=' ')
    print()