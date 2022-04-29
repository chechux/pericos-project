import clases as cl
import random

#Dimension C-137 

    #items

#los items de tipo sk sirven para tener 2 turnos seguidos,es decir,que el rival se pierda su tuno por alguna rzon
pistola_portales = cl.Items("pistola de portales","sk",0,"con la pistola de portales de rick te vas a la dimension 35 en tal de esquivar el golpe y vuelve a ser tu turno !",1)
#los items de tipo ataque incrementan la fuerza
espada_bacon = cl.Items("espada bacon","a",random.randrange(10,25),"con esta ridicula y sabrosa espada aumenta tu fuerza !",1)
#los items de tipo sanacion incrementan la vida
cuencas_de_ojos = cl.Items("cuencas de ojos","s",random.randrange(10,25),"con estos deliciosas y asquerosas cuencas de ojos aumenta tu salud !",1)
#los items de tipo precicison incrementan la precision,obviamente
parche_de_morty = cl.Items("parche de morty","p",30,"con este parche de morty te vuelves mas audaz y tu precision aumenta",1)
#los items

    #villanos

abradolf_lincler = cl.Mob("abradolf lincler",100,5,5,50,100)
asustadizo_terry = cl.Mob("asustadizo terry",100,5,5,50,10)
bola_de_nieve = cl.Mob("bola de nieve",100,5,5,50,10)

    #dimension

dimension_c137 = cl.Dimension("C-137",[pistola_portales,espada_bacon,cuencas_de_ojos,parche_de_morty],[abradolf_lincler,asustadizo_terry,bola_de_nieve])




dimensiones = [dimension_c137] 
        
               

homero = cl.Jugador("homero",100,40,50,50,20) 