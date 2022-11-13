from random import sample


def get_random_password(n=8) -> str:
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'  # TODO написать функцию генерации случайных паролей
    return ''.join(sample(alphabet, n))


n = 15
print(get_random_password(n))
