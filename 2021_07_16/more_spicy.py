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
