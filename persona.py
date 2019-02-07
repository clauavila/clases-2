## crear una carpeta que se llame clases y dentro poner dino.py y persona.py
## crear una clase persona() que tenga atributos como nombre edad profesion
## al instanciar la clase tiene que saludar igual que el dino diciendo sus atributos

class persona:
    hobbies=[] ## agregarle un atributo de clase a la clase persona que almacene una lista de hobbies
    def __init__(self,un_nombre,la_edad):
        self.nombre = un_nombre
        self.edad = la_edad
        print('Hola, soy', self.nombre,'tengo', self.edad)
   ## Agregar un metodo a la clase persona que se llame cumplea;os y que aumente la edad de la 
##persona en un anho y retorne la edad nueva 
    def cumple_plusone(self):
        self.edad += 1
        return self.edad
  ## crear un metodo getter que retorne los hobbies de la persona  
    def hobbies_lista(self):
        return self.hobbies
## crear un meetodo ue agregue hobbies a la lista
    def set_hobbies(self,lista_hobbies):
        if type (lista_hobbies) == str or type (lista_hobbies) == list:
            self.hobbies.append(lista_hobbies)
            return self.hobbies
        else:
        return ('Debes ingresar una lista [] o una cadena de texto ''')
    



clau=persona('Clau', 30)
fran = persona('Fran', 29)
clau.cumple_plusone()
fran.cumple_plusone()