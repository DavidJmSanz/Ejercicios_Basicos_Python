edad = int(input("Ingresa tu edad: "))
if 1 <= edad <= 12:
    print("eres unq Niño/a")
elif 13 <= edad <= 17:
    print("eres un@ Adolecente")
elif edad >= 18:
    print("Eres mayor de edad")
elif edad > 70 :
    print("Eres de la Tercera Edad")
else:
    print("¿eres un bebe?")