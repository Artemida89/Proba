def cheslo(x):

    print("#", x, end=" ")


namber_1 = int(input("Ввесть число №1: "))
namber_2 = int(input("Ввесть число №2: "))
a = 1
all_sum = 0

if namber_1 > 0:
    while namber_1 != 0:
        namber_2 = namber_1 ** 2 + namber_2 ** 2
        namber_1 -= 1
        all_sum += namber_2
        x = all_sum
        cheslo(x)
elif namber_1 < 0:
    while namber_1 != 0:
        namber_2 = namber_1 + namber_2
        namber_1 += 1
        all_sum = all_sum + namber_2
        x = all_sum
        cheslo(x)
