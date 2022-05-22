import random,time
import utilidades as ut

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
        
        return "----------------------------------------------------------------------------------\n\n    - - - - > Las stats de "+self.nombre+" son las siguientes :\n\n"+"             Vida : "+str(self.vida)+"\n\n             Ataque : "+str(self.ataque)+"\n\n             Defensa : "+str(self.defensa)+"\n\n             Precision : "+str(self.precision)+"\n\n             Velocidad : "+str(self.velocidad)+"\n\n----------------------------------------------------------------------------------\n\n"

    def atacar(self,victima):

        total_damage = self.ataque-(self.ataque * victima.defensa/100)

        victima.vida -= total_damage
        
        return total_damage


class Jugador(Mob):

    def __init__(self,nombre,vida,ataque,defensa,precision,velocidad,descripcion,sonido,habilidades):

        super().__init__(nombre,vida,ataque,defensa,precision,velocidad)
          
        self.descripcion = descripcion
        self.items= {}
        self.habilidades = habilidades
        self.sonido = sonido
        self.puntos = 0
        self.enemigos_derrotados = 0
        self.bosses_derrotados = 0

    def __str__(self):

        if len(self.items)>0:
            superti = ""
            for item in self.items.values():
                superti += "         "+item.nombre+"\n\n                - - > Descripcion : "+item.descripcion+" ||| Activo : "+str(item.activo[0])+"\n\n"
            return super().__str__() + "\n    - - - - > Los Items en el inventario son los siguientes :\n\n"+superti+"----------------------------------------------------------------------------------"

        else:
            return super().__str__() + "\n    - - - - > No hay Items en el inventario\n\n----------------------------------------------------------------------------------"

