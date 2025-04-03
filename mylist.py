# 1. Создание списка из 5 чисел и вывод их суммы
numbers = [10, 20, 30, 40, 50]
sum_numbers = sum(numbers)
print(f"Сумма чисел в списке: {sum_numbers}")

# 2. Нахождение максимального числа в списке
max_number = max(numbers)
print(f"Максимальное число в списке: {max_number}")

# 3. Удаление дубликатов из списка
numbers_with_duplicates = [1, 2, 3, 4, 2, 3, 5, 6, 5, 7]
unique_numbers = list(set(numbers_with_duplicates))
print(f"Список без дубликатов: {unique_numbers}")