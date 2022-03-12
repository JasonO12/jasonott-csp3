def swapNum(x, y):
    if x > y:
        temp = x
        x = y
        y = temp
    print(x, y)

def test_swapNum():
    num1 = int(input("input age 1: "))
    num2 = int(input("input age 2: "))
    x, y = swapNum(num1, num2)
    print(x, y)
