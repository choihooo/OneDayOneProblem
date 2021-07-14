# Mock_test

Programmers Mock_test Level 1
language: python
Link: https://programmers.co.kr/learn/courses/30/lessons/42840

```python
def solution(answers):
    answer = []
    size = len(answers)

    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    if len(first) <= size:
        first.extend(first)
    if len(second) <= size:
        second.extend(second)
    if len(third) <= size:
        third.extend(third)

    score = [0, 0, 0]
    for i in range(size):
        if first[i] == answers[i]:
            score[0] += 1
        if second[i] == answers[i]:
            score[1] += 1
        if third[i] == answers[i]:
            score[2] += 1

    max_score = max(score)

    for i in range(len(score)):
        if max_score == score[i]:
            answer.append(i+1)

    return answer
```

처음 제출한 코드: 테스트 케이스 2,3,4 말고 다 런타임 에러가 떴다.

나의 생각: 리스트를 확장하는 코드에서 오류가 생긴거 같았다.

그래서 저 부분을 바꿀수 있는 방법을 생각해보았다.

```python
def solution(answers):
    answer = []
    size = len(answers)

    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0, 0, 0]
    for i in range(size): # 정답과 학생 1, 2, 3의 답을 맞춰보는 코드
        if first[i % 5] == answers[i]:
            score[0] += 1
        if second[i % 8] == answers[i]:
            score[1] += 1
        if third[i % 10] == answers[i]:
            score[2] += 1

    max_score = max(score) # 가장 높은 점수를 구함

    for i in range(len(score)):
		# 동일 점수가 있을수도 있으므로 가장 높은 점수를 뽑아 비교하여 학생을 추가했다.
        if max_score == score[i]:
            answer.append(i+1)

    return answer

```

두번째 제출 코드: 정답

리스트를 확장하는 방법을 쓰지않고 인덱스를 활용한 방법을 생각해보았다.

프로그래머스에서 테스트 케이스를 공개하면 좋았겠지만, 아마도 내 생각에는 리스트의 크기가 너무 커져서 오류가 생기는 거 같았다. 다음에는 무작정 확장하는 방식을 사용하는 것이 아니라 인덱스를 활용한 방법을 먼저 생각해봐야겠다.
