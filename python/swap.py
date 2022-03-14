def swapNum(num1, num2):
    if int(num1) > int(num2):
        temp = num1
        num1 = num2
        num2 = temp
    return(num1, num2)

def test_swapNum():
    num1 = input("Input age 1: ")
    num2 = input("Input age 2: ")
    num1, num2 = swapNum(num1, num2)
    print("Swapped:", num1, num2)


if __name__ == "__main__":
    test_swapNum()