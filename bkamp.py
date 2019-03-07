

def convert(n, lst):
    s = ''
    while True:
        s = lst[n % len(lst)] + s
        if n < len(lst):
            break
        n = n // len(lst) - 1
    return s


def arrayChoice(n):
    if n == 1 || n == "short" || n == "s":
        array = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i"]


