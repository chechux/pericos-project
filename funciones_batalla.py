import utilidades as ut
import random,time

#funcion de duracion items

def check_duration_items(jugador):
    
    items_acabados = []

    #a los items que esten activos se les restan turnos y se comprueba si ya no quedan
    for value in jugador.items.values():
        if value.activo[0] == True:
            value.turnos -=1
        if value.turnos == 0:
            items_acabados.append(value.nombre)
            print("WARNING ! se te ha acabado el item :",value.nombre)

            #segun el tipo de item que sea,volvemos a la normalidad de la stat del jugador que se habia modificado
            if value.tipo == "a":
                jugador.ataque = value.activo[1]
                

    #si hay uno o mas items acabados se eliminan del inventario del jugador
    if len(items_acabados)>0:

        for item_acabado in items_acabados:
            del jugador.items[item_acabado]

#funcion de utilizacion de items

def usar_item(jugador):

    okay = False
    
    if len(jugador.items) >0:

        ut.limpiar_pantalla()

        lista_items =[]

        for item in jugador.items.values():
            if item.activo[0] == False:
                lista_items.append(item)

        print("\nTus items disponibles son los siguientes :\n")

        for index,value in enumerate(lista_items):

            print("Nombre item :",value.nombre,"\n"+value.descripcion,"potencia del item : (",value.potencia,")\n","{",index,"}","\n")

        eleccion = int(input("introduce el item que queres usar por su numero : "))


        try:
            item_seleccionado = lista_items[eleccion]

        except:
            print("error ! item no disponible o no existe")
            return None

        if item_seleccionado.tipo == "a":
            
            #guardamos el valor anterior de su ataque dentro de una posicion de la la lista (activo) para cuando acabe el efecto del item,volver a su estado incial
            jugador.items[item_seleccionado.nombre].activo.append(jugador.ataque)

            #le subimos el ataque al jugador con el valor del item (potencia)
            jugador.ataque += item_seleccionado.potencia

            #esta parte es importante,colocamos en la primera posicion de la lista (activo(que tiene cada item)) un True como que esta siendo utilizado
            #y de esta manera podamos empezar a restarle turnos de actuacion,hasta que se elimine el item de nuestro inventario
            jugador.items[item_seleccionado.nombre].activo[0] = True

            #ponemos okay como true si todo sale bien y para posterior trackeo
            okay = True
            print("se q no debo",jugador.items[item_seleccionado.nombre].activo)
            
        if item_seleccionado.tipo == "s":
            jugador.vida += item_seleccionado.potencia
            okay = True
            del jugador.items[item_seleccionado.nombre]

        # print(list(jugador.items.values())[0].nombre)
    else:
        print("no tenes items forro pelotudo !")

    if okay:
        print("Has equipado el item",item_seleccionado.nombre)
        return item_seleccionado.nombre

#funcion de batalla
def fight(jugador,villano):

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

            check_duration_items(jugador)

        if action == 4:
            
            usar_item(jugador)

        if action == 5:
            break

    