#hacer un programa que pida al usuario ingresar su primer apellido,si suapellido tiene como ultimos careteres las letras --ez-- mostrar un mensaje que diga que es un peruano
##si termina en --es-- eres casi español
#ingresar dato
username=input("ingrese tu primer apellido: ")
if username[-2:]=='es':
    print("eres casi español: ")
elif username[-2:]=='ez':
    print("eres casi peruano")