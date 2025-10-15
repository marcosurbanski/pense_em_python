def plus_hifen(f, value):
    f(value)    
   
def print_grid(g):
    print(g, end='')  
    print(g, end='')
    print(g, end='')
    print('+')


def print_grid_pipe(g):
    print(g, end='')
    print(g, end='')
    print(g, end='')
    print('|')

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print('+ - - - - + - - - - +')

def print_post():
    print('|         |         |')

def print_row():
    print_beam()
    do_four(print_post)

def print_grid2():
    do_twice(print_row)
    print_beam()

if __name__ == '__main__':
    #plus_hifen(print_grid, '+', '-', '|')
    plus_hifen(print_grid, '+'+4*'-')
    plus_hifen(print_grid_pipe, '|'+4*' ')
    plus_hifen(print_grid_pipe, '|'+4*' ')
    plus_hifen(print_grid_pipe, '|'+4*' ')
    plus_hifen(print_grid_pipe, '|'+4*' ')
    plus_hifen(print_grid, '+'+4*'-')  
    plus_hifen(print_grid_pipe, '|'+4*' ')
    plus_hifen(print_grid_pipe, '|'+4*' ')
    plus_hifen(print_grid_pipe, '|'+4*' ')
    plus_hifen(print_grid_pipe, '|'+4*' ')
    plus_hifen(print_grid, '+'+4*'-')

    print_grid2()
