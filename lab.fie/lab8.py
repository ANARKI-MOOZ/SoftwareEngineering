n = 0
while n < 100:
    print(n)
    if n % 5 == 0:
        n += 3
        continue
    elif n % 2 == 0:
        n += 1
    else:
        n += 2
