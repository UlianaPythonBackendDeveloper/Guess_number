# Импотрируем библиотеку random
import random
print("--------------------------------------------------------")
print("Добро пожаловать в игру угадай число!")
# Создаем функцию угадай число 
def guess_number():
    # Создаем переменную Answer, которая будет перебирать массив от 0 до 100
    Answer = random.randint(0,100)
    max_attempts = 3
    attempts = 0
    # Создаем бесконечный цикл
    while attempts < max_attempts:
        attempts += 1
        print(f"\n Попытка {attempts}из max_attempts")
        # пользователь вводит число 
        user_guess = int(input("Каковы ваши предположения?"))
        # если загаданное число угадано , то выводится правильно
        if user_guess == Answer:
            print(f"Правильно! Ответ: {user_guess}")
            print(f"Вы угадали с {attempts}-й попытки")
            break
        
        if user_guess < Answer:
            print(f"Ваше число {user_guess} слишком маленькое!")
        else:
            print(f"Ваше число {user_guess} слишком большое!")



guess_number()
print("Спасибо за игру! Жду вас снова!")
print("-------------------------------------------------------------------")