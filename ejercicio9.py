# Ejercicio 9
cantidad = float(input("Introduce la cantidad a invertir: "))
interes_anual = float(input("Introduce el interés anual (en %): "))
anos = int(input("Introduce el número de años: "))
capital_obtenido = cantidad * (1 + interes_anual / 100) ** anos
print("El capital obtenido en la inversión es:", round(capital_obtenido, 2))