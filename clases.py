import random,os,time

def limpiar_pantalla():

    limpiar = "clear"

    if os.name in ("nt","dos"):
        limpiar="cls"
    
    os.system(limpiar)

class Dimension():

    def __init__(self,nombre,items,villanos):
        
        self.nombre = nombre
        self.items = items
        self.villanos = villanos


class Items():

    def __init__(self,nombre,tipo,potencia,descipcion):

        self.nombre = nombre
        self.tipo = tipo
        self.potencia = potencia
        self.descripcion = descipcion




selec_items = [Items("aceite_gines","s",random.randrange(15,20),"bebete este aceite colesterolientico para tener fuerza pa echar un ratejo mas en la batalla"),Items("poco_pan","a",random.randrange(5,10),"con el poder del poco pan de patica tendras un poco mas de fuerza"),Items("porro_perroviejo","p",random.randrange(50,80),"con este porro de perroviejo te concentraras mucho mas y tu precision sube")]

class Mob():

    def __init__(self,nombre,vida,ataque,defensa,precision,velocidad):

        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.precision = precision
        self.velocidad = velocidad

class Jugador(Mob):

    def __init__(self,nombre,vida,ataque,defensa,precision,velocidad):

        super().__init__(nombre,vida,ataque,defensa,precision,velocidad)
          
        self.items= {}
        self.habilidades = {}

    def set_items(self):

        limpiar_pantalla()

        print("\n\na continuacion vas a elegir los items para",self.nombre)
        print()
        print("solo puedes escoger 2 items para tu inventario y hay un total de",len(selec_items),",elegi bien turro : \n\n")

        time.sleep(3)

        limpiar_pantalla() 

        while len(self.items)<2:

            for numero,item in enumerate(selec_items):

                 print(item.nombre,"(",numero,")\n")

                 print(item.descripcion,"\n\n")


            try:

                eleccion = int(input("escribe el numero del item para equiparlo : "))

                if selec_items[eleccion].nombre in self.items:

                    print("\n\neste lo tenes repetido forro de mierda...")

                    time.sleep(1)

                    limpiar_pantalla()

                else:

                    self.items[selec_items[eleccion].nombre] = selec_items[eleccion]

                    print("\n\n\nitem",selec_items[eleccion].nombre,"equipado con exito a",self.nombre)
                
                    time.sleep(1.5)
                                
                    limpiar_pantalla()

            except Exception as e:
                print("error! numero de item no disponible :",e)

                time.sleep(1.5)

                limpiar_pantalla()


#Dimension C-137 

    #items

#los items de tipo sk sirven para tener 2 turnos seguidos,es decir,que el rival se pierda su tuno por alguna rzon
pistola_portales = Items("pistola de portales","sk",0,"con la pistola de portales de rick te vas a la dimension 35 en tal de esquivar el golpe y vuelve a ser tu turno !")
#los items de tipo ataque incrementan la fuerza
espada_bacon = Items("espada bacon","a",random.randrange(10,25),"con esta ridicula y sabrosa espada aumenta tu fuerza !")
#los items de tipo sanacion incrementan la vida
cuencas_de_ojos = Items("cuencas de ojos","s",random.randrange(10,25),"con estos deliciosas y asquerosas cuencas de ojos aumenta tu salud !")
#los items de tipo precicison incrementan la precision,obviamente
parche_de_morty = Items("parche de morty","p",30,"con este parche de morty te vuelves mas audaz y tu precision aumenta")
#los items

    #villanos

abradolf_lincler = Mob("abradolf lincler",100,5,5,50,100)
asustadizo_terry = Mob("asustadizo terry",100,5,5,50,10)
bola_de_nieve = Mob("bola de nieve",100,5,5,50,10)

    #dimension

dimension_c137 = Dimension("C-137",[pistola_portales,espada_bacon,cuencas_de_ojos,parche_de_morty],[abradolflincler])


dimensiones = [dimension_c137] 
        
               

homero = Jugador("homero",100,40,50,50,20) 

# homero.set_items()

dimensiones[0].villanos[0].nombre
print(dimensiones[0].villanos[0].nombre)
