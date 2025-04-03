# 1. Вывод всех чисел от 1 до 10 с использованием цикла for
print("Числа от 1 до 10:")
for i in range(1, 11):
    print(i, end=" ")
print("\n")

# 2. Вывод всех чисел от 1 до N, где N вводит пользователь
N = int(input("Введите число N: "))
print(f"Числа от 1 до {N}:")
for i in range(1, N + 1):
    print(i, end=" ")
print("\n")

# 3. Вычисление суммы всех чисел от 1 до 100 с использованием цикла while
sum_numbers = 0
counter = 1

while counter <= 100:
    sum_numbers += counter
    counter += 1

print(f"Сумма чисел от 1 до 100: {sum_numbers}")