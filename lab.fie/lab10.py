array = [2, 4, 6, 8, 9]
flag = False
for value in array:
    if value % 2 == 1:
        flag = True

if flag is True:
    print("есть")
else:
    print("нету")
