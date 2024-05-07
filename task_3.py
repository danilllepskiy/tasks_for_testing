def is_prime(n: int) -> bool:
    """
    Данная функция проверяет, является ли число простым.
    """
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def find_primes_in_range(start: int, end: int) -> list[int]:
    """
    Возвращает массив простых чисел в заданном диапазоне
    """
    numbers = list(range(start, end + 1))

    for i in range(len(numbers)):
        if not is_prime(numbers[i]):
            numbers[i] = -1

    primes = [num for num in numbers if num != -1]

    return primes


print(find_primes_in_range(11, 20))
