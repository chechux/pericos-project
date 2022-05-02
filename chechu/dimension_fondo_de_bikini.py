import time
import random
###Dimension Fondo de bikini
##
##items
##
##sk
##savia_gary=("SaviGary","sk",0,"tirale savia de gary a tu rival para que no pueda atacar durante un turno!",1)
##
##ataque
##caza_medusas = Items("CazaMedusas 3000", "a", random.randrange(10,25),"Con el nuevo modelo CazaMedusas aumenta tu daño!",1)
##espatula = Items("Espatula de Oro","a",random.randrange(20,25),"el arma legendaria de Bobesponja! calcina a tus rivales.",1)#legendaria
##
##sanacion
##bote_burbujas = Items("Burbujeitor","s",random.randrange(10,25),"rociate de este jabon burbujeante para recuperar salud!",1)
##cangreburguer = Items("BurguerCangreburguer","s"random.randrange(20,25), "comete esta delicia para quedarte como nuevo!",1)#legendaria
##
##precision
##gafas = Items("Lectometor","p",30,"ponte estas gafas de lectura para aumentar tu precision",1)
##
##
##
##villanos
##
##patricio=Mob("Patricio Estrella",100,5,10,50,7)
##arenita=Mob("Arenita Mejillas",100,10,5,70,10)
##placton=Mob("Placton",80,10,5,90,10)
##calamardo=Mob("Calamardo",100,5,5,50,10)
##
##
##dimension
##
##dimension_fondo_de_bikini = Dimension("Fondo de bikini",[savia_gary, caza_medusas, espatula, bote_burbujas, cangreburguer, gafas],
##                                      [patricio, arenita, placton, calamardo]
##
##
##
##
##fdb = [dimension_fondo_de_bikini]
##
##
##bob = Jugador("Bobesponja",100,40,50,50,20)






###MINIJUEGO###

##print("-->JUAJUAJUJUAJUA")
##time.sleep(2)
##print("-->¡Que mala suerte grumete! te has topado con el mismisimo e insuperable...")
##time.sleep(2.5)
##print("-->¡HOLANDES ERRANTE!")
##time.sleep(1)
##print("-->JUAJUAJUUAJUAJU")
##time.sleep(2)
##print("-->¡Ahora tendras que enfrentarte a mi en una carrera encarnizada!")
##time.sleep(3)
##print("ahora elige tu vehiculo")
##print("")
##time.sleep(1.5)


                                    

class Vehiculo():
    def __init__(self,nombre,velocidad,daño,resistencia,gasolina,metros_r=0):
        self.nombre=nombre
        self.velocidad=velocidad
        self.daño=daño
        self.resistencia=resistencia
        self.gasolina=gasolina
        self.metros_r=metros_r

    def __str__(self):
            return self.nombre.upper() + ":\n-Velocidad:" + str(self.velocidad) + "\n-Daño:" + str(self.daño) + "\n-Resistencia:" + str(self.resistencia) + "\n-Gasolina:" + str(self.gasolina)



    def avanzar(self):
        metrosa = (random.randrange(1,7) * self.velocidad)/2
        self.metros_r+=metrosa
        self.gasolina-=random.randrange(5,15)

        print(self.nombre, "ha avanzado", metrosa,", en total ha avanzado",self.metros_r)
        if self.gasolina < 30:
            time.sleep(1)
            print("¡CUIDADO!, Te quedan", self.gasolina, " litros de aceite grasiento, deberias repostar")

    def repostar(self):
        print("Repostando...")
        gasolinar=random.randrange(10,30)
        self.gasolina +=gasolinar
        time.sleep(2)
        print("¡Repostado! ahora tienes", self.gasolina, "litros de aceite grasiento")
    
    

    def atacar(self):
        dañor = random.randrange(1,self.daño)
        self.resistencia -=dañor
        print(self.nombre," ataca, logrando", dañor,"puntos de daño, le quedan", self.resistencia,"puntos de vida")
        if dañor > self.daño-3:
            print("¡GOLPE CRÍTICO!, dejas al oponente 1 turno sin poder hacer nada")
            return True
        else:
            return False

