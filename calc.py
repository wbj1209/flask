# 곱셉, 덧셈, 4번곱셈 함수 만들기

def calc_square(digit):
    return digit * digit


def calc_plus(digit):
    return digit + digit


def calc_quad(digit):
    return digit * digit * digit * digit


def list_square(func, digit_list):
    result = []
    for digit in digit_list:
        result.append(func(digit))
    return result


num_list = [1, 2, 3, 4, 5]
print(list_square(calc_square, num_list))
print(list_square(calc_plus, num_list))
print(list_square(calc_quad, num_list))
