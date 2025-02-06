import os

os.system("cls" if os.name == "nt" else "clear")


def code_sym(rot, x, n, d):
    return chr(((x + rot) % n) + d)


def prepare(sym, lang):
    if lang == "en":
        n = 26
        if sym == sym.lower():
            d = ord("a")
            x = ord(sym) - d
        else:
            d = ord("A")
            x = ord(sym) - d
    elif lang == "ru":
        n = 32
        if sym == sym.lower():
            d = ord("а")
            x = ord(sym) - d
        else:
            d = ord("А")
            x = ord(sym) - d
    return x, n, d


def code(text, rot, lang):
    res = ""
    for sym in text:
        if sym.isalpha():
            x, n, d = prepare(sym, lang)
            res += code_sym(rot, x, n, d)
        else:
            res += sym
    return res


way = input("Encode or decode (e или d): ")

lang = input("Choose language (ru/en): ")

rot = int(input("Enter rot (integer): "))

text = input("Enter text: ")

if way == "e":
    new_text = code(text, rot, lang)
elif way == "d":
    new_text = code(text, -rot, lang)
print(new_text)
