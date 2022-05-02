import random,os,time
import utilidades as ut


# def limpiar_pantalla():

#     limpiar = "clear"

#     if os.name in ("nt","dos"):
#         limpiar="cls"
    
#     os.system(limpiar)

class Dimension():

    def __init__(self,nombre,items,villanos):
        
        self.nombre = nombre
        self.items = items
        self.villanos = villanos


class Items():

    def __init__(self,nombre,tipo,potencia,descipcion,turnos):

        self.nombre = nombre
        self.tipo = tipo
        self.potencia = potencia
        self.descripcion = descipcion
        self.turnos = turnos
        self.activo = [False]

    


selec_items = [
    
    Items("aceite_gines","s",random.randrange(15,20),"bebete este aceite colesterolientico para tener fuerza pa echar un ratejo mas en la batalla",3),
    Items("poco_pan","a",random.randrange(5,10),"con el poder del poco pan de patica tendras un poco mas de fuerza",3),
    Items("porro_perroviejo","p",random.randrange(50,80),"con este porro de perroviejo te concentraras mucho mas y tu precision sube",1)
]

class Mob():

    def __init__(self,nombre,vida,ataque,defensa,precision,velocidad):

        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.precision = precision
        self.velocidad = velocidad

    def __str__(self):
        
        return "----------------------\n\nLas stats de "+self.nombre+" son las siguientes :\n\n"+"Vida : "+str(self.vida)+"\nAtaque : "+str(self.ataque)+"\nDefensa : "+str(self.defensa)+"\nPrecision : "+str(self.precision)+"\nVelocidad : "+str(self.velocidad)

    def atacar(self,victima):

        total_damage = self.ataque-(self.ataque * victima.defensa/100)

        victima.vida -= total_damage
        return total_damage


class Jugador(Mob):

    def __init__(self,nombre,vida,ataque,defensa,precision,velocidad):

        super().__init__(nombre,vida,ataque,defensa,precision,velocidad)
          
        self.items= {}
        self.habilidades = {}

    def __str__(self):

        if len(self.items)>0:
            superti = ""
            for item in self.items.values():
                superti += item.nombre+"\ndescripcion : "+item.descripcion+" ||| activo : "+str(item.activo[0])+"\n\n"
            return super().__str__() + "\n\nLos Items en el inventario son los siguientes :\n\n"+superti+"----------------------"

        else:
            return super().__str__() + "\n\nNo hay Items en el inventario\n\n----------------------"

    def set_items(self):

        ut.limpiar_pantalla()

        print("\n\na continuacion vas a elegir los items para",self.nombre)
        print()
        print("solo puedes escoger 2 items para tu inventario y hay un total de",len(selec_items),",elegi bien turro : \n\n")

        time.sleep(3)

        ut.limpiar_pantalla() 

        while len(self.items)<2:

            for numero,item in enumerate(selec_items):

                 print(item.nombre,"(",numero,")\n")

                 print(item.descripcion,"\n\n")


            try:

                eleccion = int(input("escribe el numero del item para equiparlo : "))

                if selec_items[eleccion].nombre in self.items:

                    print("\n\neste lo tenes repetido forro de mierda...")

                    time.sleep(1)

                    ut.limpiar_pantalla()

                else:

                    self.items[selec_items[eleccion].nombre] = selec_items[eleccion]

                    print("\n\n\nitem",selec_items[eleccion].nombre,"equipado con exito a",self.nombre)
                
                    time.sleep(1.5)
                                
                    ut.limpiar_pantalla()

            except Exception as e:
                print("error! numero de item no disponible :",e)

                time.sleep(1.5)

                ut.limpiar_pantalla()


# #Dimension C-137 

#     #items

# #los items de tipo sk sirven para tener 2 turnos seguidos,es decir,que el rival se pierda su tuno por alguna rzon
# pistola_portales = Items("pistola de portales","sk",0,"con la pistola de portales de rick te vas a la dimension 35 en tal de esquivar el golpe y vuelve a ser tu turno !",1)
# #los items de tipo ataque incrementan la fuerza
# espada_bacon = Items("espada bacon","a",random.randrange(10,25),"con esta ridicula y sabrosa espada aumenta tu fuerza !",1)
# #los items de tipo sanacion incrementan la vida
# cuencas_de_ojos = Items("cuencas de ojos","s",random.randrange(10,25),"con estos deliciosas y asquerosas cuencas de ojos aumenta tu salud !",1)
# #los items de tipo precicison incrementan la precision,obviamente
# parche_de_morty = Items("parche de morty","p",30,"con este parche de morty te vuelves mas audaz y tu precision aumenta",1)
# #los items

