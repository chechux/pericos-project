import clases as cl
import sonidos_pantallas as sp
import utilidades as ut
import random,time
#Dimension C-137 

    #items

#los items de tipo sk sirven para tener 2 turnos seguidos,es decir,que el rival se pierda su tuno por alguna rzon
pistola_portales = cl.Items("Pistola de portales","sk",0,"con la pistola de portales de rick te vas a la dimension 35 en tal de esquivar el golpe y vuelve a ser tu turno !",1)
#los items de tipo ataque incrementan la fuerza
espada_bacon = cl.Items("Espada bacon","a",20,"con esta ridicula y sabrosa espada aumenta tu fuerza !",2)
#los items de tipo sanacion incrementan la vida
cuencas_de_ojos = cl.Items("Cuencas de ojos","s",15,"con estos deliciosas y asquerosas cuencas de ojos aumenta tu salud !",1)
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
savia_gary=cl.Items("SaviGary","sk",0,"tirale savia de gary a tu rival para que no pueda atacar durante un turno!",1)

#ataque
caza_medusas = cl.Items("CazaMedusas 3000", "a", 15,"Con el nuevo modelo CazaMedusas aumenta tu daño!",2)
espatula = cl.Items("Espatula de Oro","a",30,"el arma legendaria de Bobesponja! calcina a tus rivales.",1)#legendaria

#sanacion
bote_burbujas = cl.Items("Burbujeitor","s",10,"rociate de este jabon burbujeante para recuperar salud!",1)
cangreburguer = cl.Items("BurguerCangreburguer","s",15, "comete esta delicia para quedarte como nuevo!",1)#legendaria

#precision
gafas = cl.Items("Lectometor","p",30,"ponte estas gafas de lectura para aumentar tu precision",1)



#villanos

patricio=cl.Mob("Patricio Estrella",100,5,10,50,7)
arenita=cl.Mob("Arenita Mejillas",100,10,5,70,10)
placton=cl.Mob("Placton",80,10,5,90,10)
calamardo=cl.Mob("Calamardo",100,5,5,50,10)


#dimension

dimension_fondo_de_bikini = cl.Dimension("Fondo de bikini",[savia_gary, caza_medusas, espatula, bote_burbujas, cangreburguer, gafas],[patricio, arenita, placton, calamardo])



### ------------------------------------------------------------------------------------------------------
### ---------------------- El Claro de los Sueños
##
# ----------------- items
# ---------------------- ( a ) ataque
cohete_propulsor = cl.Items("Cohete Propulsor","a",20,"Con este cohete haras mucho daño", 1 )
# ---------------------- ( s ) sanacion
hada_lagrimas = cl.Items("lagrimas de Hada","s",10,"Esta bebida mejora la salud",1)
# ---------------------- ( a ) ataque
red_pot = cl.Items("Bote Hoodlum Red","a",15,"Con la tecnologia hoodlum podras golpear más fuerte",1)
# ---------------------- ( sk ) 2 turnos
yellow_pot = cl.Items("Bote Hoodlum Amarillo","sk",0,"Con la tecnologia hoodlum tienes un gorrocoptero para luchar otra vez",1)
# ---------------------- ( p ) precision
green_pot = cl.Items("Bote Hoodlum Verde","p",30,"Con la tecnologia hoodlum tienes obtendrás mayor precision",1)

# ---------------------- villanos
#                     Nombre, Vida, Ataque, Defensa, Precision, Velocidad

hoodlum = cl.Mob('Hoodlum', 100, 10, 20, 10, 20)
dark_lum = cl.Mob('Lum Oscuro', 120,10,5,20,20)
dark_rayman = cl.Mob('Rayma Oscuro',50,25,20,35,20)


# ---------------------- dimension
dimension_claro_de_los_sueños = cl.Dimension("El Claro de los Sueños", [ cohete_propulsor, hada_lagrimas, red_pot, yellow_pot, green_pot], [ hoodlum, dark_lum, dark_rayman ] )



               
        #jugadores

    #homero

bola_demolicion = cl.Habilidades("Bola de demolicion","normal",(10,20),"golpe de tipo normal con la bola de demolicion con la que homer se queria tirar")
donut_envenenado = cl.Habilidades("Donut envenenado","veneno",(5,10),"donut de tipo veneno que quitará vida paulatinamente")
golpe_borracho = cl.Habilidades("Golpe borracho","normal",(0,50),"golpe de tipo normal que puede quitar muy poco o mucho debido a la borrachera de homer")


homero = cl.Jugador("homero",30,40,50,50,20,"Este jugador tiene habilidades muy variopintas y curiosas !","./recursos/manazas2.mp3",[bola_demolicion,donut_envenenado,golpe_borracho])

        #hacker

