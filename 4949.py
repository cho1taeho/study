import sys
sys.stdin = open("input.txt", "r")


def check(line):
    stack = []
    for char in line:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')' or char == ']':
            if not stack:
                return 'no'
            elif char == ')' and stack.pop() != '(':
                return 'no'
            elif char == ']' and stack.pop() != '[':
                return 'no'
    if stack:
        return 'no'
    return 'yes'

while 1 :
    line = list(input())   #리스트로 input 받아
    if line == ['.']:      # . 이면 멈춰라
        break
    print(check(line))