#     #villanos

# abradolf_lincler = Mob("abradolf lincler",100,5,5,50,100)
# asustadizo_terry = Mob("asustadizo terry",100,5,5,50,10)
# bola_de_nieve = Mob("bola de nieve",100,5,5,50,10)

#     #dimension

# dimension_c137 = Dimension("C-137",[pistola_portales,espada_bacon,cuencas_de_ojos,parche_de_morty],[abradolf_lincler,asustadizo_terry,bola_de_nieve])




# dimensiones = [dimension_c137] 
        
               

# homero = Jugador("homero",100,40,50,50,20) 

#pruebas

# homero.set_items()

# dimensiones[0].villanos[0].nombre
# print(dimensiones[0].villanos[0].nombre)


#subfunciones que se usaran en main

#funcion de batalla
# def fight(jugador,villano):

#     kapasao = 10

#     while jugador.vida >0 and villano.vida >0:

#         action = int(input("\n\n1--Ver stats villano\n\n2--Ver stats jugador\n\n3--Atacar villano\n\n4--Usar item\n\n5--huir\n\n- - - > "))

#         if action == 1:

#             limpiar_pantalla()

#             print(villano)

#         if action == 2:

#             limpiar_pantalla()

#             print(jugador)

#         if action ==3:
            
#             if random.random() < max((jugador.precision-villano.velocidad)/100,0.3): 

#                 j1,j2 = jugador,villano

#             else:

#                 j1,j2 = villano,jugador

#             for i in range(2):

#                 print("\n"+j1.nombre,"es mas veloz que",j2.nombre,"y le va a golpear primero\n")

#                 time.sleep(1)

#                 total_damage = j1.atacar(j2)

#                 print("\nEse golpe le ha quitado",total_damage,"de vida\n")

#                 j1,j2 = j2,j1

#                 # print(jugador.vida,villano.vida)
#                 if jugador.vida <=0:
#                     return 0

#                 if villano.vida <=0:
#                     return 1
        
#         if action == 4:
            
#             print("\nTus items disponibles son los siguientes :\n")

#             for key,value in jugador.items.items():
#                 print(key,":",value.descripcion,"(",value.potencia,")","\n")
            


#         if action == 5:
#             break

#     return kapasao
        
#funcion principal del juego
# def main(jugador):

#     if isinstance(jugador,Jugador):

#         jugador.set_items()

#         while jugador.vida >0 and len(dimensiones) > 0:

#             print("\nvamos a entrar dentro de alguna dimension...\n")

#             time.sleep(1)

#             index_dimension = random.randrange(0,len(dimensiones))
#             dimension_actual = dimensiones[index_dimension]


#             print("\nvaya ! parece que hemos acabado en la dimension",dimension_actual.nombre,"\n")

#             time.sleep(1)

#             for times in range(len(dimension_actual.villanos)):

#                 index_villano = random.randrange(0,len(dimension_actual.villanos)) #indice aleatorio para elegir villano aleatorio
#                 villano_actual = dimension_actual.villanos[index_villano]

#                 print("\nte vas a enfrentar a",villano_actual.nombre,"\n")

#                 time.sleep(1)

#                 ragnarok =fight(jugador,villano_actual)
                                
#                 # print(ragnarok)

#                 if ragnarok == 0:
#                     print("jugador",jugador.nombre,"derrotado de manera muy brutal")
#                     break
#                 elif ragnarok == 1:
#                     print("\nvillano",villano_actual.nombre,"derrotado de manera muy brutal\n")
#                     del dimension_actual.villanos[index_villano]

#                 limpiar_pantalla()

#             if len(dimension_actual.villanos)==0:
#                 print("\nhas derrotado a todos los villanos de esta dimension...\n")
#                 del dimensiones[index_dimension]

#         if len(dimensiones) == 0:
#             print("Enhorabuena,te has pasado el juego -- te has pasado el juego")
#         else:
#             print("te rascaron")
#     else:
#         print("error ! no puedes jugar si no es con un jugador valido\n")

#     print("final while")

# main(homero)

# print(homero)