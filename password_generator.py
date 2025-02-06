import random as rm
import os

os.system("cls" if os.name == "nt" else "clear")


def generate_password(chars, length):
    arr = list(chars)
    rm.shuffle(arr)
    password = "".join(rm.choices(arr, k=length))
    return password


digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = lowercase_letters.upper()
punctuation = "!#$%&*+-=?@^_"
excepting_symbols = "il1Lo0O"

chars = ""

n = int(input("Количество паролей для генерации (целое число): "))
l = int(input("Длина паролей (целое число): "))
use_digits = int(input("Включать ли цифры? (1 - да, 0 - нет): "))
use_ul = int(input("Включать ли прописные EN-буквы? (1 - да, 0 - нет): "))
use_ll = int(input("Включать ли строчные EN-буквы? (1 - да, 0 - нет): "))
use_punc = int(input('Включать ли символы "!#$%&*+-=?@^_?" (1 - да, 0 - нет): '))
excepts = int(
    input('Исключать ли неоднозначные символы "il1Lo0O"? (1 - да, 0 - нет): ')
)


if use_digits == 1:
    chars += digits
if use_ul == 1:
    chars += uppercase_letters
if use_ll == 1:
    chars += lowercase_letters
if use_punc == 1:
    chars += punctuation
if excepts == 1:
    for sym in excepting_symbols:
        if sym in chars:
            chars = chars.replace(sym, "")


if chars != "":
    for _ in range(n):
        print(generate_password(chars, l))
else:
    print("Множество символов для генерации пусто")
