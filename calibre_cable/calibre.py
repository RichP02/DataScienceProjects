import math
import sys

# Declaracion de las variables
potencia = int(input("Ingresa la potencia: "))
tension = int(input("Ingresa la tension: "))
cos = float(input("Ingresa el cos: "))
longitud = float(input("Ingresa la longitud del tramo mas largo: "))
factor_temp = int(input("Ingresa la temperatura promedio: "))
factor_agru = int(input("Ingresa la cantidad de cables que van a ir juntos: "))
cantidad_agru = factor_agru
tierra = int(input("Llevas tierra (1 - Si) (2 - No): "))
match tierra:
    case 1:
        tierra = 1
    case 2:
        tierra = 0
    case _:
        tierra = 0
        print("No lleva tierra")

# potencia = 5100
# cos = 0.9
# tension = 120
# longitud = 20
# factor_temp = 32
# factor_agru = 3
# cantidad_agru = factor_agru
# tierra = 1

# Cambiando valor del factor por temperatura
if(factor_temp <= 10):
    factor_temp = 1.29
elif (factor_temp >= 11 and factor_temp <= 15 ):
    factor_temp = 1.22
elif (factor_temp > 16 and factor_temp <= 20 ):
    factor_temp = 1.15
elif (factor_temp >= 21 and factor_temp <= 25 ):
    factor_temp = 1.08
elif (factor_temp >= 26 and factor_temp <= 30 ):
    factor_temp = 1
elif (factor_temp >= 31 and factor_temp <= 35 ):
    factor_temp = 0.91
elif (factor_temp >= 36 and factor_temp <= 40 ):
    factor_temp = 0.82
elif (factor_temp >= 41 ):
    factor_temp = 0.71

# Cambiando valor del factor por agrupamiento
if(factor_agru < 4):
    factor_agru = 1
elif(factor_agru >= 4 and factor_agru <= 6):
    factor_agru = 0.8
elif(factor_agru >= 7 and factor_agru <= 9):
    factor_agru = 0.7
elif(factor_agru >= 10 and factor_agru <= 20):
    factor_agru = 0.5
elif(factor_agru >= 21 and factor_agru <= 30):
    factor_agru = 0.45
elif(factor_agru >= 31 and factor_agru <= 40):
    factor_agru = 0.4
elif(factor_agru >= 41):
    factor_agru = 0.35

# Operaciones para calcular variables
s = potencia / cos
corriente_nominal = s / tension
corriente_agrup = corriente_nominal / factor_agru
corriente_temp = corriente_agrup / factor_temp
caida_tension = ((4 * longitud * corriente_nominal) / (tension * 3))

# Imprimiendo resultados de operaciones
print("\n----------------------------------------------------------\n")
print(f"Valor de s: {s:.2f}")
print(f"Valor corriente nominal: {corriente_nominal:.2f}")
print(f"Valor corriente de agrupamiento: {corriente_agrup:.2f}")
print(f"Valor corriente de temperatura: {corriente_temp:.2f}")
print(f"Valor de caida de tension: {caida_tension:.2f}")

# Operaciones para calcular el calibre del cable
calibre_ampe = ""
calibre_tensi = ""

if corriente_temp <= 15:
    calibre_ampe = "Cal. 14"
elif corriente_temp <= 20: # Captura todo lo mayor a 15 hasta 20
    calibre_ampe = "Cal. 12"
elif corriente_temp <= 30:
    calibre_ampe = "Cal. 10"
elif corriente_temp <= 40:
    calibre_ampe = "Cal. 8"
elif corriente_temp <= 55:
    calibre_ampe = "Cal. 6"
elif corriente_temp <= 70:
    calibre_ampe = "Cal. 4"
elif corriente_temp <= 85:
    calibre_ampe = "Cal. 3"
elif corriente_temp <= 95:
    calibre_ampe = "Cal. 2"
elif corriente_temp <= 110:
    calibre_ampe = "Cal. 1"
else:
    print("ERROR: La corriente excede el límite máximo de 110A. Programa terminado.")
    sys.exit()  # Aquí se corta la ejecución del script por completo


