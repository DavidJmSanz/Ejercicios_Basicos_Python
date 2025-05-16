edad = int(input("Ingresa tu edad: "))

if edad <= 0:
    print("Edad no válida. Por favor, ingresa un número positivo.")
elif edad <= 1:
    print("¿Eres un bebé?")
elif edad <= 12:
    print("Eres un/a niño/a")
elif edad <= 17:
    print("Eres un/a adolescente")
elif edad > 70:
    print("Eres de la tercera edad")
else:
    print("Eres mayor de edad")
