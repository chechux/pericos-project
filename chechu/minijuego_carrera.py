import time
import random
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

        print(self.nombre, "ha avanzado", metrosa,", en total ha avanzado",self.metros_r,"te quedan", self.gasolina,"litros de aceite grasiento")
        if self.gasolina < 30:
            time.sleep(1)
            print("¡CUIDADO!, Te quedan", self.gasolina, " litros de aceite grasiento, deberias repostar")

    def avanzarh(self):
        metrosa = (random.randrange(1,7) * self.velocidad)/2
        self.metros_r+=metrosa
        self.gasolina-=random.randrange(5,15)
        print(self.nombre, "ha avanzado", metrosa,", en total ha avanzado",self.metros_r, "le quedan" , self.gasolina,"litros de aceite grasiento")
                 

    def repostar(self):
        print("Repostando...")
        print("")
        print("""
          .--------|-.
          |==  ==|-.
          |~~ ~~~|`\\
          |LILILI| ||
          |      |//
          |      |/
          |      |
        __|______|__
       [____________]
        """)
        gasolinar=random.randrange(10,30)
        self.gasolina +=gasolinar
        time.sleep(2)
        print("¡Repostado! ahora tienes", self.gasolina, "litros de aceite grasiento")

    def repostarh(self):
        gasolinar=random.randrange(10,30)
        self.gasolina +=gasolinar
        time.sleep(1)
        print("El Holandes ha repostado aceite grasiento")
    
    
    def atacar(self,holandes):
        dañor = random.randrange(1,self.daño)
        holandes.resistencia -=dañor
        print(self.nombre," ataca, logrando", dañor,"puntos de daño, le quedan", holandes.resistencia,"puntos de vida")
        if dañor > self.daño-3:
            print("¡GOLPE CRÍTICO!, golpeas dos veces seguidas")
            time.sleep(0.5)
            print("--> ARRGHH ¡MALDITA ESPONJA!")
            return True
        else:
            return False

    def atacarc(self,holandes):
        dañor = random.randrange(1,self.daño)
        holandes.resistencia -=dañor
        print(self.nombre," ataca, logrando", dañor,"puntos de daño, le quedan", holandes.resistencia,"puntos de vida")


    def atacarh(self,v):
        dañor = random.randrange(1,self.daño)
        v.resistencia -=dañor
        print(self.nombre," ataca, logrando", dañor,"puntos de daño, te quedan", v.resistencia,"puntos de vida")
        if dañor > self.daño-3:
            print("¡GOLPE CRÍTICO!, el Holandes te golpea dos veces...")
            time.sleep(0.5)
            print("--> JUAJUAJUA ¡PRINGAO!")
            dañor = random.randrange(1,self.daño)
            v.resistencia -=dañor
            print(self.nombre," ataca, logrando", dañor,"puntos de daño, te quedan", v.resistencia,"puntos de vida")
            
        

    def azar(self,z):
        metodo=random.randint(1,2)
        if metodo == 1:
            holandes.atacarh(z)
        elif metodo == 2:
            holandes.avanzarh()
                

    def empezar(self):
        print("""
┏━━━┓
┃┏━┓┃
┗┛┏┛┃
┏┓┗┓┃
┃┗━┛┃
┗━━━┛

""")

        time.sleep(1)
        print("""
┏━━━┓
┃┏━┓┃
┗┛┏┛┃
┏━┛┏┛
┃┃┗━┓
┗━━━┛

""")

        time.sleep(1)

        print("""
╋┏┓
┏┛┃
┗┓┃
╋┃┃
┏┛┗┓
┗━━┛

""")

        time.sleep(1.5)

        print("""


                 ┏┓
                 ┃┃
┏━━┳━━┫   ┃┃
┃┏┓┃┏┓┃   ┃┃
┃┗┛┃┗┛┃   ┃┃
┗━┓┣━━┻   ┃┃
┏━┛┃        ┏━┓
┗━━┛        ┗━┛    

""")

def ganar():
    print("""
                    ┏┓┏┓┏┓┏━━┓┏━┓  ┏┓
                    ┃┃┃┃┃┃┗┫┣┛┃┃┗┓┃┃
                    ┃┃┃┃┃┃  ┃┃  ┃┏┓┗┛┃
                    ┃┗┛┗┛┃  ┃┃  ┃┃┗┓┃┃
                    ┗┓┏┓┏┛┏┫┣┓┃┃  ┃┃┃
                      ┗┛┗┛  ┗━━┛┗┛  ┗━┛

""")

def perder():
    print("""
                ┏┓      ┏━━━┓┏━━━┓┏━━━┓
                ┃┃      ┃┏━┓┃┃┏━┓┃┃┏━━┛
                ┃┃      ┃┃  ┃┃┃┗━━┓┃┗━━┓
                ┃┃  ┏┓┃┃  ┃┃┗━━┓┃┃┏━━┛
                ┃┗━┛┃┃┗━┛┃┃┗━┛┃┃┗━━┓
                ┗━━━┛┗━━━┛┗━━━┛┗━━━┛

""")


holandes=Vehiculo("Barco del holandes errante",7,17,30,100)
v1=Vehiculo("coche de la señorita puff",7,10,90,90)
v2=Vehiculo("Gary",5,15,150,175)
v3=Vehiculo("casa de bobesponja",10,20,80,70)




