
'''

1
input number from the user --  88949
print the number in reverse -- 94988
print the biggest digit -- 9
print how many times the biggest digit appears? -- 2
print the min digit -- 4
print the sum of digits -- 38
print the avg of digits -- 8+8+9+4+9 / 5

2
write a function that gets a list of numbers and returns if the list is sorted or not

3
write a function that gets a list of numbers (with duplication), n-th biggest and returns it
i.e. [88, 100, 90, 95, 95, 97, 97, 99, 97, 99] , 4 --> will return 95 (because it is the 4-th biggest after 100, 99, 97, 95)
'''

def num() -> int:
    while True:
        number = input("please enter a number: ")
        if number.isdigit():
            return int(number)
        else:
            print("please enter a number")
            continue

def rev_max_appear(_user_number):
    _user_number_list = _user_number.split()
    print(_user_number_list)
    print(_user_number_list[reverse=True)
    _max = max(_user_number_list)
    print(_max)
    _count = _user_number.count(max)
    print(_count)
    return _rev, _max, _count



_user_number = num()
rev_max_appear(_user_number