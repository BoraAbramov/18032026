

def four_unique_digit(num_list, n):
    '''

    :param num_list: list of numbers
    :param n: number in the list
    :return: index of unique number
    '''
    num_list = set(num_list)
    num_list = list(num_list)
    num_list.sort(reverse=True)

    if n in num_list:
        _index = num_list.index(n)
        _index += 1
        return _index
    else:
        print(f"{n} not in the list")
        return None




numbers = [88, 100, 90, 95, 95, 97, 97, 99, 97, 99]

n = int(input("please enter a number and I return you index"))

_calaulation = four_unique_digit(numbers, n)

print(_calaulation)