#(2°C × 9/5) + 32 = 35.6°F
def cel2fah():
    dogin = int(input("hello a? "))
    num2 = (dogin  * 9/5) + 32
    print(num2)
    return
cel2fah(5)


def fah2cel():
    catin = int(input("what num u want?"))
    num3 = (catin - 32) * 5/9
    print(num3)
    return
fah2cel()