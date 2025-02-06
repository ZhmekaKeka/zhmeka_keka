from time import time

start = time()  # начало подсчета времени

found = False
for a in range(2, 151):
    if found:
        break
    for b in range(a, 151):
        for c in range(b, 151):
            for d in range(c, 151):
                e5 = a**5 + b**5 + c**5 + d**5
                if e5 == int(e5**0.2) ** 5:
                    print(a, b, c, d, int(e5**0.2))
                    print("Сумма:", a + b + c + d + int(e5**0.2))
                    found = True

finish = time()  # конец подсчета времени
print("Время работы (сек):", finish - start)
