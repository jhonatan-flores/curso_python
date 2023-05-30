## comvenciones para nombrar una variable

#  Convenciones más usuales
'''''
## lowerCamelCase
# Se crea uniendo palabras en la que la primera letra siempre estará en minúsculas y las siguientes palabras 
# tendrán su primera letra en mayúsculas. 
# Por ejemplo, una función para comprobar el estado de una API podríamos llamarla así con el formato lowerCamelCase:'''
def comprobarEstadoApi():
    pass
'''
## UpperCamelCase
# la primera palabra también tendrá su primera letra en mayúsculas.
# una clase para trabajar con la API de Twitter, podríamos llamarla así:'''
class twitterApi:
    pass
'''
## snake_case
# aquí uniremos las palabras mediante guiones y siempre en minúsculas'''
def comprobar_estado_api():
    pass
## SCREAMING_SNAKE_CASE
'''
todas las letras deberán ir en mayúsculas.'''
class TwitterApi:
    VERSION_API = 1
    URL_API = 'https://api.twitter.com'
## constantes y como se declara en python
'''Al inicio: _nombre
El uso de _ antes del nombre de una variable, como podría ser _mi_variable no modifica el comportamiento del código. Su uso es una mera convención que ha sido acordada por los usuarios de Python, y que indica que esa variable no debería ser accedida desde fuera de la clase, pero puede serlo.
'''
class Clase:
    def __init__(self):
        self._variable = 10

mi_clase = Clase()

# No se debería hacer, pero se puede
mi_clase._variable # 10

#Su uso si que puede modificar el comportamiento del código usado con funciones. Una función es definida con _ no es importada por defecto si usamos from x import *.
'''
Al Final: nombre_
Para entender el uso de la barra baja al final de una variable o función, es importante saber que Python tiene un determinado conjunto de palabras reservadas o keywords. Estas palabras no pueden ser usadas, porque de serlo Python se confundiría y no sabría como interpretarlas. Si por el motivo que sea, queremos llamar a una variable con el mismo nombre que una palabra reservada, podemos hacer algo así como class_. El siguiente código muestra que pasa si intentamos usar una palabra reservada para llamar a una variable.

#class = 5 # Error! class es una palabra reservada
'''
## Podemos usar _ para solucionarlo. Nótese que a diferencia de otras formas de usar _ en este caso no modifica comportamiento, por lo que su uso es arbitrario.
'''
class_ = 5
def_ = 10
Doble al Principio: __nombre
A diferencia del uso de una sola barra baja, el uso de la doble __ en un atributo o método hace que Python lo oculte al exterior. Existe un concepto muy interesante y particular de Python llamado name mangling, del que te recomendamos leer más.

Por lo tanto, en el siguiente ejemplo __nombre no será accesible desde el exterior de la clase. Por supuesto si que podría accederse desde la propia clase.

class Clase:
    def __init__(self):
        self.__variable = 10

mi_clase = Clase()
#mi_clase.__variable # Error! No es accesible
Doble al Principio y Final: nombre
Por último, el uso de __ al principio y al final de un nombre tiene especial relevancia cuando es aplicado a métodos. De hecho, a lo largo de este post ya has visto el uso de __init__ varias veces. Se trata de una forma que usa Python para designar a los conocidos como métodos mágicos como pueden ser también el __call__ o el __le__. Por norma general, es mejor no definir métodos propios con estos nombres, y limitarse a utilizar los que Python ya ofrece.

class Clase:
    def __init__(self):
        print("Init")
Descartando Variables con Barra Baja
Su uso suele ser común cuando queremos descartar una variable que por ejemplo pueda devolver una función. Veamos un ejemplo de una función que devuelve dos parámetros, la suma y la resta de dos variables.

def sumayresta(a, b):
    return (a+b), (a-b)
Tal vez queramos sólo el valor de la suma y no nos interese el valor de la resta. Para ello podríamos hacer lo siguiente.

suma, _ = sumayresta(5, 5)
# 10
Es una forma de decir “no me interesa esta variable”, pero como no se puede dejar el hueco vacío, se usa _ para rellenarlo.'''