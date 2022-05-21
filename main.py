#importacion de modulos principales
import clases as cl,instanciaciones as ins,funciones_batalla as fb,utilidades as ut
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

            # if sp.mihilo_main_theme.estado:
            #     sp.mihilo_main_theme.start()
            
            # sp.mihilo_main_theme.estado = True

            print("\n\n\n\n\n    - - - - > Vamos a entrar dentro de alguna dimension...\n")

            time.sleep(4)

            index_dimension = random.randrange(0,len(ins.dimensiones))
            dimension_actual = ins.dimensiones[index_dimension]


            print("\n\n    - - - - > Vaya ! parece que hemos acabado en la dimension",dimension_actual.nombre,"\n")
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

                if ragnarok == 0:
                    print("\n\n    - - - - > Jugador",jugador.nombre,"derrotado de manera muy brutal\n")
                    time.sleep(3)
                    break
                elif ragnarok == 1:
                    print("\n\n    - - - - > Villano",villano_actual.nombre,"derrotado de manera muy brutal\n")
                    time.sleep(1.5)
                    jugador.puntos +=100
                    print(jugador.nombre," + 100 PTS !")
                    time.sleep(3)
                    del dimension_actual.villanos[index_villano]

            ut.cargando()

            if len(dimension_actual.villanos)==0:
                print("\nhas derrotado a todos los villanos de esta dimension...\n")
                ut.cargando()
                del ins.dimensiones[index_dimension]

        if len(ins.dimensiones) == 0:
            print("Enhorabuena,te has pasado el juego -- te has pasado el juego")
            print("puntos totales : ",jugador.puntos)
        else:
            print("te rascaron")
            print("puntos totales : ",jugador.puntos)
    else:
        
        print("error ! no puedes jugar si no es con un jugador valido\n")

    print("final while")

main()
