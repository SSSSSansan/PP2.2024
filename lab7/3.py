import pygame
pygame.init()

win = pygame.display.set_mode((550, 550))
  
width = 50
height = 50
x = 200
y = 200
vel = 20
  

run = True
while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
          x -= vel
    if keys[pygame.K_RIGHT] and x < 500-width:
        x += vel
    if keys[pygame.K_UP] and y > 0:  
        y -= vel
    if keys[pygame.K_DOWN] and y < 500-height:
        y += vel
          
    win.fill((255, 255, 255))
      
    pygame.draw.circle(win, (255, 0, 0), (x, y), 25)
      
    pygame.display.flip() 
  
pygame.quit()