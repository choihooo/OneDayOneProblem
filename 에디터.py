from sys import stdin
 
stk1 = list(stdin.readline().strip()) # 한줄 짜리 입력을 받아서 리스트로 만든다.
stk2 = []
n = int(input())
for line in stdin: # 입력을 받으면서 for문을 돌린다.
    if line[0] == 'L':
        if stk1: stk2.append(stk1.pop())
        else: continue
    elif line[0] == 'D':
        if stk2: stk1.append(stk2.pop())
        else: continue
    elif line[0] == 'B':
        if stk1: stk1.pop()
        else: continue
    elif line[0] == 'P':
        stk1.append(line[2])
print(''.join(stk1 + list(reversed(stk2))))