def prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True

k = int(input())
lst = []
for i in range(1, k + 1):
    if deliteli(i) == True:
        lst.append(i)
print(lst)