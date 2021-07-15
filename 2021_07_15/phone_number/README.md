Programmers PhoneNumber Level 2

language: python

Link: [https://programmers.co.kr/learn/courses/30/lessons/42577](https://programmers.co.kr/learn/courses/30/lessons/42577)

```python
def solution(phone_book):
    answer = True
    leng = []
    for i in phone_book:
        leng.append(len(i))

    min_leng = min(leng)

    for i in range(len(phone_book)):
        if leng[i] == min_leng:
            for j in range(len(phone_book)):
                if i!=j:
                    if phone_book[i] in phone_book[j]:
                        answer = False

    return answer
```

첫번째 제출 코드: 테스트1, 5, 13, 19, 효율성3, 4

phone_book = sorted(phone_book, key = lambda x : len(x))

```python
def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)

    for i in range(1,len(phone_book)):
        if phone_book[i-1] in phone_book[i]:
            answer = False


    return answer
```

세번째 제출 코드: 테스트 13

깜빡하고 두번째 코드를 그냥 지워버렸다.

정렬 하는 방법을 생각해보니까 훨씬 쉬워졌다.

이 코드는 똑같은 숫자가 뒤에 있어도 False로 바뀌기 때문이다.

```python
def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)

    for i in range(1,len(phone_book)):
        if phone_book[i-1] in phone_book[i][:len(phone_book)+1]:
            answer = False

    return answer
```

네번째 제출 코드: 정답
