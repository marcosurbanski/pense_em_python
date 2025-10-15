def right_justify(s):
    num_espacos = 70 - len(s)
    print(' ' * num_espacos + s)

    
if __name__ == '__main__':
    right_justify('monty')