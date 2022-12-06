# int, int -> string
# Given integer num and base b, converts num to a string representation in base b
def convert(num, b):
    if num // b == 0:
        if num % b >= 10:
            return str(chr(55 + (num % b)))
        else:
            return str(num)
    string1 = ''
    if num // b != 0:
        remain = num % b
        if remain > 9:
            remain += 55
            remain = chr(remain)
        string1 += str(convert((num // b), b)) + str(remain)
        return string1
