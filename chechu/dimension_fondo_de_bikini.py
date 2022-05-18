import clases as cl,sonidos_pantallas as sp
import time
import random
###Dimension Fondo de bikini###

##items

#sk
savia_gary=("SaviGary","sk",0,"Tirale savia de gary a tu rival para que no pueda atacar durante un turno!",1)

#ataque
caza_medusas = Items("CazaMedusas 3000", "a", random.randrange(10,25),"Con el nuevo modelo CazaMedusas aumenta tu daño!",1)
espatula = Items("Espatula de Oro","a",random.randrange(20,25),"El arma legendaria de Bobesponja! calcina a tus rivales.",1)#legendaria

#sanacion
bote_burbujas = Items("Burbujeitor","s",random.randrange(10,25),"Rociate de este jabon burbujeante para recuperar salud!",1)
cangreburguer = Items("BurguerCangreburguer","s",random.randrange(20,25), "Cómete esta delicia para quedarte como nuevo!",1)#legendaria

#precision
gafas = Items("Lectometor","p",30,"Ponte estas gafas de lectura para aumentar tu precision",1)



##villanos

patricio=Mob("Patricio Estrella",100,5,10,50,7)
arenita=Mob("Arenita Mejillas",100,10,5,70,10)
placton=Mob("Placton",80,10,5,90,10)
calamardo=Mob("Calamardo",100,5,5,50,10)

##habilidades

golpe_cubo = Habilidades("Comida Podrida","veneno",(5,10),"Envenena a tu enemigo con comida del cubo de cebo, ¡puaaaaaj!")
golpe_trucado = Habilidades("¿Hay trampa?","normal",(0,50),"Ha bobesponja le ha crecido el brazo sorprendentemente, pero... no parece muy estable")
golpe_ancla = Habilidades("Golpe ancla","normal",(10,20),"¡Lenate de valor y zúrrale una buena a tu rival!")
golpe_condimento = Habilidades("Golpe condimento","normal",(10,20), "Disparale a tu oponente pero, con mucha salsa")


##dimension

dimension_fondo_de_bikini = Dimension("Fondo de bikini",[savia_gary, caza_medusas, espatula, bote_burbujas, cangreburguer, gafas,
                                      patricio, arenita, placton, calamardo])


fdb = [dimension_fondo_de_bikini]


 ##jugador                   


bob = Jugador("Bobesponja",100,30,80,80,20,"¡Este jugador es muy escurridizo, rápido y el mejor cocinero de todas las dimensiones!","./recursos/risa.mp3",
              [comida_cubo, golpe_trucado, golpe_ancla, golpe_condimento])

def mostrar_bob():
    print("""

---------------------------------------------------------------------------------------------

        Nombre: {}                                                                                    
                                                                                            .--..--..--..--..--..--.                                                                     
        Ataque : {}                                                                  |(_.'  |    /    .-\-.  \   |
                                                                                         \     0|    |   ( O| O)   |                                                                                                            
        Defensa : {}                                                                  \ (_) | o         -` .-`   |
                                                                                             |    \   |`-._ _ _ _ _ \ /
        Precision : {}                                                                  \    |   |  `. |_||_|     |
                                                                                              | o  |    \_      \      |       
        Velocidad : {}                                                                  |     \     `--..-'   O |  
                                                                                                    |     `-.-'      /-.__         
        Descripcion : {}
        
---------------------------------------------------------------------------------------------

""". format(bob.nombre, bob.ataque, bob.defensa, bob.precision, bob.velocidad, bob.descripcion))


mihilo_mostrar_bob = sp.Songhilo_jugadores()
mihilo_mostrar_bob.set_song(bob.sonido)
mihilo_mostrar_bob.start()
del mihilo_mostrar_bob

mostrar_bob()


