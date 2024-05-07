def find_common_divisors(nums: list[int]) -> list[int]:
    """
    Возвращает массив общих делителей для всех чисел в  заданном массиве.
    """
    common_divisors = set()

    min_num = min(nums)

    for i in range(1, min_num + 1):
        is_common_divisor = True
        for num in nums:
            if num % i != 0:
                is_common_divisor = False
                break

        if is_common_divisor:
            common_divisors.add(i)

    return list(common_divisors)

# nums = [42, 12, 18]
# print(find_common_divisors(nums))
