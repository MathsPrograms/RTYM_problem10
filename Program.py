def item1a(num):
    k = False
    for numadd in range(10):
        if (10 * num + numadd) % 2024 == 0:
            k = True
            print("Можно приписать цифру ", numadd, " и получить число ", 10*num+numadd, ", которое делится на 2024")
    if k == False:
        print("Такой цифры не существует")
def item1b():
    k = 0
    for num in range(100, 1000):
        for numadd in range(10):
            if (10 * num + numadd) % 2024 == 0:
                k += 1
    print("Всего таких чисел ", k)
def item1c(numOfnumadd):
    t = True
    for num in range(100, 1000):
        k = False
        for numadd in range(10^numOfnumadd):
            if (num * (10^numOfnumadd) + numadd) % 2024 == 0:
                k = True
        if k == False:
            t = False
    if t == True:
        print("Всегда найдутся ", numOfnumadd, " цифр, которые можно приписать в конце, чтобы полученное число делилось на 2024")
        return True
    else:
        print(numOfnumadd, " цифр недостаточно")
        return False
def item2(divider):
    t = True
    for num in range(100, 1000):
        k = False
        for numadd1 in range(10):
            for numadd2 in range(10):
                if (num * 10 + numadd1 + numadd2 * 10000) % divider == 0:
                    k = True
        if k == False:
            t = False
    if t == True:
        print("Всегда найдутся 2 цифры, которые можно приписать в конце и в начале, чтобы полученное число делилось на ", divider)
    else:
        print("Не всегда найдутся 2 цифры, которые можно приписать в конце и в начале, чтобы полученное число делилось на ", divider)
def item3a(divider):
    t = True
    for num in range(100, 1000):
        k = False
        for numadd1 in range(10):
            for numadd2 in range(10):
                for numadd3 in range(10):
                    numsplit = str(num).split
                    if (int(str(numadd1) + numsplit[0] + numsplit[1] + str(numadd2) + numsplit[2] + str(numadd3))) % divider == 0:
                        k = True
                    if (int(str(numadd1) + numsplit[0] + str(numadd2) + numsplit[1] + numsplit[2] + str(numadd3))) % divider == 0:
                        k = True
        if k == False:
            t = False
    if t == True:
        return True
    else:
        return False
def item3b(divider):
    t = True
    for num in range(100, 1000):
        k = False
        for numadd1 in range(10):
            for numadd2 in range(10):
                for numadd3 in range(10):
                    for numadd4 in range(10):
                        numsplit = str(num).split
                        if (int(str(numadd1) + numsplit[0] + str(numadd2) + numsplit[1] + str(numadd3) + numsplit[2] + str(numadd4))) % divider == 0:
                            k = True
        if k == False:
            t = False
    if t == True:
        return True
    else:
        return False
def item3c():
    divisors2024 = [1, 2, 4, 8, 11, 22, 23, 44, 46, 88, 92, 184, 253, 506, 1012, 2024]
    n = 16
    if item3a(divisors2024[2024]) == False:
        while item3a(divisors2024[n]) == False:
            n += -1
        print("Ответ: ", divisors2024[n])
    if item3b(divisors2024[2024]) == False:
        while item3b(divisors2024[n]) == False:
            n += -1
        print("Ответ: ", divisors2024[n])
def item4(divider):
    t = False
    for num in range(100, 1000):
        k = False
        for numadd1 in range(10):
            for numadd2 in range(1, 10):
                if (num * 10 + numadd1 + numadd2 * 10000) % divider == 0:
                    k = True
        if k == False:
            t = True
    if t == True:
        return True
    else:
        return False
def primecheck(num):
    divisors = 0
    for div in range(1, num + 1):
        if (num % div) == 0:
            divisors += 1
    if divisors == 2:
        return True
    else:
        return False
while True:
    input1 = input("Выбирете пункт задачи 10: 1а, 1б, 1в, 2а, 2б, 2в, 3а, 3б, 3в, 4а, 4б. Чтобы выйти напишите END")
    if input1 == "END":
        break
    if input1 == "1а":
        item1a(202)
    if input1 == "1б":
        item1b()
    if input1 == "1в":
        k = 1
        while item1c(k):
            k += 1
    if input1 == "2a":
        item2(72)
    if input1 == "2б":
        item2(44)
    if input1 == "2в":
        item2(23)
    if input1 == "3а":
        if item3a(2024) == True:
            print("Ответ: Да")
        else:
            print("Ответ: Нет")
    if input1 == "3б":
        if item3b(2024) == True:
            print("Ответ: Да")
        else:
            print("Ответ: Нет")
    if input1 == "3в":
        item3c()
    if input1 == "4а":
        numbers = []
        for num in range(1, 51):
            if item4(num):
                numbers.append(num)
        print(numbers)
    if input1 == "4б":
        num = 2
        while not item4(num) or not primecheck(num):
            num += 1
        print(num)
        input()