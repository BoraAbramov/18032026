from hmac import new


def input_size() -> int:
    while True:
        triangel_size = input("please enter a number: ")
        if triangel_size.isdigit():
            return int(triangel_size)
        else:
            print("please enter a number")
            continue

def Tprint(_size):
    for i in range(1, _size + 1):
        print(i)
        for j in range(i + 1, 1, 1):
            print(j, end=" ")



while True:
    _size = input_size()
    Tprint(_size)
    break

