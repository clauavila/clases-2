class Dino:
    
    # cola, dientes, color, size
    def __init__(self,un_nombre='',un_color='verde'):   ## init es una funcion predefinida de python, se utiliza siempre al iniciar
        nombre = un_nombre
        color = un_color
        print('Hola, soy un dinosaurio, me llamo', un_nombre,'y soy de color', un_color)
    
pepito = Dino("Pepe",'azul')
pepita = Dino('Pepa','rojo')
pepite = Dino('Pepx')
pepo = Dino(un_color='RoJO')
pepex = Dino('pepex','amarillo')


## agregarle una propiedad color a la clase Dino, y que salude diciendo 
# de que color es el dinosaurio.  
