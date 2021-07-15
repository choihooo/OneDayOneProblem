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

ó�� ������ �ڵ�: �׽�Ʈ ���̽� 2,3,4 ���� �� ��Ÿ�� ������ ����.

���� ����: ����Ʈ�� Ȯ���ϴ� �ڵ忡�� ������ ����� ���Ҵ�.

�׷��� �� �κ��� �ٲܼ� �ִ� ����� �����غ��Ҵ�.

```python
def solution(answers):
    answer = []
    size = len(answers)

    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0, 0, 0]
    for i in range(size): # ����� �л� 1, 2, 3�� ���� ���纸�� �ڵ�
        if first[i % 5] == answers[i]:
            score[0] += 1
        if second[i % 8] == answers[i]:
            score[1] += 1
        if third[i % 10] == answers[i]:
            score[2] += 1

    max_score = max(score) # ���� ���� ������ ����

    for i in range(len(score)):
		# ���� ������ �������� �����Ƿ� ���� ���� ������ �̾� ���Ͽ� �л��� �߰��ߴ�.
        if max_score == score[i]:
            answer.append(i+1)

    return answer

```

�ι�° ���� �ڵ�: ����

����Ʈ�� Ȯ���ϴ� ����� �����ʰ� �ε����� Ȱ���� ����� �����غ��Ҵ�.

���α׷��ӽ����� �׽�Ʈ ���̽��� �����ϸ� ���Ұ�����, �Ƹ��� �� �������� ����Ʈ�� ũ�Ⱑ �ʹ� Ŀ���� ������ ����� �� ���Ҵ�. �������� ������ Ȯ���ϴ� ����� ����ϴ� ���� �ƴ϶� �ε����� Ȱ���� ����� ���� �����غ��߰ڴ�.
