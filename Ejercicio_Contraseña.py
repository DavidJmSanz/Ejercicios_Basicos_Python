contraseña_guardada=input("ingrese su nueva contraseña: ")

validacion_contraseña=input("Ingrese la contraseña guardada: ")

if contraseña_guardada.lower() == validacion_contraseña.lower():
    print("la contraseña es la correcta, la contra seña es: ", contraseña_guardada)
else:
    print("la contraseña es la incorrecta, intenta de nuevo")

