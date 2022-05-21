import instanciaciones as ins,utilidades as ut
import time,random

def set_items(jugador):

    ut.limpiar_pantalla()

    print("\n\n\n\n\n    - - - - > A continuacion vas a elegir los items para",jugador.nombre)
    time.sleep(2)
    print()
    print()
    print("    - - - - > Solo puedes escoger 3 items para tu inventario y hay un total de 6 -- elige bien : \n\n")

    time.sleep(5)

    ut.limpiar_pantalla()

    items_aleatorios = []

    while len(items_aleatorios) != 6:
        item_random = ins.selec_items[random.randrange(0,len(ins.selec_items)-1)]

        if item_random not in items_aleatorios:
            items_aleatorios.append(item_random)

    for numero,item in enumerate(items_aleatorios):

            print()

            print()

            print(" "*7,item.nombre,"(",numero,")\n")

            print(" "*7,item.descripcion,"\n\n")

            time.sleep(.7)

    while len(jugador.items)<3:

        try:

            eleccion = int(input("       Escribe el numero del item para equiparlo : "))

            if items_aleatorios[eleccion].nombre in jugador.items:

                print("\n\n       No ! Este Item ya lo tienes equipado...")

                time.sleep(1)

                ut.limpiar_pantalla()

            else:

                jugador.items[items_aleatorios[eleccion].nombre] = items_aleatorios[eleccion]

                print("\n\n\n       item",items_aleatorios[eleccion].nombre,"equipado con exito a",jugador.nombre)
            
                time.sleep(1.5)
                            
                ut.limpiar_pantalla()

        except Exception as e:
            print("       error! numero de item no disponible :",e)

            time.sleep(1.5)

        ut.limpiar_pantalla()
        for numero,item in enumerate(items_aleatorios):

            print()
            
            print()

            print(" "*7,item.nombre,"(",numero,")\n")

            print(" "*7,item.descripcion,"\n\n")

def que_jugador():
    ut.cargando()
    nombreuser = input("\n\n\n\n\n\n\n\n\n\n\n\n    - - - - > Introduce tu NICK : ")
    time.sleep(1)
    print("\n\n    - - - - > Perfecto ! tu NICK es : ",nombreuser)
    time.sleep(1.5)
    return nombreuser