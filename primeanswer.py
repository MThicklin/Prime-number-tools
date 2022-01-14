n = 0
for a in range(999, 100, -1):
    for b in range(a, 100, -1):
        x = a * b
        print("A is currently: " + str(a))
        if x > n:
            s = str(a * b)
            if s == s[::-1]:
                n = a * b
                print("N is currently: " + str(n))
print(n)