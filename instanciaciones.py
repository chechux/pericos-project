import clases as cl,sonidos_pantallas as sp
import random
#Dimension C-137 

    #items

#los items de tipo sk sirven para tener 2 turnos seguidos,es decir,que el rival se pierda su tuno por alguna rzon
pistola_portales = cl.Items("Pistola de portales","sk",0,"con la pistola de portales de rick te vas a la dimension 35 en tal de esquivar el golpe y vuelve a ser tu turno !",1)
#los items de tipo ataque incrementan la fuerza
espada_bacon = cl.Items("Espada bacon","a",random.randrange(10,25),"con esta ridicula y sabrosa espada aumenta tu fuerza !",1)
#los items de tipo sanacion incrementan la vida
cuencas_de_ojos = cl.Items("Cuencas de ojos","s",random.randrange(10,25),"con estos deliciosas y asquerosas cuencas de ojos aumenta tu salud !",1)
#los items de tipo precicison incrementan la precision,obviamente
parche_de_morty = cl.Items("Parche de morty","p",30,"con este parche de morty te vuelves mas audaz y tu precision aumenta",1)
#los items

    #villanos

abradolf_lincler = cl.Mob("abradolf lincler",100,5,5,50,100)
asustadizo_terry = cl.Mob("asustadizo terry",100,5,5,50,10)
bola_de_nieve = cl.Mob("bola de nieve",100,5,5,50,10)

    #dimension

dimension_c137 = cl.Dimension("C-137",[pistola_portales,espada_bacon,cuencas_de_ojos,parche_de_morty],[abradolf_lincler,asustadizo_terry,bola_de_nieve])


    #Dimension Fondo de bikini

#items

#sk
savia_gary=("SaviGary","sk",0,"tirale savia de gary a tu rival para que no pueda atacar durante un turno!",1)

#ataque
caza_medusas = cl.Items("CazaMedusas 3000", "a", random.randrange(10,25),"Con el nuevo modelo CazaMedusas aumenta tu daño!",1)
espatula = cl.Items("Espatula de Oro","a",random.randrange(20,25),"el arma legendaria de Bobesponja! calcina a tus rivales.",1)#legendaria

#sanacion
bote_burbujas = cl.Items("Burbujeitor","s",random.randrange(10,25),"rociate de este jabon burbujeante para recuperar salud!",1)
cangreburguer = cl.Items("BurguerCangreburguer","s",random.randrange(20,25), "comete esta delicia para quedarte como nuevo!",1)#legendaria

#precision
gafas = cl.Items("Lectometor","p",30,"ponte estas gafas de lectura para aumentar tu precision",1)



#villanos

patricio=cl.Mob("Patricio Estrella",100,5,10,50,7)
arenita=cl.Mob("Arenita Mejillas",100,10,5,70,10)
placton=cl.Mob("Placton",80,10,5,90,10)
calamardo=cl.Mob("Calamardo",100,5,5,50,10)


#dimension

dimension_fondo_de_bikini = cl.Dimension("Fondo de bikini",[savia_gary, caza_medusas, espatula, bote_burbujas, cangreburguer, gafas],[patricio, arenita, placton, calamardo])


        
               
        #jugadores

    #habilidades homero

bola_demolicion = cl.Habilidades("Bola de demolicion","normal",(10,20),"golpe de tipo normal con la bola de demolicion con la que homer se queria tirar")
donut_envenenado = cl.Habilidades("Donut envenenado","veneno",(5,10),"donut de tipo veneno que quitará vida paulatinamente")
golpe_borracho = cl.Habilidades("Golpe borracho","normal",(0,50),"golpe de tipo normal que puede quitar muy poco o mucho debido a la borrachera de homer")


homero = cl.Jugador("homero",100,40,50,50,20,"Este jugador tiene habilidades muy variopintas y curiosas !",4,[bola_demolicion,donut_envenenado,golpe_borracho])

homero_ascii= """  
                                                                                            &              
                                                                                         .-"`"-.
                                                                                        /       \\                 
                                                                                        |   __  _|
                                                                                        |  /  \/ \\
                                                                                       WW  \_o/_o/
                                                                                        (        _)
                                                                                        |   .----\\
                                                                                        ;  | '----'
                                                                                        \__'--;`
                                                                                        |___/\|
            """
# print(homero_ascii)
# print(nn)



dimensiones = [dimension_c137,dimension_fondo_de_bikini]



#mostrar a cada jugador

def  mostrar_homero():
    print("""
---------------------------------------------------------------------------------------------
                                                                                    &              
    ataque : {}                                                                  .-"`"-.
                                                                                /       \\                 
    defensa : {}                                                                |   __  _|
                                                                                |  /  \/ \\
    precision : {}                                                             WW  \_o/_o/
                                                                                (        _)
    velocidad : {}                                                              |   .----\\
                                                                                ;  | '----'
    descripcion : {}   \__'--;`
                                                                                |___/\|
---------------------------------------------------------------------------------------------
        """.format(homero.ataque,homero.defensa,homero.precision,homero.velocidad,homero.descripcion))
    
    mihilo_mostrar_homer = sp.Songhilo_jugadores()
    mihilo_mostrar_homer.set_song("/Users/zaslake/Desktop/2/programacion/python/abril2022/periko/recursos/manazas2.m4a")
    mihilo_mostrar_homer.start()
    del mihilo_mostrar_homer
    

mostrar_homero()