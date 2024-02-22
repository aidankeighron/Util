import pygame as pg
import sys
import numpy as np

def new_generation(cells: list) -> list:
    next_generation = []
    for i in range(len(cells)):
        next_generation_row = []
        for j in range(len(cells[i])):
            neighbor_count = 0
            for n in [-1, 0, 1]:
                for m in [-1, 0, 1]:
                    if (not ((len(cells[i])-1)>=j+m>=0<=i+n<=(len(cells)-1)) or 
                        (n==0 and m==0)):
                        continue
                    neighbor_count += cells[i+n][j+m]

            next_generation_row.append(
                int((cells[i][j] and 2 <= neighbor_count <= 3) or 
                    (not cells[i][j] and neighbor_count == 3)))
        next_generation.append(next_generation_row)
    return next_generation

def write_text(string, x, y, font_size, screen):
    text = pg.font.Font('freesansbold.ttf', font_size).render(string, True, (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text, text_rect)

pg.init()

screen_size = (800, 800)
simulation_size = (100, 100)
simulation_frame_rate = 30
paused_frame_rate = 120
frame_cap = 100
screen = pg.display.set_mode(screen_size)

clock = pg.time.Clock()

WHITE = [255, 255, 255]
BLACK = [0, 0, 0]

colors = np.array([WHITE, BLACK])
grid = np.zeros(shape=simulation_size, dtype=int)
paused = True
drag = False

while True:
    clock.tick(simulation_frame_rate if not paused else paused_frame_rate)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            keys = pg.key.get_pressed()
            if keys[pg.K_SPACE]:
                paused = not paused
            if keys[pg.K_w]:
                simulation_frame_rate += 5 if not keys[pg.K_LCTRL] else 1
                if simulation_frame_rate >= frame_cap:
                    simulation_frame_rate = frame_cap
            if keys[pg.K_s]:
                simulation_frame_rate -= 5 if not keys[pg.K_LCTRL] else 1
                if simulation_frame_rate <= 0:
                    simulation_frame_rate = 5 if not keys[pg.K_LCTRL] else 1
        if event.type == pg.MOUSEBUTTONDOWN:
            drag = True
        if event.type == pg.MOUSEBUTTONUP:
            drag = False
            
    screen.fill(WHITE)
    
    if drag:
        x,y = pg.mouse.get_pos()
        grid[x//8][y//8] = 1
    
    if not paused:
        grid = new_generation(grid)
        
    surface = pg.surfarray.make_surface(colors[grid])
    surface = pg.transform.scale(surface, (800, 800))  # Scaled a bit.
    screen.blit(surface, (0, 0))
    write_text("Press space to pause", 5, 5, 14, screen)
    write_text(f"Paused: {paused}", 5, 20, 14, screen)
    write_text("W - Speed up | S - Slow down | Hold ctrl for fine control", 5, 35, 14, screen)
    write_text(f"Frame rate: {simulation_frame_rate}", 5, 50, 14, screen)
    write_text(f"FPS: {round(clock.get_fps(), 2)}", 5, 65, 14, screen)
    pg.display.flip()
    

        
        
# BLINKER = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
# print(new_generation(BLINKER))