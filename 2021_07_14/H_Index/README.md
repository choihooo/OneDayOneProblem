# H_index

Programmers H_index Level 2
language: python
Link: https://programmers.co.kr/learn/courses/30/lessons/42747

```python
def solution(citations):
    size = len(citations)
    sort_citations = sorted(citations)

    for i in range(size-1, -1, -1):
        if sort_citations[i] < i:
            break

    return i
```

첫번째 코드: 문제를 잘못이해해서 답이 다 틀렸다.

```python
def solution(citations):
    citations = sorted(citations)
    size = len(citations)

    for i in range(size):
        if citations[i] >= size-i:
            return size-i

    return 0
```

두번째 코드:h-index에 대해서 찾아보고 다시 풀어봤더니 정답이였다.

이로써 프로그래머스에서 정렬 문제 뽑아논 건 다 풀었다.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2123ffa6-0302-415e-8cd9-e39fdb269788/zxczxc.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2123ffa6-0302-415e-8cd9-e39fdb269788/zxczxc.png)
