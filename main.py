#importacion de modulos principales
import clases as cl,instanciaciones as ins,funciones_batalla as fb,utilidades as ut
import mysql_whiteshark as mys
import funciones_admin as fad
import sonidos_pantallas as sp

#importacion de modulos utiles
import random,time,os



# time.sleep(2)
# sp.mihilo_main_theme.stop_song()
def main():

    sp.mihilo_main_theme.start()

    ut.inicio_juego()

    usuario = fad.que_jugador()

    sp.mihilo_main_theme.control_volumen(30)

    jugador = ins.elegir_jugador()
    
    ut.cargando()

    if isinstance(jugador,cl.Jugador):

        sp.mihilo_main_theme.control_volumen(100)

        fad.set_items(jugador)

        ut.cargando()

        sp.mihilo_main_theme.pause_song()

        while jugador.vida >0 and len(ins.dimensiones) > 0:

            sp.mihilo_main_theme.song.resume()

            print("\n\n\n\n\n    - - - - > Vamos a entrar dentro de alguna dimension...\n")
            time.sleep(4)

            index_dimension = random.randrange(0,len(ins.dimensiones))
            dimension_actual = ins.dimensiones[index_dimension]


            print("\n\n    - - - - > Vaya ! parece que hemos acabado en la dimension :",dimension_actual.nombre.upper(),"\n")
            time.sleep(3)

            for times in range(len(dimension_actual.villanos)):

                ut.cargando()

                index_villano = random.randrange(0,len(dimension_actual.villanos)) #indice aleatorio para elegir villano aleatorio
                villano_actual = dimension_actual.villanos[index_villano]

                print("\n\n\n\n\n    - - - - > Vaya ! Te vas a enfrentar a",villano_actual.nombre,"\n")

                time.sleep(3)

                ut.limpiar_pantalla()

                sp.mihilo_main_theme.pause_song()

                ragnarok =fb.fight(jugador,villano_actual) 

                sp.mihilo_main_theme.song.resume()

                if ragnarok == 0:

                    print("\n\n    - - - - > Jugador",jugador.nombre,"derrotado de manera muy brutal\n")
                    time.sleep(3)
                    break

                elif ragnarok == 1:

                    print("\n\n    - - - - > Villano",villano_actual.nombre,"derrotado de manera muy brutal\n")
                    time.sleep(1.5)

                    jugador.puntos +=100
                    jugador.enemigos_derrotados +=1

                    print("\n\n\n\n\n\n    - - - - >",jugador.nombre," + 100 PTS !")
                    time.sleep(3)

                    del dimension_actual.villanos[index_villano]

                elif ragnarok == 2:
                    ut.limpiar_pantalla()
                    print("\n\n\n\n\n\n    - - - - > Has huido del combate ! vamos hacia otra dimension...")
                    time.sleep(2.5)
                    break

            ut.cargando()

            if len(dimension_actual.villanos)==0:
                print("\n\n\n\n\n\n     - - - - > Has derrotado a todos los villanos de esta dimension...\n")
                time.sleep(4)
                ut.cargando()
                del ins.dimensiones[index_dimension]

        if len(ins.dimensiones) == 0:
            print("\n\n\n\n\n\n    - - - - > Enhorabuena -- Juego completado !")
            print("\n\n\n                  - - - - > puntos totales : ",jugador.puntos)
            print("\n\n\n                  - - - - > Enemigos derrotados : ",jugador.enemigos_derrotados)
            print("\n\n\n                  - - - - > Bosses derrotados : ",jugador.bosses_derrotados)
            try:
                mys.subir_datos_partida(jugador.nombre,jugador.puntos,jugador.enemigos_derrotados,jugador.bosses_derrotados)
            except:
                pass

        else:
            print("\n\n\n\n\n\n    - - - - > Te rascaron,hasta aqui has llegado... !!")
            print("\n\n\n                  - - - - > puntos totales : ",jugador.puntos)
            print("\n\n\n                  - - - - > Enemigos derrotados : ",jugador.enemigos_derrotados)
            print("\n\n\n                  - - - - > Bosses derrotados : ",jugador.bosses_derrotados)
            try:
                mys.subir_datos_partida(jugador.nombre,jugador.puntos,jugador.enemigos_derrotados,jugador.bosses_derrotados)
            except:
                pass

    else:
        
        print("error ! no puedes jugar si no es con un jugador valido\n")


main()
