import utilidades as ut
import random,time
import sonidos_pantallas as sp
    #funciones de habilidades

#funcion de elegir habilidad

def elegir_habilidad(jugador):

    ut.limpiar_pantalla()

    print("\n\nElige una habilidad para utilizar : \n\n")

    for index,habilidad in enumerate(jugador.habilidades):

        time.sleep(.5)

        print(habilidad.nombre,":",habilidad.descripcion,"\n")
        print("tipo :",habilidad.tipo,"potencia :",habilidad.potencia,"{",index,"}\n\n")

    while True:
    
        habilidad_user = int(input("- - - > "))

        try:
            jugador.habilidades[habilidad_user]
            return habilidad_user
        except:
            print("error ! habilidad no existente")
            time.sleep(1)
            
    #quiero crear mas tarde mis propias excepciones


#funcion usar habilidad

def usar_habilidad(jugador,villano,habilidad):
        
    habilidad_user = jugador.habilidades[habilidad]

    if habilidad_user.tipo == "normal":
    

        base_ataque = random.randrange(habilidad_user.potencia[0],habilidad_user.potencia[1])

        ataque = base_ataque+(base_ataque*(jugador.ataque/100))-(base_ataque*villano.defensa/100)

        villano.vida -= ataque

        return ataque
    
    if habilidad_user.tipo == "veneno":

        base_ataque = random.randrange(habilidad_user.potencia[0],habilidad_user.potencia[1])

        ataque = base_ataque+(base_ataque*(jugador.ataque/100))-(base_ataque*villano.defensa/100)

        villano.vida -= ataque

        #mecanicas de envenenamiento
        villano.envenenado[0]=True
        villano.envenenado.append([habilidad_user.potencia[0],habilidad_user.potencia[1],random.randrange(2,5)])
        print("\n\nHas envenenado al villano",villano.nombre,"por",villano.envenenado[1][2],"turnos...\n")
        time.sleep(2)

        return ataque

#funcion chequear duracion items (tipo veneno)

def check_duration_poison(villano):

    if villano.envenenado[0]:

        if villano.envenenado[1][2] >0:

            villano.envenenado[1][2] -=1

            total_damage = random.randrange(villano.envenenado[1][0],villano.envenenado[1][1])

            villano.vida -= total_damage

            print("El veneno afecta a",villano.nombre,"quitandole",total_damage,"puntos de vida")

        else:
            villano.envenenado[0] = False
            del villano.envenenado[1]
            print("El villano",villano.nombre,"se ha curado del veneno !")

#funcion de duracion items

def check_duration_items(jugador):
    
    items_acabados = []

    #a los items que esten activos se les restan turnos y se comprueba si ya no quedan
    for value in jugador.items.values():
        if value.activo[0] == True:
            value.turnos -=1
        if value.turnos == 0:
            items_acabados.append(value.nombre)
            print("\n\n---------------------------------------------\nWARNING ! se te ha acabado el item :",value.nombre,"\n---------------------------------------------")

            #segun el tipo de item que sea,volvemos a la normalidad de la stat del jugador que se habia modificado
            if value.tipo == "a":
                jugador.ataque = value.activo[1]

            if value.tipo == "p":
                jugador.precision = value.activo[1]                

    #si hay uno o mas items acabados se eliminan del inventario del jugador
    if len(items_acabados)>0:

        for item_acabado in items_acabados:
            del jugador.items[item_acabado]

#funcion de utilizacion de items

def usar_item(jugador):

    okay = False

    ut.limpiar_pantalla()

    lista_items =[]

    for item in jugador.items.values():
        if item.activo[0] == False:
            lista_items.append(item)

    if len(lista_items)>0:

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

            
        if item_seleccionado.tipo == "s":

            jugador.vida += item_seleccionado.potencia
            okay = True
            del jugador.items[item_seleccionado.nombre]

        if item_seleccionado.tipo == "p":
            
            jugador.items[item_seleccionado.nombre].activo.append(jugador.precision)

            jugador.precision +=item_seleccionado.potencia

            jugador.items[item_seleccionado.nombre].activo[0] = True

            okay = True

        if item_seleccionado.tipo == "sk":

            print("Vas a volver a golpear gracias a",item_seleccionado.nombre)

        # print(list(jugador.items.values())[0].nombre)
    else:
        print("no tenes items forro pelotudo !")

    if okay:

        print("\nHas equipado el item",item_seleccionado.nombre)
        return item_seleccionado.nombre


#funcion real de pelea
def luchar(jugador,villano):

    if random.random() < max((jugador.precision-villano.velocidad)/100,0.3): 

        print("\n"+jugador.nombre,"es mas veloz que",villano.nombre,"y le va a golpear primero\n")
        time.sleep(1.5)

        habilidad_user = elegir_habilidad(jugador)
        
        print("\nhas elegido la habilidad :",jugador.habilidades[habilidad_user].nombre)
        time.sleep(1)

        damage_user = usar_habilidad(jugador,villano,habilidad_user)

        print("\nwoww ! ese golpe le ha quitado a",villano.nombre,damage_user,"puntos de vida")

        if villano.vida >0:
            damage_villano = villano.atacar(jugador)
            print("\nEl pestilente villano,",villano.nombre,"te ha quitado",damage_villano,"puntos de vida")

    else:

        #villano ataca primero
        print("\n"+villano.nombre,"es mas veloz que",jugador.nombre,"y le va a golpear primero\n")
        time.sleep(.5)

        damage_villano = villano.atacar(jugador)

        print("\nEl pestilente villano,",villano.nombre,"te ha quitado",damage_villano,"puntos de vida")
        time.sleep(1.5)

        print("Ahora te toca a ti zurrarle...")
        time.sleep(1.5)

        habilidad_user = elegir_habilidad(jugador)
        
        print("\nhas elegido la habilidad :",jugador.habilidades[habilidad_user].nombre)
        time.sleep(1)

        damage_user = usar_habilidad(jugador,villano,habilidad_user)

        print("\nwoww ! ese golpe le ha quitado a",villano.nombre,damage_user,"puntos de vida")


#funcion de batalla
def fight(jugador,villano):

    sp.mihilo_fight_theme = sp.Songhilo()
    sp.mihilo_fight_theme.set_song("./recursos/lucha.mp3")
    sp.mihilo_fight_theme.start()

    while jugador.vida >0 and villano.vida >0:

        action = int(input("\n\n1--Ver stats villano\n\n2--Ver stats jugador\n\n3--Atacar villano\n\n4--Usar item\n\n5--huir\n\n- - - > "))

        if action == 1:

            ut.limpiar_pantalla()

            print(villano)

        if action == 2:

            ut.limpiar_pantalla()

            print(jugador)

        if action ==3:

            luchar(jugador,villano)

            #chequeamos que los items sigan activos
            check_duration_items(jugador)

            #chequeamos que el villano siga envenenado o no
            check_duration_poison(villano)

        if action == 4:
            
            usar_item(jugador)

        if action == 5:
            break
    
    del sp.mihilo_fight_theme

    if villano.vida>0:
        return 0
    else:
        return 1
    