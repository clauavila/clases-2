class Dino:
    
    # cola, dientes, color, size
    def __init__(self,un_nombre='',un_color='verde'):   ## init es una funcion predefinida de python, se utiliza siempre al iniciar
        self.nombre = un_nombre
        self.color = un_color
        print('Hola, soy un dinosaurio, me llamo', self.nombre,'y soy de color', self.color)

    def rugir (self, rugido):
        print(self)
        print (rugido)
        print ('RAAAWR!!!', rugido)
    
    def cambiar_color(self, un_color):
        self.color= un_color
        ##print ('Se cambio el color de',self.nombre,'a', self.color)
    
    def que_color(self):
        print('El color del dino es',self.color)

pepito = Dino("Pepe",'azul') ##siempre hay que instanciar el objeto antes de ejecutar una funcion
pepito.cambiar_color('amarillo') ##init es la funcion para instanciar y crear el objeto

## aca instaciamos varios objetos tipo Dino
pepito = Dino("Pepe",'azul')
pepita = Dino('Pepa','dorado')
pepite = Dino('Pepx')
pepo = Dino(un_color='RoJO')
pepex = Dino('pepex','amarillo')


## agregarle una propiedad color a la clase Dino, y que salude diciendo 
# de que color es el dinosaurio.  
