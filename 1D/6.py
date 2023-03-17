import math

for a in range(1, 1001):
    for b in range(1, 1001):
        c = math.sqrt(a**2 + b**2)
        if c == int(c):
            print("({}, {}, {})".format(a, b, int(c)))
