def power(base, exponent):
    result = 1
    # Для додатного показника
    if exponent > 0:
        for _ in range(exponent):
            result *= base
    # Для від'ємного показника
    elif exponent < 0:
        for _ in range(abs(exponent)):
            result /= base
    # Якщо показник дорівнює 0, результат завжди 1
    return result

# Приклад використання функції:
base = 2
exponent = 3
print(power(base, exponent))  # Виведе 8
