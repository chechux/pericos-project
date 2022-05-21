
import mysql.connector as msq

def concetar(user,passworduser,base):
    try:
        miconexion = msq.connect(
            host= 'localhost',
            user=user,
            password=passworduser,
            database=base
        )

        if miconexion.is_connected():
            print("conexion establecida")
            return miconexion

    except Exception as fail:
        print("error al conectar con la base de datos")
        print(fail)

miconex = concetar("root","1234","multiverso")



def subir_datos_partida(jugadorr,pts,enemigos,bosses):

    micursor = miconex.cursor()
    micursor.execute("insert into jugador (nombre,puntos,enemigos,bosses) values({},{},{},{})".format(jugadorr,pts,str(enemigos),str(bosses)))
    # micursor.execute("select * from jugador;")
    # micursor.execute("insert into jugador (nombre,puntos,enemigos,bosses) values('jose',5,5,5)")
    # for x in micursor:
    #     print(x)
    miconex.commit()
    micursor.close()
    print("todo bien")

# subir_datos_partida()

# for bd in micursor:
#     print(bd)

# subir_datos_partida("jose",999,1,2)
# subir_datos_partida("ppp",200,2,1)