# --- Cálculo por Caída de Tensión ---
if caida_tension <= 2.08:
    calibre_tensi = "Cal. 14"
elif caida_tension <= 3.31:
    calibre_tensi = "Cal. 12"
elif caida_tension <= 5.26:
    calibre_tensi = "Cal. 10"
elif caida_tension <= 8.37:
    calibre_tensi = "Cal. 8"
elif caida_tension <= 13.3:
    calibre_tensi = "Cal. 6"
elif caida_tension <= 21.2:
    calibre_tensi = "Cal. 4"
elif caida_tension <= 33.6:
    calibre_tensi = "Cal. 2"
elif caida_tension <= 42.4:
    calibre_tensi = "Cal. 1"
else:
    print("ERROR: La corriente excede el límite máximo de 110A. Programa terminado.")
    sys.exit()


print("\n----------------------------------------------------------\n")
jerarquia_calibres = ["Cal. 14", "Cal. 12", "Cal. 10", "Cal. 8", "Cal. 6", "Cal. 4", "Cal. 3", "Cal. 2", "Cal. 1"]
decision_cali = ""

indice_ampe = jerarquia_calibres.index(calibre_ampe)
indice_tensi = jerarquia_calibres.index(calibre_tensi)

if indice_ampe >= indice_tensi:
    decision_cali = calibre_ampe
else:
    decision_cali = calibre_tensi

print(f"Resultado por Amperaje: {calibre_ampe}")
print(f"Resultado por Caída de Tensión: {calibre_tensi}")

if(decision_cali == "Cal. 14"):
    print("\nNOTA DE NORMATIVIDAD (NOM-001-SEDE): El calibre mínimo para circuitos de fuerza, cocina y electrodomésticos debe ser 12 AWG (protegido con breaker de 20A).")
    motor = int(input("¿Tienes algo conectado algo de eso? (1 - Si) (2 - No): "))

    if (motor == 1):
        decision_cali = "Cal. 12"
    else:
        pass

print(f"-> Calibre final seleccionado: {decision_cali}")


# Tamaños de los calibres
print("\n----------------------------------------------------------\n")
match decision_cali:
    case "Cal. 14":
        grosor_calibre = 6.258
    case "Cal. 12":
        grosor_calibre = 8.581
    case "Cal. 10":
        grosor_calibre = 13.61
    case "Cal. 8":
        grosor_calibre = 23.61
    case "Cal. 6":
        grosor_calibre = 32.71
    case "Cal. 4":
        grosor_calibre = 53.16
    case "Cal. 3":
        grosor_calibre = 62.77
    case "Cal. 2":
        grosor_calibre = 74.71
    case "Cal. 1":
        grosor_calibre = 100.8

decision_tierra = ""
if (tierra == 1):
    if (corriente_temp < 15):
        decision_tierra = "Cal. 14"
        grosor_tierra = 2.08
    elif (corriente_temp >= 15 and corriente_temp < 20):
        decision_tierra = "Cal. 12"
        grosor_tierra = 3.31
    elif (corriente_temp >= 21 and corriente_temp < 60):
        decision_tierra = "Cal. 10"
        grosor_tierra = 5.26
    elif (corriente_temp >= 61 and corriente_temp <= 100):
        decision_tierra = "Cal. 8"
        grosor_tierra = 8.37
else:
    grosor_tierra = 0

# Seleccionar el tipo de tuberia
tuberia = (grosor_calibre * cantidad_agru) + grosor_tierra
decision_tube = ""

if (tuberia < 81):
    decision_tube = "1/2\""
elif (tuberia >= 82 and tuberia < 141):
    decision_tube =  "3/4\""
elif (tuberia >= 142 and tuberia < 229):
    decision_tube = "1\""

print(f"El cable que se utiliza es {decision_cali} = {grosor_calibre} x {cantidad_agru}")
if (tierra == 1):
    print(f"El cable para la tierra es {decision_tierra} = {grosor_tierra}")
else:
    pass
print(f"El grosor total utilizado es: {tuberia:.2f}")

print(f"-> Tuberia a utilizar: {decision_tube}")
print("\n----------------------------------------------------------\n")