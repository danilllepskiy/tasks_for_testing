def print_multiplication_table(n: int):
    """
    Выводит таблицу умножения до заданного числа.
    """
    print("  ", end="")
    for i in range(1, n + 1):
        print(f"{i:>3}", end="")
    print()

    for i in range(1, n + 1):
        print(f"{i:>2}", end="")

        for j in range(1, n + 1):
            print(f"{i * j:>3}", end="")
        print()

# print_multiplication_table(9)
