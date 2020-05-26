from collections import  namedtuple

persona = namedtuple('persona', ['nombre', 'apellido', 'cedula'] )
animal = namedtuple('animal', ['nombre', 'dueño', 'telefono'] )

firulais = animal(nombre='firulais', dueño='juan', telefono='23213')
luis = persona(nombre='Luis', apellido='solis', cedula='1231231')
maria = persona(nombre='Maria', apellido='Vargas', cedula='42342')

