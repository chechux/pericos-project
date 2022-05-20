##import clases as cl


### ------------------------------------------------------------------------------------------------------
### ---------------------- El Claro de los Sueños
##
### ----------------- items
### ---------------------- ( a ) ataque
##cohete_propulsor = cl.Items("Cohete Propulsor","a",random.randrange(50,100),"Con este cohete haras mucho daño", 1 )
### ---------------------- ( s ) sanacion
##hada_lagrimas = cl.Items("lagrimas de Hada","s",random.randrange(15,30),"Esta bebida mejora la salud",1)
### ---------------------- ( a ) ataque
##red_pot = cl.Items("Bote Hoodlum Red","a",random.randrange(10,20),"Con la tecnologia hoodlum podras golpear más fuerte",1)
### ---------------------- ( sk ) 2 turnos
##yellow_pot = cl.Items("Bote Hoodlum Amarillo","sk",0,"Con la tecnologia hoodlum tienes un gorrocoptero para luchar otro dia",1)
### ---------------------- ( p ) precision
##green_pot = cl.Items("Bote Hoodlum Verde","p",30,"Con la tecnologia hoodlum tienes obtendrás mayor precision",1)

### ---------------------- villanos
###                     Nombre, Vida, Ataque, Defensa, Precision, Velocidad

##hoodlum = cl.Mob('Hoodlum', 100, 20, 20, 10, 20)
##dark_lum = cl.Mob('Lum Oscuro', 120,10,5,20,20)
##dark_rayman = cl.Mob('Rayma Oscuro',50,25,20,35,20)


### ---------------------- dimension
##dimension_claro_de_los_sueños = cl.Dimension("El Claro de los Sueños", [ cohete_propulsor, hada_lagrimas, red_pot, yellow_pot, green_pot], [ hoodlum, dark_lum, dark_rayman ] )
##

##----------------Habilidades
##golpe_cargado = cl.Habilidades("Golpe Cargado","normal", (15,30), " Golpe cargado de tipo normal que hace Rayman")
##golpe_envenenado = cl.Habilidades("Envenenamiento","veneno",(5,10),"Gracias a Leptys, Rayman puede envenenar a un enemigo")
##golpe_ocasional = cl.Habilidades("Golpe Ocasional","normal",(0,50),"Rayman reune energias para asestar un golpe que puede ser muy potente")
##

##hacker = cl.Jugador('Anonymus',150,45,50,50,25, [ golpe_cargado, golpe_envenenado,  golpe_ocasional ] )

didujo_hacker= '''
        
                                          █   █
                                    █               █
                                █                       █
                           █                                 █
                        █  ▄▀█     █▀▄    █
                     █                                             █
                ▐▌                  ▄▄                     █
                    █          ▀▄         ▄▀         █
                ▐██            ▀▀▀          ██▌
                   ▐██                               ██ 
            ▄████▄   ▌  ▄████▄

'''
print(didujo_hacker)

##    print("""
##---------------------------------------------------------------------------------------------
##
##    Nombre : {}                                          █    █
##                                                              █               █
##    Ataque : {}                                  █                        █
##                                                     █                                 █
##    Defensa : {}                        █  ▄▀█     █▀▄     █
##                                               █                                             █
##    Precision : {}                ▐▌                  ▄▄                  █
##                                               █         ▀▄         ▄▀        █
##    Velocidad : {}               ▐██           ▀▀▀         ██▌
##                                              ▐██                              ██ 
##    Descripcion : {}         ▄████▄   ▌  ▄████▄
##
##---------------------------------------------------------------------------------------------
##        """.format( hacker.nombre, hacker.ataque, hacker.defensa, hacker.precision, hacker.velocidad, hacker.descripcion))
##
##    
##    mihilo_mostrar_hacker = sp.Songhilo_jugadores()
##    mihilo_mostrar_hacker.set_song(homero.sonido) # Archivo La_purga.mp3
##    mihilo_mostrar_hacker.start()
##    del mihilo_mostrar_hacker
