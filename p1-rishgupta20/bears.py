# int -> booelan
# Given integer n, returns True or False based on reachabilty of goal
def bears(n):
    if n < 42:
        return False
    if n >= 42:
        if n == 42:
            return True
        if n % 2 == 0:
            if bears(n - n // 2) is True:
                return True
        if n % 3 == 0 or n % 4 == 0:
            n1 = str(n)
            if n != n - int(n1[len(n1) - 1]) * int(n1[len(n1) - 2]):
                if bears(n - int(n1[len(n1) - 1]) * int(n1[len(n1) - 2])) is True:
                    return True
        if n % 5 == 0:
            if bears(n - 42) is True:
                return True
    return False
