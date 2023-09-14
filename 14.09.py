def deliteli(n: int) -> list:
    lst = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            lst.append(i)
            if i != n // i:
                lst.append(n // i)
    return sorted(lst)

a = int(input())
b = int(input())
for i in range(a, b + 1):
    if len(deliteli(i)) == 4:
        print(i)
        print(*deliteli(i))
        print()