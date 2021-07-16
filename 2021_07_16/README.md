```python
def solution(scoville, K):
    answer = 0
    scoville.sort()

    for i in range(scoville):
        if len(scoville) == 1:
            return -1

        combine_food = scoville.pop(0) + (scoville.pop(1)*2)
        for j in range(scoville):
            if scoville[j] <= combine_food:
                scoville.insert(j+1, combine_food)
                answer += 1

        if scoville[0] >= K:
            break

    return answer
```

첫번째 제출 코드: 에러(TypeError: 'list' object cannot be interpreted as an integer)

range(scoville)하는데 len함수를 안 넣어줘서 오류가 난거였음

사소한 실수도 조심하자

```python
def solution(scoville, K):
    answer = 0
    scoville.sort()

    for i in range(len(scoville)):
        if len(scoville) == 1:
            return -1

        combine_food = scoville.pop(0) + (scoville.pop(1)*2)
        for j in range(len(scoville)):
            if scoville[j] <= combine_food:
                scoville.insert(j+1, combine_food)
                answer += 1

        if scoville[0] >= K:
            break

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))
```

두번째: 오답

pop을 하면 바로 빈칸은 채워진다는 것을 잊지말자

```python
def solution(scoville, K):
    answer = 0
    scoville.sort()

    for i in range(len(scoville)):
        if len(scoville) == 1:
            return -1

        combine_food = scoville.pop(0) + (scoville.pop(0)*2)
        for j in range(len(scoville)):
            if scoville[j] <= combine_food:
                scoville.insert(j+1, combine_food)
                answer += 1
								##여기 브레이크를 넣어줘야함
        if scoville[0] >= K:
            break

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))
```

세번쨰: 오답

```python
def solution(scoville, K):
    answer = 0
    scoville.sort()

    for i in range(len(scoville)):
        if len(scoville) == 1:
            return -1

        combine_food = scoville.pop(0) + (scoville.pop(0)*2)
        for j in range(len(scoville)):
            if scoville[j] <= combine_food:
                scoville.insert(j+1, combine_food)
                answer += 1
                break

        if scoville[0] >= K:
            break

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))
```

네번째: 답은 맞았지만 시간초과

이중 포문이 원인인것같음

```python
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    for i in range(len(scoville)):
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        combined_food = first + (second * 2)
        answer += 1
        heapq.heappush(scoville, combined_food)

        if scoville[0] > K:
            break

        if len(scoville) == 1:
            return -1

    return answer
```

다섯번째: 정답

같은 사람이 짠게 맞나 싶을 정도다.

기본 라이브러리에 대해 조금 더 공부할 필요가 있는 것 같다.
