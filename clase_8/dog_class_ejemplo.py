
# perro

class Perro:
    def __init__(self, nombre):
        self.mi_nombre = nombre
        print(f'ha nacido un {self.mi_nombre}!')

    def ladra(self):
        print(f'Soy {self.mi_nombre} y estoy ladrando!')

bobby = Perro(nombre='Booby')
camilo = Perro(nombre='Camilo')

bobby.ladra()
camilo.ladra()