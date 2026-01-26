num = 2
rows = 4

for i in range(1, rows + 1):
    for j in range(i):
        print(num, end=" ")
        num += 2
    print()
