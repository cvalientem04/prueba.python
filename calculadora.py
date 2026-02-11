print("Bienvenido a la calculadora de Python")

numero1 = input("Ingrese el primer número: ")
numero2 = input("Ingrese el segundo número: ")  
operacion = input("Ingrese la operación (+, -, *, /): ")

numero1 =  int(numero1)
numero2 =  int(numero2)

if operacion == "+":
    resultado = numero1 + numero2
    print(f"El resultado de la suma es: {resultado}")

if operacion == "-":
    resultado = numero1 - numero2
    print(f"El resultado de la resta es: {resultado}")

if operacion == "*":
    resultado = numero1 * numero2
    print(f"El resultado de la multiplicación es: {resultado}")

if operacion == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"El resultado de la división es: {resultado}")
    else:
        print("Error: No se puede dividir por cero.")