holandes=Vehiculo("Barco del holandes errante",7,15,100,100)
v1=Vehiculo("coche de la señorita puff",7,10,90,90)
v2=Vehiculo("Gary",5,15,150,175)
v3=Vehiculo("casa de bobesponja",10,20,80,70)

print(v1)
print("----------------------")
print(v2)
print("----------------------")
print(v3)
print("")
print("REGLAS: \nPulsa 1 para avanzar x metros. \nPulsa 2 para repostar aceite grasiento. \nPulsa 3 para atacar al Holandes Errante.")
print("")
print("(el vehiculo se elige poniendo 'v' y el numero del vehiculo por orden)")
eleccion=input("-->")

if eleccion == "v1":
    print(v1.nombre," ¡Buena elecion!")
    time.sleep(1)
    print("¿PREPARADOOS?")
    time.sleep(1)
    print("¿LISTOOS?")
    time.sleep(2)
    print("¡YAAAAA!")
    print("")
    time.sleep(1)
    
    while (v1.metros_r <= 100 or holandes.metros_r <=100) or (v1.resistencia <=0 or holandes.resistencia <=0):
        accion=int(input("¿que vas a hacer?:"))
        if accion == 1:
            v1.avanzar()

        if accion == 2:
            v1.repostar()
            if holandes.gasolina < 20:
                holandes.repostar()
                print("el holandes a repostado aceite grasiento tambien")
            else:
                print("el holandes ha aprovechado esa paradita para avanzar")
                holandes.avanzar()
               

        if accion == 3:
            v1.atacar()


            

if eleccion == "v2":
    print(v2.nombre," ¡Buena elecion!")
    time.sleep(1)
    print("¿PREPARADOOS?")
    time.sleep(1)
    print("¿LISTOOS?")
    time.sleep(2)
    print("¡YAAAAA!")
    print("")
    time.sleep(1)
    
    while v2.metros_r < 100:
        accion=int(input("¿que vas a hacer?:"))
        if accion == 1:
            v2.avanzar()

        if accion == 2:
            v2.repostar()
            if holandes.gasolina < 20:
                holandes.repostar()
                print("el holandes a repostado aceite grasiento tambien")
            else:
                holandes.avanzar()
                print("el holandes ha aprovechado esa paradita para avanzar")

        if accion == 3:
            v2.atacar()

    if v2.metros_r > 100 or holandes.resistencia <=0:
        print("--> ¡ARGGHHH , ME HAS DERROTADO! PERO SOLO POR ESTA VEZ...")



if eleccion == "v3":
    print(v3.nombre," ¡Buena elecion!")
    time.sleep(1)
    print("¿PREPARADOOS?")
    time.sleep(1)
    print("¿LISTOOS?")
    time.sleep(2)
    print("¡YAAAAA!")
    print("")
    time.sleep(1)
    
    while (v1.metros_r <= 100 or holandes.metros_r <=100) or (v1.resistencia <=0 or holandes.resistencia <=0):
        
        accion=int(input("¿que vas a hacer?:"))
        if accion == 1:
            v3.avanzar()

        if accion == 2:
            v3.repostar()
            if holandes.gasolina < 20:
                holandes.repostar()
                print("el holandes a repostado aceite grasiento tambien")
            else:
                print("el holandes ha aprovechado esa paradita para avanzar")
                holandes.avanzar()
                
        if accion == 3:
            if v3.atacar():
                continue
            else:
                ##holandes random
                print("hola")

    if v3.metros_r >= 100 or holandes.resistencia <=0:
        print("--> ¡ARGGHHH , ME HAS DERROTADO! PERO SOLO POR ESTA VEZ...")
                
    















                                      


