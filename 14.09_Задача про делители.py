def deliteli(n: int) -> list:
    #function, which count and return the list of dividers of n
    lst = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            lst.append(i)
            if i != n // i:
                lst.append(n // i)
    return sorted(lst)[::-1]

#checking type of input a, b
while True:
    a, b = input(), input()
    if a.isdigit() == True and b.isdigit() == True:
        a, b = int(a), int(b)
        for i in range(a, b + 1):
            if len(deliteli(i)) == 4:
                print(i)
                print(*deliteli(i))
                print()
    else:
        print('Вы ошиблись с типом данных. Пожалуйста, введите данные еще раз')
