def summa(n):
    if n < 0:
        return "Error"
    if n == 0:
        return 0
    return n + summa(n - 1)


def fibonachee_recursion (n):
    if 1 >= n >= 0:
        return n
    elif n >= 2:
        return fibonachee_recursion(n-1) + fibonachee_recursion(n-2)
    elif n < 0:
         return "Error"


def fibonachee(n):
    f = 0
    s = 1
    while n != 0:
        k = f
        f = s + f
        s = k
        n = n - 1
    return s


print(fibonachee(7))
print(fibonachee_recursion(7))
