def swap_first_two_digits(N):
    g=0
    temp_N = N
    while temp_N >= 100:
        temp_N //= 10
        g+=1
    first_digit = temp_N // 10
    second_digit = temp_N % 10
    multiplier = 1
    for i in range(g):
        multiplier *= 10
    remaining_part = N % (multiplier * 1)
    new_first_two_digits = second_digit * 10 + first_digit
    result = new_first_two_digits * (multiplier * 1) + remaining_part
    return result
