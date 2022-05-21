import random, time


#Minijuego de Reflux

class Codigo():
    
    def __init__(self):

        self.codigo = self.generar_codigo()
        
        self.lista_mostrar = self.mostrar_codigo()
        
    def generar_codigo(self):
        dic = []
        x = random.choice( [ '1234', '1432', '3421', '4213' ] )
        y =  random.choice( [ '5678', '5876', '7865', '8657' ] )
        z =  random.choice( [ '9356', '7469', '5219', '3789' ] )

        dic = '-'.join([x,y,z])
        return dic
    
    def  mostrar_codigo(self):
        backup = ''
        backup = self.codigo
        
        backup = backup.replace('-',' ')
                
        for j in range(0,len(backup)):
            #print( backup[ j ], type( backup[ j ] ) )

            if backup[ j ] != ' ':
                if backup[ j ] in '123456789':
                    backup = backup.replace( str( backup[ j ] ), '-' )
               
        #print(backup)
        return backup

class Probando(Codigo):
    
    def __init__(self, n1,n2):

        super.__init__()
        
        self.numero = numero
        self.nums = [ ]


didujo_rayman= '''
        
'''

print('Reflux -> Preparate para tu perdición')
print()
print('Reflux -> Para vencerme tendrás que resolver un código o seras mi prisionero eterno')
print('\n\n**Modo de Juego:** -> Al acertar un numero puedes quitarle vida a Reflux con un Ataque Especial\n\n')
print('Como último recurso, puedes repetir un numero existente\n\n')

def  pide_nums ():
    ok = 0
    try:
        
        x1 = input('Dime un número del 1 -- 9 : ')
        x1 = int(x1)
        
        if x1 in range(1,10):
            ok += 1
            
        if ok == 1:
            return x1
        
        else:
            print('\n\nNumeros Invalidos ',x1,'\n\n')
            pide_nums()
        
    except Exception:
        d = '\n valor no  válido : '+' '+str(x1)+' '+'\n\n'
        print(d)
        pide_nums()
        

def  comprovar_vida(x):
    if x <= 0:
        return False
    
def coincidencia( num, ocul, cod, reflux):

    lista = list(ocul)
    
    for i in range(0,14):
        
        if( cod[i] != '-' and ocul[i] != ' '):  #Mientras el resultado del indice sea un caracter extraño
                                                                  # El código no se ejecuta
            if str(num) in cod:
                
                if cod[i] == str(num):
                    
                        lista[i] = str(num)
                        x = random.randrange(30,55)
                        print('\n\nGolpeas a Reflux con ',x,'de daño')
                        reflux -= x
        else:
            continue    # Pasa a la siguiente iteración
                        
    j = "".join(lista)

    return j, reflux
    
# ---------- START ---------------
reflux_vida = 300

intentos = 0

objeto = Codigo( )

##print(objeto.codigo,type(objeto.codigo))

oculto = objeto.lista_mostrar

while True:
    
    if comprovar_vida( reflux_vida ) == False: # Esta funcion evalua si reflux se ha quedado sin vida
        print('\n\n Reflux -> Me has derrotado ... ,  puedes marcharte')
        break
    else:
        print( '\n\nVida de Reflux : ', reflux_vida )
        
    print('\n\n')
    print('Intento : ',intentos,'    Código : ',oculto)

    n1 = pide_nums()
    
    oculto, reflux_vida = coincidencia( n1 , oculto, objeto.codigo,  reflux_vida)
##    coincidencia( n1 , oculto, objeto.codigo,  reflux_vida)
    



    

    
    



