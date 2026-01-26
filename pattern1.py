# Number of rows for the top half
n = 5

# Top half (increasing)
for i in range(1, n + 1):
    print("* " * i)

# Bottom half (decreasing)
for i in range(n - 1, 0, -1):
    print("* " * i)
