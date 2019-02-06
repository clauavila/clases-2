## crear una carpeta que se llame clases y dentro poner dino.py y persona.py
## crear una clase persona() que tenga atributos como nombre edad profesion
## al instanciar la clase tiene que saludar igual que el dino diciendo sus atributos

class persona:
    def __init__(self,un_nombre,la_edad,un_hobbie):
        self.nombre = un_nombre
        self.edad = la_edad
        self.hobbie= un_hobbie
        print('Hola, soy', self.nombre,'tengo', self.edad, 'y mi hobbie es', self.hobbie)

clau = persona('Clau','30','Panaderia')

