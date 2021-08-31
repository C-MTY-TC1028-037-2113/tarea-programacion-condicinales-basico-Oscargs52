def main():
    #escribe tu código abajo de esta línea
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    num3 = int(input("Ingresa el tercer número: "))

    if (num1 > num2 and num1 > num3) or (num2 == num3 and num1 > num2):
        print(num1)
    elif (num2 > num1 and num2 > num3) or (num1 == num3 and num2 > num1) or (num2 == num1 and num2 > 3): 
        print(num2)
    else:
        print(num3)


if __name__=='__main__':
    main()
