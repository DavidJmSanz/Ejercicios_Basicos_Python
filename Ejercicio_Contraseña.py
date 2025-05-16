contraseña=input("ingrese su nueva contraseña: ")
cont_nueva = contraseña.upper()
ing_contraseña=input("Ingrese la contraseña guardada: ")
val_contraseña=ing_contraseña.upper()

if cont_nueva == val_contraseña:
    print("la contraseña es la correcta, la contra seña es: ", cont_nueva)
else:
    print("la contraseña es la incorrecta, intenta de nuevo")

