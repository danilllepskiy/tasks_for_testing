from random import randint


def find_breaking_height(breaking_point: int) -> int:
    min_height = 1
    max_height = 5000
    experiments = 0

    while min_height < max_height:
        mid_height = (min_height + max_height) // 2
        experiments += 1

        # Сбрасываем предмет с середины текущего диапазона
        # breaking_point - это высота, начиная с которой предмет разрушается

        if mid_height >= breaking_point:
            max_height = mid_height
        else:
            min_height = mid_height + 1

    return experiments


breaking_point = randint(1, 5000)
experiments_needed = find_breaking_height(breaking_point)
print(
    f"Ученым потребуется максимум {experiments_needed} экспериментов "
    f"для определения высоты, начиная с которой предметы разбиваются.")
