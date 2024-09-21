n = 5

for i in range(1, n + 1):
    for _ in range(n - i):
        print(" ", end="")
    for j in range(i, 0, -1):
        print(j, end="")
    print()

for i in range(n, 0, -1):
    print("    ", end="")
    for j in range(i, 0, -1):
        print(j, end="")
    print()
    