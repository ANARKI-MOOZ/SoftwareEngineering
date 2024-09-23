n = int(input())
if 0 <= n <= 3:
    print(" n >= 0 и n <= 3")
elif 3 < n < 6:
    print("n > 3 и n < 6")
elif 6 <= n <= 10:
    print(" n >= 6 и n <= 10")
else:
    print("число должно быть в диапазоне от 0 до 10")
