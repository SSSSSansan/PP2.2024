import pygame as pg
import os

pg.init()

class Sound:
    def __init__(self, path_to_sound):
        self.sound = pg.mixer.Sound(os.path.join('lab7', 'music', path_to_sound))
        self.is_playing = True
    
path_to_sound = os.listdir(os.path.join('lab7', 'music'))
path_to_sound.sort()

sounds = []

for sound_file in path_to_sound:
    sound = Sound(sound_file)
    sounds.append(sound)

screen = pg.display.set_mode((490, 635))

sound_index = 0
sounds[0].sound.play()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                if sounds[sound_index].is_playing:
                    pg.mixer.pause()
                    sounds[sound_index].is_playing = False
                else:
                    pg.mixer.unpause()
                    sounds[sound_index].is_playing = True
            elif event.key == pg.K_RIGHT:
                pg.mixer.stop()
                sound_index += 1
                if sound_index == len(sounds):
                    sound_index = 0
                sounds[sound_index].sound.play()
            elif event.key == pg.K_LEFT:
                pg.mixer.stop()
                sound_index -= 1
                if sound_index == -1:
                    sound_index = len(sounds) - 1
                sounds[sound_index].sound.play()

    pg.display.flip()

pg.quit()
