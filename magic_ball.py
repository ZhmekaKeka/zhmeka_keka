import random as rm
import os


answers = [
    "Бесспорно",
    "Предрешено",
    "Никаких сомнений",
    "Определённо да",
    "Можешь быть уверен в этом",
    "Мне кажется - да",
    "Вероятнее всего",
    "Хорошие перспективы",
    "Знаки говорят - да",
    "Да",
    "Пока неясно, попробуй снова",
    "Спроси позже",
    "Лучше не рассказывать",
    "Сейчас нельзя предсказать",
    "Сконцентрируйся и спроси опять",
    "Даже не думай",
    "Мой ответ - нет",
    "По моим данным - нет",
    "Перспективы не очень хорошие",
    "Весьма сомнительно",
]


def is_no(ans):
    if ans in ["нет", "Нет", "НЕТ"]:
        return True


def is_yes(ans):
    if ans in ["да", "Да", "ДА"]:
        return True


def question():
    print("Задайте мне свой вопрос")
    ans = input("Введите вопрос: ")
    print("Мой ответ: {}".format(rm.choice(answers)))
    print()


os.system("cls" if os.name == "nt" else "clear")
print("Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.")
name = input("Как тебя зовут?\nОтвет: ")
print("\nПривет, {}".format(name))
print()
question()
ans = input("Желаете ещё задать вопрос, {}?\nОтвет: ".format(name))

while True:
    if is_yes(ans):
        print()
        question()
        ans = input("Желаете ещё задать вопрос, {}?\nОтвет: ".format(name))
    if is_no(ans):
        print()
        print("Возвращайся, если ещё возникнут вопросы.")
        print("Еще увидимся, {}...".format(name))
        break
    if not (is_yes(ans) or is_no(ans)):
        print()
        print("Не понимаю ваш ответ.")
        ans = input("Желаете ещё задать вопрос, {}?\nОтвет: ".format(name))
