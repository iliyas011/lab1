t = int(input())

if t <= 0:
    print()
else:
    a, b = 0, 1
    for _ in range(t):
        print(a)
        a, b = b, a + b
