from email.mime import audio
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
        self.song.play(loop=True)

    def pause_song(self):

        self.song.pause()

mihilo_main_theme = Songhilo()

mihilo_fight_theme = Songhilo()



