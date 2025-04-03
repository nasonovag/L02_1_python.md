import random

def guess_the_number():
    secret_number = random.randint(0, 10)
    attempts = 3
    
    print("Я загадал число от 0 до 10. У вас 3 попытки, чтобы угадать его!")

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Попытка {attempt}. Введите число: "))
            
            if guess == secret_number:
                print("Поздравляю! Вы угадали число! 🎉")
                return
            elif guess < secret_number:
                print("Не верно! Загаданное число больше.")
            else:
                print("Не верно! Загаданное число меньше.")
        
        except ValueError:
            print("Пожалуйста, введите целое число.")

    print(f"Вы проиграли! Загаданное число было {secret_number}. 😢")

guess_the_number()