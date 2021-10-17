'''
def outer_func(func):
    def inner_func(digit1, digit2):
        if digit2 == 0:
            print('cannot')
            return
        func(digit1, digit2)
    return inner_func


@outer_func
def divide(digit1, digit2):
    return print(digit1 / digit2)


divide(3, 2)
'''

'''
def general_decorator(func):
    def wrapper(*args, **kwargs):
        print('야호')
        return func(*args, **kwargs)
    return wrapper


@general_decorator
def calc_square(digit):
    return digit * digit


@general_decorator
def calc_quad(digit1, digit2, digit3, digit4):
    return digit1 * digit2 * digit3 * digit4


print(calc_square(3))
print(calc_quad(1, 2, 3, 4))
'''

'''
def mark_bold(func):
    def wrapper(*args, **kwargs):
        return '<b>' + func(*args, **kwargs) + '</b>'
    return wrapper


def mark_italic(func):
    def wrapper(*args, **kwargs):
        return '<i>' + func(*args, **kwargs) + '</i>'
    return wrapper


@mark_bold
@mark_italic
def add_html(str):
    return str


print(add_html('안녕'))
'''


def mark_html(tag):
    def outer_wrapper(function):
        def inner_wrapper(*args, **kwargs):
            return '<' + tag + '>' + function(*args, **kwargs) + '</' + tag + '>'
        return inner_wrapper
    return outer_wrapper


@mark_html('b')
def print_bold(title):
    return title


@mark_html('h1')
def print_title(title):
    return title


print(print_title('야호'))
