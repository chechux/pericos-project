#importacion de modulos principales
import clases as cl,instanciaciones as ins,funciones_batalla as fb,utilidades as ut
import sonidos_pantallas as sp

#importacion de modulos utiles
import random,time,os



# time.sleep(2)
# sp.mihilo_main_theme.stop_song()
def main(jugador):

    sp.mihilo_main_theme.start()

    if isinstance(jugador,cl.Jugador):

        jugador.set_items()

        sp.mihilo_main_theme.pause_song()

        while jugador.vida >0 and len(ins.dimensiones) > 0:

            sp.mihilo_main_theme.song.resume()

            # if sp.mihilo_main_theme.estado:
            #     sp.mihilo_main_theme.start()
            
            # sp.mihilo_main_theme.estado = True

            print("\nvamos a entrar dentro de alguna dimension...\n")

            time.sleep(1)

            index_dimension = random.randrange(0,len(ins.dimensiones))
            dimension_actual = ins.dimensiones[index_dimension]


            print("\nvaya ! parece que hemos acabado en la dimension",dimension_actual.nombre,"\n")

            time.sleep(1)

            for times in range(len(dimension_actual.villanos)):

                index_villano = random.randrange(0,len(dimension_actual.villanos)) #indice aleatorio para elegir villano aleatorio
                villano_actual = dimension_actual.villanos[index_villano]

                print("\nte vas a enfrentar a",villano_actual.nombre,"\n")

                time.sleep(1)

                sp.mihilo_main_theme.pause_song()

                ragnarok =fb.fight(jugador,villano_actual) 

                if ragnarok == 0:
                    print("jugador",jugador.nombre,"derrotado de manera muy brutal")
                    break
                elif ragnarok == 1:
                    print("\nvillano",villano_actual.nombre,"derrotado de manera muy brutal\n")
                    del dimension_actual.villanos[index_villano]

                ut.limpiar_pantalla()

            if len(dimension_actual.villanos)==0:
                print("\nhas derrotado a todos los villanos de esta dimension...\n")
                del ins.dimensiones[index_dimension]

        if len(ins.dimensiones) == 0:
            print("Enhorabuena,te has pasado el juego -- te has pasado el juego")
        else:
            print("te rascaron")
    else:
        
        print("error ! no puedes jugar si no es con un jugador valido\n")

    print("final while")

main(ins.homero)
