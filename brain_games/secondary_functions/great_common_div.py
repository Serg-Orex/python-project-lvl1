def get_great_common_div(a, b):
    if a > b:
        c = b
    else:
        c = a
    d = 1
    while d <= c:
        if b % d == 0 and a % d == 0:
            gcd = d
            d += 1
        else:
            d += 1
    return gcd
