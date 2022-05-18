import audioplayer,threading as th


#clase encargada de llevar la ejecucion de la musica principal en un hilo independiente a la linea principal del programa
class Songhilo(th.Thread):

    #con este constructor inicializamos todo lo q necesitamos ademas de el hilo en si
    def __int__(self):

        super().__init__(self)

    def set_song(self,ruta):

        self.song = audioplayer.AudioPlayer(ruta)
        self.stoprequest = th.Event()

    def run(self):

        self.song.volume = 100
        self.song.play(loop=True,block=False)

class Songhilo_jugadores(Songhilo):

    def run(self):

        self.song.volume = 100
        self.song.play(loop=False,block=True)


mihilo_main_theme = Songhilo()
mihilo_main_theme.set_song("./recursos/monkey.mp3")
# mihilo_main_theme.set_song("/Users/zaslake/Desktop/2/programacion/python/abril2022/periko/recursos/monkey.mp3")

mihilo_fight_theme = Songhilo()
mihilo_fight_theme.set_song("./recursos/lucha.mp3")
# mihilo_fight_theme.set_song("/Users/zaslake/Desktop/2/programacion/python/abril2022/periko/recursos/lucha.mp3")


# import time
# mihilo_fight_theme.start()
# time.sleep(3)
# print(mihilo_fight_theme.acabar_hilo())

# time.sleep(2)
# print(1)
# mihilo_fight_theme.song.play(loop=True,block=False)

# time.sleep(3)
# print(2)
# mihilo_fight_theme.song.close()

# time.sleep(2)
# print(3)
# del mihilo_fight_theme
# time.sleep(3)

# mihilo_fight_theme = Songhilo()
# mihilo_fight_theme.set_song("/Users/zaslake/Desktop/2/programacion/python/abril2022/periko/recursos/lucha.mp3")
# print(mihilo_fight_theme)



