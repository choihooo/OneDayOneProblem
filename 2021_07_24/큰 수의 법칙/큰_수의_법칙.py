# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
#N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수 순서대로 정렬하기
first = data[-1]
second = data[-2]
answer = 0
# 해답2도 여기까진 동일

cnt = 1

for i in range(m):
    if cnt <= 3:
        answer += first
        cnt += 1
    else:
        answer += second
        cnt = 1

print(answer)

# 위에가 실제 상황 만들어서 풀기

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k # m은 더하기 횟수, k는 연속해서 똑같은 수를 더하는 횟수
count += m % (k + 1) 

answer = 0
answer += (count) * first
answer += (m - count) * second

print(answer)

# 수학적 사고로 문제 풀기