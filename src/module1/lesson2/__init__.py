def max(a, b, c):
    if a > c and a > b:
        return a
    elif b > c:
        return b
    else:
        return c


arg1 = 6
arg2 = 5
arg3 = 4
j = max(arg1, arg2, arg3)
print(j)
