def divs(num):

        div = []
       
        for i in range(1, num +1):
            if  num % i == 0:
                div.append(i)
        return div
            

def run():
        num = input("un numero ")
        assert num.isnumeric(), "debes ingresar un numero"
        print(divs(int(num)))


if __name__ == '__main__' :
    run()