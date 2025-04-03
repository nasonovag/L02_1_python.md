# 1. Создание словаря с информацией о студенте и вывод данных
student = {
    "Имя": "Иван",
    "Возраст": 20,
    "Курс": 3
}

print("Информация о студенте:")
for key, value in student.items():
    print(f"{key}: {value}")

print("\n")

# 2. Объединение двух словарей в один
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"d": 4, "e": 5, "f": 6}

merged_dict = {**dict1, **dict2}
print("Объединенный словарь:", merged_dict)

print("\n")

# 3. Проверка наличия ключа в словаре
key_to_check = input("Введите ключ для проверки: ")

if key_to_check in merged_dict:
    print(f"Ключ '{key_to_check}' найден в словаре! Значение: {merged_dict[key_to_check]}")
else:
    print(f"Ключ '{key_to_check}' отсутствует в словаре.")