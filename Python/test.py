import pygame as pg
import sys
import numpy as np

def new_generation(board: list, ant_position: list, direction: int) -> tuple:
    directions = [(-1, 0), (0, 1), (1,0), (0,-1)]

    x, y = ant_position

    direction = (direction + (1 if board[x][y] else -1)) % 4

    move_x, move_y = directions[direction]
    ant_position[0] += move_x
    ant_position[1] += move_y

    board[x][y] = 0 if board[x][y] else 1

    return board, ant_position, direction

def write_text(string, x, y, font_size, screen):
    text = pg.font.Font('freesansbold.ttf', font_size).render(string, True, (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text, text_rect)

pg.init()

screen_size = (800, 800)
simulation_size = (100, 100)
simulation_frame_rate = 30
frame_cap = 100
iteration = 0
screen = pg.display.set_mode(screen_size)

clock = pg.time.Clock()

WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
RED = [255, 0, 0]

colors = np.array([WHITE, BLACK, RED])
grid = np.zeros(shape=simulation_size, dtype=int)
ant_position = [simulation_size[0]//2, simulation_size[1]//2]
direction = 3
paused = True

while True:
    clock.tick(simulation_frame_rate)

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
            
    screen.fill(WHITE)
    
    
    if not paused:
        grid, ant_position, direction = new_generation(grid, ant_position, direction)
        iteration += 1

    
    temp = grid[ant_position[0], ant_position[1]]
    grid[ant_position[0], ant_position[1]] = 2
    surface = pg.surfarray.make_surface(colors[grid])
    grid[ant_position[0], ant_position[1]] = temp
    surface = pg.transform.scale(surface, (800, 800))  # Scaled a bit.
    screen.blit(surface, (0, 0))
    write_text("Press space to pause", 5, 5, 14, screen)
    write_text(f"Paused: {paused}", 5, 20, 14, screen)
    write_text("W - Speed up | S - Slow down | Hold ctrl for fine control", 5, 35, 14, screen)
    write_text(f"Frame rate: {simulation_frame_rate}", 5, 50, 14, screen)
    write_text(f"FPS: {round(clock.get_fps(), 2)}", 5, 65, 14, screen)
    write_text(f"Iteration: {iteration}", 5, 80, 14, screen)
    pg.display.flip()
    

        
        
# BLINKER = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
# print(new_generation(BLINKER))