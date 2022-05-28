import math 
from functools import reduce


def run():
    my_list = [1, "Hello", 4.5]
    my_dict = {"firstname": "maria", "apellido": "rivera"}


    super_list = [
        {"firstname": "Facundo", "lastname": "García"},
        {"firstname": "Miguel", "lastname": "Rodriguez"},
        {"firstname": "Pablo", "lastname": "Trinidad"},
        {"firstname": "Susana", "lastname": "Martinez"},
        {"firstname": "José", "lastname": "Fernandez"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 3, 0, 1],
        "floating_nums": [1.1, 4.55, 6.43],
    }


    '''for key, value in super_dict.items():
        print(key, " ", value)'''



    #Crear una lista de los 100 primeros números al cuadrado
    #También que no sean divisibles entre tres

    nums = []

    '''
    for i in range(1, 101):
        if i % 3 != 0:
            nums.append(i**2)
    
    print(nums)
    '''

    '''print([ i**2 for i in range(1, 101) if i % 3 != 0 ])'''


    #Crear con un list comphrension, una lista de todos los múltiplos de 4 que son a la vez múltiplos de 6 y 9 hasta 5 dígitos

    '''print( [i for i in range(1, 99999) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0])'''

    #Crear un diccionario llaves = 100 primeros números naturales valores = la llave al cubo

    '''print({i: i**3 for i in range(1, 101)})'''

    #Crear un diccionario con los 1000 primero numeros clave = numero valor = raiz cuadrada

    '''print({i: math.sqrt(i) for i in range(1, 999)})'''

    #

    num = [1,2,3,45,64,45,6,5423,435,345,345,22]

    print(list(map(lambda x : x**2, num)))
    print(list(filter(lambda x : x%2 != 0, num)))
    print(reduce(lambda a,b : a*b, num))




if __name__ == '__main__':
    run()