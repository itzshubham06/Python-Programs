n = 5
symbols = ["*", "#"]

for i in range(1, n + 1):
    for j in range(i):
        print(symbols[j % 2], end=" ")
    print()
