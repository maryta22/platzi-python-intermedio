def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError("no puede ser vacio")
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False

def run():
    '''
    try:
        print(palindrome(1))
    except TypeError:
        print("Solo se pueden ingresar strings")
    '''
    try:
        print(palindrome(""))
    except TypeError:
        print("Solo se pueden ingresar strings")
    finally:
        print("finally")


if __name__ == '__main__' :
    run()