golpe_cargado = cl.Habilidades("Golpe Cargado","normal", (15,30), " Golpe cargado de tipo normal que hace Rayman")
golpe_envenenado = cl.Habilidades("Envenenamiento","veneno",(5,10),"Gracias a Leptys, Rayman puede envenenar a un enemigo")
golpe_ocasional = cl.Habilidades("Golpe Ocasional","normal",(0,50),"Rayman reune energias para asestar un golpe que puede ser muy potente")


hacker = cl.Jugador('Anonymus',100,45,50,50,25,"Este gran hacker es siniestro !","./recursos/La_purga.mp3", [ golpe_cargado, golpe_envenenado,  golpe_ocasional ] )

print(homero)


jugadores = [homero,hacker]

dimensiones = [dimension_c137,dimension_fondo_de_bikini,dimension_claro_de_los_sueños]

        #items totales

selec_items = [
    
    cl.Items("aceite_gines","s",random.randrange(15,20),"bebete este aceite colesterolientico para tener fuerza pa echar un ratejo mas en la batalla",3),
    cl.Items("poco_pan","a",random.randrange(5,10),"con el poder del poco pan de patica tendras un poco mas de fuerza",3),
    cl.Items("porro_perroviejo","p",random.randrange(50,80),"con este porro de perroviejo te concentraras mucho mas y tu precision sube",1),

    cohete_propulsor,hada_lagrimas,green_pot,yellow_pot,red_pot,

    savia_gary,cangreburguer,caza_medusas,espatula,gafas,bote_burbujas,

    parche_de_morty,espada_bacon,cuencas_de_ojos,pistola_portales

]


#mostrar a cada jugador

def  mostrar_homero():
    print("""
---------------------------------------------------------------------------------------------
    Nombre : {}
                                                                                    &              
    Ataque : {}                                                                  .-"`"-.
                                                                                /       \\                 
    Defensa : {}                                                                |   __  _|
                                    ( 1 )                                       |  /  \/ \\             ░░███╗░ 
    Precision : {}                                                             WW  \_o/_o/             ░████║░
                                                                                (        _)            ██╔██║░
    Velocidad : {}                                                              |   .----\\                ██║░░
                                                                                ;  | '----'            ███████╗
    Descripcion : {}   \__'--;`               ╚══════╝
                                                                                |___/\|
---------------------------------------------------------------------------------------------
        """.format(homero.nombre,homero.ataque,homero.defensa,homero.precision,homero.velocidad,homero.descripcion))
    
    mihilo_mostrar_homer = sp.Songhilo_jugadores()
    mihilo_mostrar_homer.set_song(homero.sonido)
    mihilo_mostrar_homer.start()
    del mihilo_mostrar_homer

<<<<<<< HEAD
mostrar_homero()
=======

def mostrar_hacker():
    print("""
---------------------------------------------------------------------------------------------

    Nombre : {}                                            
                                                            ▄ ▀▀ ▀▀ ▄
    Ataque : {}                                           █           █
                                                        █               █
    Defensa : {}                                      █                   █
                                                    █    ▄▀▀▀█    █▀▀▀▄    █
    Precision : {}                                 █                        █
                                                 ▐▌      ▄▄    ▀▀▀    ▄▄     █
                                                   █       ▀▀▀     ▀▀▀      █
    Velocidad : {}                                   █         ▀▀▀         █
                                                     ▐██                 ██
    Descripcion : {}    ▄████▄    ▀▀▀   ▄████▄
---------------------------------------------------------------------------------------------
        """.format( hacker.nombre, hacker.ataque, hacker.defensa, hacker.precision, hacker.velocidad, hacker.descripcion))


    mihilo_mostrar_hacker = sp.Songhilo_jugadores()
    mihilo_mostrar_hacker.set_song(hacker.sonido) # Archivo La_purga.mp3
    mihilo_mostrar_hacker.start()
    del mihilo_mostrar_hacker


def elegir_jugador():
    ut.limpiar_pantalla()
    print()
    print()
    print()
    print("    - - > A continuacion vas a elegir un personaje para jugar...")
    time.sleep(3)

    ut.limpiar_pantalla()

    mostrar_homero()
    time.sleep(16)

    mostrar_hacker()
    time.sleep(6)

    print();print()
    while True:
        try:
            eleccion_user = int(input("- - - - > "))
            return jugadores[eleccion_user-1]
        except IndexError:
            print("No existe ningun personaje con ese numero...")
            time.sleep(1.5)
        except ValueError:
            print("Solo numeros,no texto o otro tipo de caracteres...")
            time.sleep(1.5)

# elegir_jugador() 
>>>>>>> 4ab59824b4dca4745021d6c2064f1c77b5964aa1
