import pygame as pg

pg.init()
screen = pg.display.set_mode((1000, 800))
screen.fill((255, 255, 255))

class Button(pg.sprite.Sprite):
    def __init__(self, x, y, text, font_size):
        super().__init__()
        self.font = pg.font.Font(None, font_size)
        self.text = text
        self.image = self.font.render(self.text, True, (0, 0, 0))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.is_selected = False

    def make_selected(self, group):
        if not self.is_selected:
            self.prev_image = self.image.copy()
            self.image = self.font.render(self.text, True, (255, 0, 0))
            self.is_selected = True
        else:
            self.image = self.prev_image
            self.is_selected = False
        for i in group.sprites():
            if i == self:
                continue
            i.make_default(group)
            
    def make_default(self, group):
        try: 
            self.image = self.prev_image
            self.is_selected = False
        except:
            pass

def draw_line(screen, start, end, width, color):
    pg.draw.line(screen, color, start, end, width)

def draw_rectangle(screen, color, rect, size):
    pg.draw.rect(screen, color, rect, size)

def draw_ellipse(screen, color, rect, size):
    pg.draw.ellipse(screen, color, rect, size)

def draw_right_triangle(screen, color, pos, size):
    pg.draw.polygon(screen, color, [(pos[0], pos[1]), (pos[0] + size, pos[1]), (pos[0], pos[1] + size)])

def draw_equilateral_triangle(screen, color, pos, size):
    height = size * (3 ** 0.5) / 2
    pg.draw.polygon(screen, color, [(pos[0], pos[1] + size), (pos[0] + size / 2, pos[1] - height), (pos[0] + size, pos[1] + size)])

def draw_rhombus(screen, color, pos, size):
    pg.draw.polygon(screen, color, [(pos[0], pos[1] + size // 2), 
                                    (pos[0] + size // 2, pos[1]), 
                                    (pos[0] + size, pos[1] + size // 2), 
                                    (pos[0] + size // 2, pos[1] + size)])


brush = Button(5, 5, 'Brush (B)', 24)
draw_rect = Button(5, 40, 'Rectangle (R)', 24)
draw_circle = Button(5, 75, 'Circle (C)', 24)
eraser = Button(5, 110, 'Eraser (E)', 24)

draw_square = Button(5, 145, 'Square (S)', 24)
draw_right_triangle_btn = Button(5, 180, 'Right Triangle (T)', 24)
draw_equilateral_triangle_btn = Button(5, 215, 'Equilateral Triangle (U)', 24)
draw_rhombus_btn = Button(5, 250, 'Rhombus (V)', 24)

red_color = Button(5, 300, 'Red (1)', 24)
black_color = Button(5, 335, 'Black (2)', 24)
blue_color = Button(5, 370, 'Blue (3)', 24)
green_color = Button(5, 405, 'Green (4)', 24)

all_buttons = pg.sprite.Group(brush, draw_rect, draw_circle, eraser, draw_square, draw_right_triangle_btn, draw_equilateral_triangle_btn, draw_rhombus_btn)
colors = pg.sprite.Group(red_color, black_color, blue_color, green_color)

selected_color = (0, 0, 0)

start_pos = (0, 0)
end_pos = (0, 0)
drawing = False

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if brush.rect.collidepoint(event.pos):
                brush.make_selected(all_buttons)
            elif draw_rect.rect.collidepoint(event.pos):
                draw_rect.make_selected(all_buttons)
            elif draw_circle.rect.collidepoint(event.pos):
                draw_circle.make_selected(all_buttons)
            elif eraser.rect.collidepoint(event.pos):
                eraser.make_selected(all_buttons)
            elif draw_square.rect.collidepoint(event.pos):
                draw_square.make_selected(all_buttons)
            elif draw_right_triangle_btn.rect.collidepoint(event.pos):
                draw_right_triangle_btn.make_selected(all_buttons)
            elif draw_equilateral_triangle_btn.rect.collidepoint(event.pos):
                draw_equilateral_triangle_btn.make_selected(all_buttons)
            elif draw_rhombus_btn.rect.collidepoint(event.pos):
                draw_rhombus_btn.make_selected(all_buttons)
            elif event.button == 1:  # Left mouse button pressed
                start_pos = event.pos
                drawing = True
        elif event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button released
                drawing = False
                end_pos = event.pos
                if draw_rect.is_selected:
                    draw_rectangle(screen, selected_color, (start_pos[0], start_pos[1], end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]), 5)
                elif draw_circle.is_selected:
                    draw_ellipse(screen, selected_color, (start_pos[0], start_pos[1], end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]), 5)
                elif draw_square.is_selected:
                    draw_rectangle(screen, selected_color, (start_pos[0], start_pos[1], end_pos[0] - start_pos[0], end_pos[0] - start_pos[0]), 5)
                elif draw_right_triangle_btn.is_selected:
                    draw_right_triangle(screen, selected_color, start_pos, end_pos[0] - start_pos[0])
                elif draw_equilateral_triangle_btn.is_selected:
                    draw_equilateral_triangle(screen, selected_color, start_pos, end_pos[0] - start_pos[0])
                elif draw_rhombus_btn.is_selected:
                    draw_rhombus(screen, selected_color, start_pos, end_pos[0] - start_pos[0])
        elif event.type == pg.MOUSEMOTION and drawing:
            if brush.is_selected:
                draw_line(screen, start_pos, event.pos, 5, selected_color)
            elif eraser.is_selected:
                draw_line(screen, start_pos, event.pos, 20, (255, 255, 255))
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_b:
                brush.make_selected(all_buttons)
            elif event.key == pg.K_r:
                draw_rect.make_selected(all_buttons)
            elif event.key == pg.K_c:
                draw_circle.make_selected(all_buttons)
            elif event.key == pg.K_e:
                eraser.make_selected(all_buttons)
            elif event.key == pg.K_s:
                draw_square.make_selected(all_buttons)
            elif event.key == pg.K_t:
                draw_right_triangle_btn.make_selected(all_buttons)
            elif event.key == pg.K_u:
                draw_equilateral_triangle_btn.make_selected(all_buttons)
            elif event.key == pg.K_v:
                draw_rhombus_btn.make_selected(all_buttons)
            elif event.key == pg.K_1:
                selected_color = (255, 0, 0)  # Red
            elif event.key == pg.K_2:
                selected_color = (0, 0, 0)    # Black
            elif event.key == pg.K_3:
                selected_color = (0, 0, 255)  # Blue
            elif event.key == pg.K_4:
                selected_color = (0, 255, 0)  # Green

    all_buttons.draw(screen)
    colors.draw(screen)
    pg.display.flip()

pg.quit()
