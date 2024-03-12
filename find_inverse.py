#find inverse using extended euclidean algorithm
def find_inverse(a, m):
    if m == 1:
        return 0
    m0 = m
    y = 0
    x = 1
    while a > 1:
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    if x < 0:
        x = x + m0
    return x