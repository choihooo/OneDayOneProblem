def solution(citations):
    citations = sorted(citations)
    size = len(citations)

    for i in range(size):
        if citations[i] >= size-i:
            return size-i

    return 0


print(solution([3, 0, 6, 1, 5]))
