numbers = [34, 15, 23, 3, 65, 32, 100, 77]
n = int(input("число: "))
if n in numbers:
    if n % 2 == 0:
        print("есть и четная")
    else:
        print("есть и нечетная")
else:
    print(f"переменной {n} нет")
