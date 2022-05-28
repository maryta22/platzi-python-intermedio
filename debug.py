def divs(num):
    try:

        div = []

        if num<0:
            raise ValueError("negativo")
       
        for i in range(1, num +1):
            if  num % i == 0:
                div.append(i)

    except ValueError as ve:
        print(ve)
    
    finally:
        return div
            

def run():
    try:
        num = int(input("un numero "))
        print(divs(num))
    except ValueError:
        print("un numero")


if __name__ == '__main__' :
    run()