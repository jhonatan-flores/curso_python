#definir variable
auxdni=str()
dni=(int)
while True:#no hay 'repitir'en python
    #ingresa datos
    print("Ingrese DNI: ", end="")
    dni =int(input())
    #comversion de numero a texto
    auxdni=str(dni)
    #contar caracteres de la cadena validar con 8 e mostras mensajes de advertencia
    if len(auxdni)==8:
        print("la cantidad de digitos ingresados es correcta ")
    else:
        print("la cantidad de digitos ingresados no es correcta, intente de nuevo ")
    if len (auxdni)==8: break