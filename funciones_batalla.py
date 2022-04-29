from sre_constants import SUCCESS
import utilidades as ut
import random,time

#funcion de utilizacion de items

def usar_item(jugador):

    okay = False
    
    if len(jugador.items) >0:

        ut.limpiar_pantalla()


        lista_items = list(jugador.items.values())
        print("\nTus items disponibles son los siguientes :\n")

        for index,value in enumerate(lista_items):

            print("Nombre item :",value.nombre,"\n",value.descripcion,"potencia del item : (",value.potencia,")\n","{",index,"}","\n")

        eleccion = int(input("introduce el item que queres usar por su numero : "))

        try:
            item_seleccionado = lista_items[eleccion]

        except Exception as e:
            print("error ! item no disponible o no existe")

        if item_seleccionado.tipo == "a":
            jugador.ataque += item_seleccionado.potencia
            okay = True
            del jugador.items[item_seleccionado.nombre]

        if item_seleccionado.tipo == "s":
            jugador.vida += item_seleccionado.potencia
            okay = True
            del jugador.items[item_seleccionado.nombre]

        # print(list(jugador.items.values())[0].nombre)
    else:
        print("no tenes items forro pelotudo !")

    if okay:
        print("Has equipado el item",item_seleccionado.nombre)

#funcion de batalla
def fight(jugador,villano):

    kapasao = 10

    while jugador.vida >0 and villano.vida >0:

        action = int(input("\n\n1--Ver stats villano\n\n2--Ver stats jugador\n\n3--Atacar villano\n\n4--Usar item\n\n5--huir\n\n- - - > "))

        if action == 1:

            ut.limpiar_pantalla()

            print(villano)

        if action == 2:

            ut.limpiar_pantalla()

            print(jugador)

        if action ==3:
            
            if random.random() < max((jugador.precision-villano.velocidad)/100,0.3): 

                j1,j2 = jugador,villano

            else:

                j1,j2 = villano,jugador

            for i in range(2):

                print("\n"+j1.nombre,"es mas veloz que",j2.nombre,"y le va a golpear primero\n")

                time.sleep(1)

                total_damage = j1.atacar(j2)

                print("\nEse golpe le ha quitado",total_damage,"de vida\n")

                j1,j2 = j2,j1

                # print(jugador.vida,villano.vida)
                if jugador.vida <=0:
                    return 0

                if villano.vida <=0:
                    return 1
        
        if action == 4:
            
            usar_item(jugador)

        if action == 5:
            break

    return kapasao
    