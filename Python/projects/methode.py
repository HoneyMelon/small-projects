def methode(a, b, c):
    x = 0
    if a < 3 and b < 3:
        x = 3
    else:
        while c > 3:
            x -= c
            c -= 1
        if a == b:
            x = x // a
    return x


c0 = [(0, 0, 0), (3, 3, 0)]
c1 = [(0, 0, 0), (3, 3, 0), (0, 1, 0)]
c2c = [(3, 3, 4), (3, 3, 4), (3, 4, 4), (0, 0, 0), (3, 3, 0)]
c3b = [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]