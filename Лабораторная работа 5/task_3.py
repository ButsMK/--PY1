from random import randint


def get_unique_list_numbers(low: int, high: int, n: int) -> list[int]:
    out = []
    while len(out) != n:  # TODO написать функцию для получения списка уникальных целых чисел
        num = randint(low, high)
        if num not in out:
            out.append(num)
    return out


low = -10
high = 10
n = 15
list_unique_numbers = get_unique_list_numbers(low, high, n)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
