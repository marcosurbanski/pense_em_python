def do_twice(f, value):
    f(value)
    f(value)
    
def print_twice(s):
    print(s)
    print(s)

def do_four(f, value):
    do_twice(f, value)
    do_twice(f, value)


if __name__ == '__main__':

    do_twice(print_twice, 'spam')

    do_four(print_twice, 'do_four_spam')