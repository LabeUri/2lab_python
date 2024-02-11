def factorial(n):
    result = 1
    # Перевірка чи число n є невід'ємним цілим
    if n < 0:
        return "Факторіал визначений тільки для невід'ємних цілих чисел"
    elif n == 0:
        return 1
    else:
        for i in range(1, n + 1):
            result *= i
        return result

# Приклад використання функції:
number = 5
print("Факторіал числа", number, "дорівнює", factorial(number))  # Виведе 120
