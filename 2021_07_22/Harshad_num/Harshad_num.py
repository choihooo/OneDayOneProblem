def solution(x):
    num_list = list(map(int, str(x)))
    sum_of_digits = 0
    for i in range(len(num_list)):
        sum_of_digits += num_list[i]

    if x % sum_of_digits == 0:
        return True
    else:
        return False
    