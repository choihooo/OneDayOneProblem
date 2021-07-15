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

ù��° �ڵ�: ������ �߸������ؼ� ���� �� Ʋ�ȴ�.

```python
def solution(citations):
    citations = sorted(citations)
    size = len(citations)

    for i in range(size):
        if citations[i] >= size-i:
            return size-i

    return 0
```

�ι�° �ڵ�:h-index�� ���ؼ� ã�ƺ��� �ٽ� Ǯ��ô��� �����̿���.

�̷ν� ���α׷��ӽ����� ���� ���� �̾Ƴ� �� �� Ǯ����.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2123ffa6-0302-415e-8cd9-e39fdb269788/zxczxc.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2123ffa6-0302-415e-8cd9-e39fdb269788/zxczxc.png)
