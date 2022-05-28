import random

def read():
    palabras = []
    with open("./data.txt", "r", encoding="utf-8") as f: 
        for line in f:
            palabras.append(line)
    return palabras

def menu():
    return 'Menu del juego\nPresiona 1 para jugar\nPresiona 2 para salir\n'



def run():
    palabras = read()

    print(menu())
    opcion = int(input("Ingresa un numero"))

    while opcion != 2:

        numero = random.randint(0, len(palabras))
        palabra = palabras[numero]
        palabra = palabra.replace("\n","")

        lineas = "_" * len(palabra)

        while lineas != palabra:

            print(lineas)

            letra = input("Ingresa una letra")
            if letra in palabra:
                indices = [pos for pos, char in enumerate(palabra) if char == letra]
                print(indices)
                for i in indices:
                    lineas = lineas[:i]+ letra + lineas[i+1:]
            
        print("")
        print(menu())
        opcion = int(input("Ingresa un numero"))
    

if __name__ == '__main__' :
    run()