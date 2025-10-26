def prim_peste_x(n):
    ok = True
    if n == 0:
        ok = False
    if n == 1:
        ok = False
    else:
        for i in range(2, n//2+1):
            if n % i == 0:
                ok = False
                break
    return ok


def next_prime(n):
    n += 1
    while prim_peste_x(n) is False:
        n += 1
    return n


print(next_prime(1000))
