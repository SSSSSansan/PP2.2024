import pygame
import os
 
pygame.mixer.init()
pygame.init()
screen = pygame.display.set_mode((1280, 600))
pygame.display.set_caption("Музыкальный проигрыватель")
clock = pygame.time.Clock()
done = False
songs = []
 
folder_path = 'musics'
files_list = os.listdir(folder_path)
 
for file_name in files_list:
    file_path = os.path.join(folder_path, file_name)
    if os.path.isfile(file_path):
        songs.append(file_path)
 
pygame.mixer.music.load(songs[0])
pygame.mixer.music.play()
current_song_index = 0
paused = False
 
font = pygame.font.Font( None, 36)
 
 
instruction_text = [
    "Используйте стрелки '<' и '>' для переключения между песнями.",
    "Нажмите пробел для паузы/продолжения проигрывания.",
    "Программа автоматически переключает на следующую песню после окончания текущей."
]
 
while not done:
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(50, 50, 400, 50))  
 
    current_song_text = font.render("Текущая песня: " + songs[current_song_index], True, (0, 0, 0))
    screen.blit(current_song_text, (60, 60))
 
    for idx, line in enumerate(instruction_text):
        instruction = font.render(line, True, (128, 5, 5))
        screen.blit(instruction, (60, 150 + idx * 40))
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                current_song_index = (current_song_index + 1)
                pygame.mixer.music.load(songs[current_song_index])
                pygame.mixer.music.play()
                paused = False
            elif event.key == pygame.K_LEFT:
                current_song_index = (current_song_index - 1)
                pygame.mixer.music.load(songs[current_song_index])
                pygame.mixer.music.play()
                paused = False
            elif event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True
 
    if not pygame.mixer.music.get_busy() and not paused:
        current_song_index = (current_song_index + 1) % len(songs)
        pygame.mixer.music.load(songs[current_song_index] )
        pygame.mixer.music.play()
 
    pygame.display.flip()
    clock.tick(60)
 
pygame.quit()