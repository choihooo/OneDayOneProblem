def solution(n):
    answer = 0
    n_list = list(str(n))
    n_list.sort(reverse=True)
    n_str = ''.join(n_list)
    answer = int(n_str)
    return answer


print(solution(118372))