print(v1)
print("----------------------")
print(v2)
print("----------------------")
print(v3)
print("")
print("")
print("-------- BOSS STATS--------")
print(holandes)
print("")
print("REGLAS: \nPulsa 1 para avanzar x metros. \nPulsa 2 para repostar aceite grasiento. \nPulsa 3 para atacar al Holandes Errante.")
print("")
time.sleep(1.5)
print("!Llega a los 200 metros o destruye el vehiculo enemigo para ganar!")
print("")
print("(el vehiculo se elige poniendo 'v' y el numero del vehiculo por orden)")

eleccion=input("-->")




if eleccion == "v1":
    print(v1.nombre," ¡Buena elecion!")
    v1.empezar()
    
    while v1.metros_r <= 200 and holandes.metros_r <=200:
        if v1.gasolina <= 0:
            break
        if v1.resistencia <=0:
            break
        if holandes.resistencia <=0:
            break
        if v1.metros_r >=200:
            break
        if holandes.metros_r >= 200:
            break
        
        print("")
        accion=int(input("¿que vas a hacer?: \n.1-Avanzar. \n2.-Repostar. \n3.-Atacar. \n-->"))
        print("")
        if accion == 1:
            v1.avanzar()
            if holandes.gasolina < 20:
                holandes.repostarh()
            else:
                holandes.azar(v1)                

        if accion == 2:
            v1.repostar()
            if holandes.gasolina < 20:
                holandes.repostarh()
            else:
                holandes.azar(v1)
               
        if accion == 3:
            if v1.atacar(holandes):
                v1.atacarc(holandes)
                holandes.azar(v1)
            else:
                if holandes.gasolina < 20:
                    holandes.repostarh()
                else:
                    holandes.azar(v1)

    if v1.metros_r >=200:
        print("¡¡¡Enhorabuena!!! has llegado a la meta antes que el Holandes Errante :)")
        ganar()
    
    elif holandes.metros_r >=200:
        print("El Holandes Errante ha llegado a la meta... :(")
        perder()

    elif v1.gasolina <=0:
        print("Has perdido... Te has quedado sin aceite grasiento")
        perder()
        
    elif v1.resistencia <=0:
        print("El Holandes ha roto tu vehiculo... has perdido")
        perder()

    elif holandes.resistencia <=0:
        print("¡Has tumbado el barco del Holandes Errante! Enhorabuena")
        ganar()
            





if eleccion == "v2":
    print(v2.nombre, "¡Buena eleccion!")    
    while v2.metros_r <= 200 and holandes.metros_r <=200:
        if v2.gasolina <= 0:
            break
        if v2.resistencia <=0:
            break
        if holandes.resistencia <=0:
            break
        if v2.metros_r >=200:
            break
        if holandes.metros_r >= 200:
            break
        
        print("")
        accion=int(input("¿que vas a hacer?: \n.1-Avanzar. \n2.-Repostar. \n3.-Atacar"))
        print("")
        if accion == 1:
            v2.avanzar()
            if holandes.gasolina < 20:
                holandes.repostarh()
            else:
                holandes.azar(v2)
            
                

        if accion == 2:
            v2.repostar()
            if holandes.gasolina < 20:
                holandes.repostarh()
            else:
                holandes.azar(v2)
                pass


            if accion == 3:
                if v2.atacar(holandes):
                    v2.atacarc(holandes)
                    holandes.azar(v2)
                else:
                    if holandes.gasolina < 20:
                        holandes.repostarh()
                    else:
                        holandes.azar(v2)
                    
    if v2.metros_r >=200:
        print("¡¡¡Enhorabuena!!! has ganado al Holandes Errante :)")
        ganar()
    
    elif holandes.metros_r >=200:
        print("El Holandes Errante ha llegado a la meta... :(")
        perder()

    elif v2.gasolina <=0:
        print("Has perdido... Te has quedado sin aceite grasiento")
        perder()

    elif v2.resistencia <=0:
        print("El Holandes ha roto tu vehiculo... has perdido")
        perder()
        
    elif holandes.resistencia <=0:
        print("¡Has tumbado el barco del Holandes Errante! Enhorabuena")
        ganar()





        
if eleccion == "v3":
    print(v3.nombre, "!Buena eleccion")

    
    while v3.metros_r <= 200 and holandes.metros_r <=200:
        if v3.gasolina <= 0:
            break
        if v3.resistencia <=0:
            break
        if holandes.resistencia <=0:
            break
        if v3.metros_r >=200:
            break
        if holandes.metros_r >= 200:
            break
        
        print("")
        accion=int(input("¿que vas a hacer?: \n.1-Avanzar. \n2.-Repostar. \n3.-Atacar"))
        print("")
        if accion == 1:
            v3.avanzar()
            if holandes.gasolina < 20:
                holandes.repostarh()
            else:
                holandes.azar(v3)
                

        if accion == 2:
            v3.repostar()
            if holandes.gasolina < 20:
                holandes.repostarh()
            else:
                holandes.azar(v3)

               
        if accion == 3:
            if v3.atacar(holandes):
                v3.atacarc(holandes)
                holandes.azar(v3)
            else:
                if holandes.gasolina < 20:
                    holandes.repostarh()
                else:
                    holandes.azar(v3)
                    

    if v3.metros_r >=200:
        print("¡¡¡Enhorabuena!!! has ganado al Holandes Errante :)")
        ganar()
    
    elif holandes.metros_r >=200:
        print("El Holandes Errante ha llegado a la meta... :(")
        perder()
        
    elif v3.gasolina <=0:
        print("Has perdido... Te has quedado sin aceite grasiento")
        perder()

    elif v3.resistencia <=0:
        print("El Holandes ha roto tu vehiculo... has perdido")
        perder()
        
    elif holandes.resistencia <=0:
        print("¡Has tumbado el barco del Holandes Errante! Enhorabuena")
        ganar()




