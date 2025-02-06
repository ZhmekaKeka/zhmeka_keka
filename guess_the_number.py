import random as rm
import os


def is_no(ans):
    if ans in ["нет", "Нет", "НЕТ"]:
        return True


def is_yes(ans):
    if ans in ["да", "Да", "ДА"]:
        return True


def is_valid(ans):
    while True:
        if ans.isdigit() and 1 <= int(ans) <= 100:
            return int(ans)
        else:
            print("Вне диапазона или не является целым числом.")
            ans = input("Введите число:")


def batch():
    print("Загадано число от 1 до 100.")
    num = rm.randint(1, 100)
    ans = is_valid(input("Введите число: "))
    print()
    tries = 1
    while True:
        if ans < num:
            print("Слишком мало, попробуйте еще раз")
            ans = is_valid(input("Введите число: "))
            print()
            tries += 1
        elif ans > num:
            print("Слишком много, попробуйте еще раз")
            ans = is_valid(input("Введите число: "))
            print()
            tries += 1
        elif ans == num:
            print("Вы угадали, поздравляем!")
            print("Потребовалось попыток: {}".format(tries))
            print()
            break


def print_start():
    os.system("cls" if os.name == "nt" else "clear")
    print("Добро пожаловать в числовую угадайку!")
    print()


print_start()
batches = 1
batch()
ans = input("Желаете продолжить ещё?\nОтвет: ")

while True:
    if is_yes(ans):
        batches += 1
        os.system("cls" if os.name == "nt" else "clear")
        batch()
        ans = input("Желаете продолжить ещё?\nОтвет: ")
    if is_no(ans):
        print()
        print("Спасибо, что играли в числовую угадайку.")
        print("Сыграно партий: {}".format(batches))
        print("Еще увидимся...")
        break
    if not (is_yes(ans) or is_no(ans)):
        print()
        print("Не понимаю ваш ответ.")
        ans = input("Желаете продолжить ещё?\nОтвет: ")
