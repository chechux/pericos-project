import random,time
import utilidades as ut
import threading as th

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

    
class Habilidades ():

    def __init__(self,nombre,tipo,potencia,descripcion):

        self.nombre = nombre
        self.tipo = tipo
        self.potencia = potencia
        self.descripcion = descripcion

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

        #esta variable se enciende cuando este envenenado,ademas de que se agregara 
        #a la lista el valor que hay que ir restando a su vida durante los turnos activos del veneno,tambien agregados
        self.envenenado = [False]

    def __str__(self):
        
        return "----------------------\n\nLas stats de "+self.nombre+" son las siguientes :\n\n"+"Vida : "+str(self.vida)+"\nAtaque : "+str(self.ataque)+"\nDefensa : "+str(self.defensa)+"\nPrecision : "+str(self.precision)+"\nVelocidad : "+str(self.velocidad)

    def atacar(self,victima):

        total_damage = self.ataque-(self.ataque * victima.defensa/100)

        victima.vida -= total_damage
        
        return total_damage


class Jugador(Mob):

    def __init__(self,nombre,vida,ataque,defensa,precision,velocidad,descripcion,habilidades):

        super().__init__(nombre,vida,ataque,defensa,precision,velocidad)
          
        self.descripcion = descripcion
        self.items= {}
        self.habilidades = habilidades
        self.puntos = 0
        self.enemigos_derrotados = 0
        self.bosses_derrotados = 0

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

    def mostrar_jugador(self):
        print("""
                                                                                        &              
        ataque : {}                                                                  .-"`"-.
                                                                                    /       \\                 
        defensa : {}                                                                |   __  _|
                                                                                    |  /  \/ \\
        precision : {}                                                             WW  \_o/_o/
                                                                                    (        _)
        velocidad : {}                                                              |   .----\\
                                                                                    ;  | '----'
                                                                                    \__'--;`
                                                                                    |___/\|
            """.format(self.ataque,self.defensa,self.precision,self.velocidad))