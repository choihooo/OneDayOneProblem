def solution(strings, n):
    answer = []
    answer = sorted(strings, key=lambda x: (x[n], x))  # 람다로 여러가지 조건줘서 정렬하기

    return answer


print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))
