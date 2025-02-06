from time import time

top = 50
cnt = 0
max_cnt = 30
start = time()

for a in range(1, top + 1):
    if cnt == max_cnt:
        break
    for b in range(a, top + 1):
        if cnt == max_cnt:
            break
        for c in range(a + 1, top + 1):
            if cnt == max_cnt:
                break
            for d in range(c, top + 1):
                if cnt == max_cnt:
                    break
                if a == c or b == d:
                    continue
                a3, b3, c3, d3 = a**3, b**3, c**3, d**3
                if a3 + b3 == c3 + d3:
                    print(
                        str(a)
                        + "**3 + "
                        + str(b)
                        + "**3 = "
                        + str(c)
                        + "**3 + "
                        + str(d)
                        + "**3 = ",
                        a3 + b3,
                    )
                    cnt += 1

finish = time()

print("time: " + str(finish - start) + " sec")
