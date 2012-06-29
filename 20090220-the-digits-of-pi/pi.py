import sys

def spigot(digit):
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    while digit > 0:
        if 4 * q + r - t < n * t:
            digit -= 1
            yield n
            q, r, n = 10 * q, 10 * (r - n * t), (10 * (3 * q + r)) // t - 10 * n
        else:
            q, r, t, k, n, l = q * k, (2 * q + r) * l, t * l, k + 1, (q * (7 * k + 2) + r * l) // (t * l), l + 2

for i, d in enumerate(spigot(1001)):
    # sys.stdout.write(str(d))
    if i == 0:
        assert d == 3
    elif i == 1000:
        assert d == 9
