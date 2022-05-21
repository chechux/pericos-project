import time
import random
###MINIJUEGO###
def Minijuego_carrera():
    
    print("-->JUAJUAJUJUAJUA")
    time.sleep(1.5)
    print("-->¡Que mala suerte grumete! te has topado con el mismisimo e insuperable...")
    time.sleep(2)
    print("-->¡HOLANDES ERRANTE!")
    time.sleep(0.5)
    print("""
         ( " ")
       /\_.' '._/\
    \   
       |         |
        \       /
         \    /`
       (__)  /
         `.__.'
    """)
    time.sleep(1.5)
    print("-->JUAJUAJUUAJUAJU")
    time.sleep(1)
    print("-->¡Ahora tendras que enfrentarte a mi en una carrera encarnizada!")
    time.sleep(3)
    print("Elige tu vehiculo:")
    print("")
    time.sleep(1.5)
                                  

    class Vehiculo():
        def __init__(self,nombre,velocidad,daño,resistencia,gasolina,metros_r=0,kit=1):
            self.nombre=nombre
            self.velocidad=velocidad
            self.daño=daño
            self.resistencia=resistencia
            self.gasolina=gasolina
            self.metros_r=metros_r
            self.kit=kit

            def __str__(self):
                    return self.nombre.upper() + ":\n-Velocidad:" + str(self.velocidad) + "\n-Daño:" + str(self.daño) + "\n-Resistencia:" + str(self.resistencia) + "\n-Gasolina:" + str(self.gasolina)


        def avanzar(self):
            metrosa = (random.randrange(1,7) * self.velocidad)/2
            self.metros_r+=metrosa
            self.gasolina-=random.randrange(5,15)
            pro_kit=random.randrange(1,25)

            print(self.nombre, "avanza", metrosa,"metros, en total has avanzado",self.metros_r,"metros, te quedan", self.gasolina,"litros de aceite grasiento.")
            print("")
            time.sleep(0.7)
            if self.gasolina < 30:
                time.sleep(1)
                print("¡CUIDADO!, Te quedan", self.gasolina, " litros de aceite grasiento, deberias repostar...")
                print("")
                time.sleep(0.7)
            if pro_kit == 2:
                print("!WOW¡ te has encontrado un kit de reparacion en el garaje del Señor Cangrejo")
                print("")
                self.kit+=1
                time.sleep(0.7)

        def avanzarh(self):
            metrosa = (random.randrange(1,7) * self.velocidad)/2
            self.metros_r+=metrosa
            self.gasolina-=random.randrange(5,15)
            print(self.nombre, "ha avanzado", metrosa,"metros, en total ha avanzado",self.metros_r, "metros, le quedan" , self.gasolina,"litros de aceite grasiento.")
            time.sleep(0.7)
            pro_kit=random.randrange(1,25)
            if pro_kit == 2:
                print("El Holandes le ha robado un kit de reparacion al Señor Cangrejo")
                self.kit+=1
                time.sleep(1)

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
            print("¡Repostado! ahora tienes", self.gasolina, "litros de aceite grasiento.")
            print("")
            time.sleep(0.7)

        def repostarh(self):
            gasolinar=random.randrange(10,30)
            self.gasolina +=gasolinar
            time.sleep(1)
            print("El Holandes ha repostado aceite grasiento.")
            time.sleep(1)
    
    
        def atacar(self,holandes):
            dañor = random.randrange(1,self.daño)
            holandes.resistencia -=dañor
            print(self.nombre," ataca, logrando", dañor,"puntos de daño, le quedan", holandes.resistencia,"puntos de vida al Holandes.")
            print("")
            time.sleep(0.7)
            if dañor > self.daño-3:
                print("¡GOLPE CRÍTICO!, golpeas dos veces seguidas.")
                print("""

                  _ ._  _ , _ ._
                (_ ' ( `  )_  .__)
               ( (  (    )   `)  ) _)
              (__ (_   (_ . _) _) ,__)
                 `~~`\ ' . /`~~`
                          ;   ;  
                         /   \\
    _____________/_ __ \_____________

    """)
                time.sleep(1)
                print("--> ARRGHH ¡MALDITA ESPONJA!")
                time.sleep(0.7)
                return True
            else:
                return False

        def atacarc(self,holandes):
            dañor = random.randrange(1,self.daño)
            holandes.resistencia -=dañor
            print(self.nombre," vuelve a atacar, logrando",dañor,"puntos de daño, le quedan",holandes.resistencia,"puntos de vida.")
            print("")
            time.sleep(0.7)


        def atacarh(self,v):
            dañor = random.randrange(1,self.daño)
            v.resistencia -=dañor
            print(self.nombre," ataca, logrando",dañor,"puntos de daño, te quedan",v.resistencia,"puntos de vida.")
            time.sleep(1)
            if dañor > self.daño-3:
                print("¡GOLPE CRÍTICO!, el Holandes te golpea dos veces...")
                print("""
                  _ ._  _ , _ ._
                (_ ' ( `  )_  .__)
               ( (  (    )   `)  ) _)
              (__ (_   (_ . _) _) ,__)
                 `~~`\ ' . /`~~`
                          ;   ;  
                         /   \\
    _____________/_ __ \_____________
    """)
                time.sleep(1.3)
                dañor = random.randrange(1,self.daño)
                v.resistencia -=dañor
                print(self.nombre," ataca, logrando", dañor,"puntos de daño, te quedan", v.resistencia,"puntos de vida.")
                time.sleep(0.5)
                print("--> JUAJUAJUA ¡PRINGAO!")
                time.sleep(1)
            if v.resistencia < 20:
                time.sleep(0.5)
                print("¡WARNING!, te quedan",v.resistencia, "puntos de resistencia, deberias reparar el vehiculo")
                time.sleep(1)

        def curar(self):       
            if self.kit >=1:
                self.kit-=1
                self.resistencia+=15
                print("Reparando...")
                print("""
     /(  ___________
    |  >:===========`
    )(
    ""
    """)
                time.sleep(2)
                print("¡Reparado! ahora tienes",self.resistencia ,"puntos de resistencia, te quedan",self.kit, "kits de reparacion")
                print("")
                time.sleep(0.7)
            else:
                time.sleep(0.5)
                print("¡No te quedan kits de reparación! encuentrate alguno avanzando")
                print("")
                time.sleep(0.7)

        def curarh(self):
            if self.kit >=1:
                self.kit-=1
                self.resistencia+=10
                time.sleep(1)
                print("El Holandes ha reparado su vehiculo")
                time.sleep(0.7)
            else:
                pass                   

        def azar(self,z):
            metodo=random.randint(1,2)
            if metodo == 1:
                 holandes.atacarh(z)
            elif metodo == 2:
                holandes.avanzarh()

        def desc(self,holandes):
            print(self.nombre.upper())
            print("--------------------")
            print("-Metros recorridos:", self.metros_r,"\n-Vida:",self.resistencia,"\n-Gasolina:", self.gasolina,"\n-Kits:",self.kit)
            print("")
            print(holandes.nombre.upper())
            print("--------------------")
            print("-Metros recorridos:", holandes.metros_r,"\n-Vida:",holandes.resistencia,"\n-Gasolina:", holandes.gasolina,"\n-Kits:",holandes.kit)
            time.sleep(0.7)
                

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
        return True

    def perder():
        print("""
                    ┏┓      ┏━━━┓┏━━━┓┏━━━┓
                    ┃┃      ┃┏━┓┃┃┏━┓┃┃┏━━┛
                    ┃┃      ┃┃  ┃┃┃┗━━┓┃┗━━┓
                    ┃┃  ┏┓┃┃  ┃┃┗━━┓┃┃┏━━┛
                    ┃┗━┛┃┃┗━┛┃┃┗━┛┃┃┗━━┓
                    ┗━━━┛┗━━━┛┗━━━┛┗━━━┛
    """)
        return False


    ##velocidad,daño,resistencia,gasolina

    holandes=Vehiculo("Barco del holandes errante",10,15,100,100)
    v1=Vehiculo("coche de la señorita puff",10,10,90,90)
    v2=Vehiculo("Gary",7,10,150,150)
    v3=Vehiculo("casa de bobesponja",15,17,80,75)



    print(v1.nombre.upper(),"\n-Velocidad:", v1.velocidad,"\n-Daño:",v1.daño,"\n-Resistencia:",v1.resistencia,"\n-Gasolina:",v1.gasolina)
    print("----------------------")
    print(v2.nombre.upper(),"\n-Velocidad:", v2.velocidad,"\n-Daño:",v2.daño,"\n-Resistencia:",v2.resistencia,"\n-Gasolina:",v2.gasolina)
    print("----------------------")
    print(v3.nombre.upper(),"\n-Velocidad:", v3.velocidad,"\n-Daño:",v3.daño,"\n-Resistencia:",v3.resistencia,"\n-Gasolina:",v3.gasolina)
    print("")
    print("")
    print("-------- BOSS STATS--------")
    print(holandes.nombre.upper(),"\n-Velocidad:", holandes.velocidad,"\n-Daño:",holandes.daño,"\n-Resistencia:",holandes.resistencia,"\n-Gasolina:",holandes.gasolina)
    print("")
    print("REGLAS: \nPulsa 1 para avanzar x metros. \nPulsa 2 para repostar aceite grasiento. \nPulsa 3 para atacar al Holandes Errante. \nPulsa 4 para ver las stats acutales. \nPulsa 5 para reparar tu vehiculo 15 puntos.")
    print("")
    time.sleep(1.5)
    print("!Llega a los 200 metros o destruye el vehiculo enemigo para ganar!")
    print("")
    print("(el vehiculo se elige poniendo 'v' y el numero del vehiculo por orden)")

    eleccion=input("-->")    

    if eleccion == "v1":
        print(v1.nombre," ¡Buena elecion!")
        time.sleep(1)
        v1.empezar()
        time.sleep(0.5)
        
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
            print("")
            accion=int(input("¿que vas a hacer?: \n.1-Avanzar. \n2.-Repostar. \n3.-Atacar. \n4.-Stats. \n5.-Reparar. \n-->"))
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
                    if holandes.resistencia <= 15:
                        holandes.curarh()
                    elif holandes.gasolina < 20:
                        holandes.repostarh()
                    else:
                        holandes.azar(v1)
                        
            if accion == 4:
                v1.desc(holandes)

            if accion == 5:
                v1.curar()
                holandes.azar(v1)
                

        if v1.metros_r >=200:
            print("¡¡¡Enhorabuena!!! has llegado a la meta antes que el Holandes Errante :)")
            ganar()
        
        elif holandes.metros_r >=200:
            print("El Holandes Errante ha llegado a la meta... :(")
            perder()

        elif v1.gasolina <=0:
            print("Has perdido... Te has quedado sin aceite grasiento.")
            perder()
            
        elif v1.resistencia <=0:
            print("El Holandes ha roto tu vehiculo... has perdido")
            perder()

        elif holandes.resistencia <=0:
            print("¡Has tumbado el barco del Holandes Errante! Enhorabuena.")
            ganar()
                




    if eleccion == "v2":
        print(v2.nombre, "¡Buena eleccion!")
        time.sleep(1)
        v2.empezar()
        time.sleep(0.5)
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
            accion=int(input("¿que vas a hacer?:\n.1-Avanzar. \n2.-Repostar. \n3.-Atacar. \n4.-Stats. \n 5.-Reparar. \n-->"))
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
                    if holandes.resistencia <= 15:
                        holandes.curarh()
                    if holandes.gasolina < 20:
                        holandes.repostarh()
                    else:
                        holandes.azar(v2)

                        
            if accion == 4:
                v2.desc(holandes)

            if accion == 5:
                v2.curar()
                holandes.azar(v1)
                        
        if v2.metros_r >=200:
            print("¡¡¡Enhorabuena!!! has ganado al Holandes Errante :)")
            ganar()
        
        elif holandes.metros_r >=200:
            print("El Holandes Errante ha llegado a la meta... :(")
            perder()

        elif v2.gasolina <=0:
            print("Has perdido... Te has quedado sin aceite grasiento.")
            perder()

        elif v2.resistencia <=0:
            print("El Holandes ha roto tu vehiculo... has perdido.")
            perder()
            
        elif holandes.resistencia <=0:
            print("¡Has tumbado el barco del Holandes Errante! Enhorabuena.")
            ganar()




            
    if eleccion == "v3":
        print(v3.nombre, "!Buena eleccion")
        time.sleep(1)
        v3.empezar()

        
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
            accion=int(input("¿que vas a hacer?: \n.1-Avanzar. \n2.-Repostar. \n3.-Atacar. \n4.-Stats. \n 5.-Reparar. \n -->"))
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
                    if holandes.resistencia <= 15:
                        holandes.curarh()
                    if holandes.gasolina < 20:
                        holandes.repostarh()
                    else:
                        holandes.azar(v3)

            if accion == 4:
                v3.desc(holandes)

            if accion == 5:
                v3.curar()
                holandes.azar(v1)
                        

        if v3.metros_r >=200:
            print("¡¡¡Enhorabuena!!! has ganado al Holandes Errante :)")
            ganar()
        
        elif holandes.metros_r >=200:
            print("El Holandes Errante ha llegado a la meta... :(")
            perder()
            
        elif v3.gasolina <=0:
            print("Has perdido... Te has quedado sin aceite grasiento.")
            perder()

        elif v3.resistencia <=0:
            print("El Holandes ha roto tu vehiculo... has perdido.")
            perder()
            
        elif holandes.resistencia <=0:
            print("¡Has tumbado el barco del Holandes Errante! Enhorabuena.")
            ganar()

                                                                                                                                                                                                                ##      .--..--..--..--..--..--.
                                                                                                                                                                                                           ##    .' \  (`._   (_)     _   \
