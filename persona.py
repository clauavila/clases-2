## crear una carpeta que se llame clases y dentro poner dino.py y persona.py
## crear una clase persona() que tenga atributos como nombre edad profesion
## al instanciar la clase tiene que saludar igual que el dino diciendo sus atributos

class persona:
    def __init__(self,un_nombre,la_edad,un_hobbie):
        self.nombre = un_nombre
        self.edad = la_edad
        self.hobbie= un_hobbie
        print('Hola, soy', self.nombre,'tengo', self.edad, 'y mi hobbie es', self.hobbie)
    
    def cumple_plusone(self):
        self.edad += 1
        return self.edad

clau = persona('Clau',30,'Panaderia')
fran= persona('Fran', 29, 'Tomar pilsen')
clau.cumple_plusone()
fran.cumple_plusone()


### Agregar un metodo a la clase persona que se llame cumplea;os y que aumente la edad de la 
##persona en un anho y retorne la edad nueva