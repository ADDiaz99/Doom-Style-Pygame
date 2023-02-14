import pygame as pg


class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sound/'
        self.shotgun = pg.mixer.Sound(self.path + 'shotgun.wav')
        self.theme = pg.mixer.music.load(self.path + 'theme.mp3')
        #self.theme = pg.mixer.music.load(self.path + 'noche_de_senso.mp3')