print(Minijuego_carrera())                                                                                                                                                                                                              ##  .'    |  '._)         (_)  |
                                                                                                                                                                                                                ##  \ _.')\      .----..---.   /
                                                                                                                                                                                                                ##  |(_.'  |    /    .-\-.  \  |
                                                                                                                                                                                                                ##  \     0|    |   ( O| O) | o|
                                                                                                                                                                                                                ##   |  _  |  .--.____.'._.-.  |
                                                                                                                                                                                                                ##   \ (_) | o         -` .-`  |
                                                                                                                                                                                                                ##    |    \   |`-._ _ _ _ _\                                                                                                                                                                                                                ##    \    |   |  `. |_||_|   |
                                                                                                                                                                                                                ##    | o  |    \_      \     |     -.   .-.
                                                                                                                                                                                                                ##    |.-.  \     `--..-'   O|     `.`-' .'
                                                                                                                                                                                                                ##  _.'  .' |     `-.-'      /-.__   ' .-'
                                                                                                                                                                                                                ##.' `-.` '.|='=.='=.='=.='=|._/_ `-'.'
                                                                                                                                                                                                                ##`-._  `.  |________/\_____|    `-.'
                                                                                                                                                                                                                ##   .'   ).| '=' '='\/ '=' |
                                                                                                                                                                                                                ##   `._.`  '---------------'
                                                                                                                                                                                                                ##           //___\   //___\
                                                                                                                                                                                                                ##             ||       ||
                                                                                                                                                                                                                ##               ||_.-.   ||_.-.
