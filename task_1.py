def get_computers_str(number: int) -> str:

    last_digit = number % 10
    last_two_digits = number % 100

    word_endings = ["компьютер", "компьютера", "компьютеров"]

    if last_digit == 1 and last_two_digits != 11:
        word_ending = word_endings[0]
    elif 2 <= last_digit <= 4 and (last_two_digits < 10 or last_two_digits > 20):
        word_ending = word_endings[1]
    else:
        word_ending = word_endings[2]
    return f"{number} {word_ending}"
