# Простой калькулятор
def calculator():
    try:
        expression = input("Введите выражение (например, 2 + 2): ")
        result = eval(expression)
        print(f"Результат: {result}")
    except Exception as e:
        print(f"Ошибка: {e}")

calculator()