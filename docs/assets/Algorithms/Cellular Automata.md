---
layout: script
language: Algorithms
---

# Conway's Game Of Life

Implementation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) in python.

```python
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
```

Creating a UI with Pygame:

```python
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
```

# Langtons Ant

Implementation of [Langtons Ant](https://en.wikipedia.org/wiki/Langton%27s_ant) in python.

```python
def new_generation(board: list, ant_position: list, direction: int) -> tuple:
    directions = [(-1, 0), (0, 1), (1,0), (0,-1)]

    x, y = ant_position

    direction = (direction + (1 if board[x][y] else -1)) % 4

    move_x, move_y = directions[direction]
    ant_position[0] += move_x
    ant_position[1] += move_y

    board[x][y] = 0 if board[x][y] else 1

    return board, ant_position, direction
```

Creating a UI with pygame.

```python
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
```

# Wa Tor

Battle between sharks and fish.

```python
import random
def fish_movement(i, j, grid, new_grid, colors):
    options = [[1,0],[0,1],[-1,0],[0,-1]]
    spaces = []
    for x, y in options:
        try:
            if grid[i+x][j+y][0] == 0 and new_grid[i+x][j+y][0] == 0:
                spaces.append([x,y])
        except IndexError:
            ... # Out of bounds
    if spaces:
        space = random.choice(spaces)
        if grid[i][j][1]-1 <= 0:
            new_grid[i+space[0]][j+space[1]] = [1, 5]
            colors[i+space[0]][j+space[1]] = 1
            new_grid[i][j] = [1, 5]
            colors[i][j] = 1
        else:
            new_grid[i+space[0]][j+space[1]] = [1, grid[i][j][1]-1]
            colors[i+space[0]][j+space[1]] = 1
    else:
        new_grid[i][j] = [1, grid[i][j][1]-1]
        colors[i][j] = 1
        
def shark_movement(i, j, grid, new_grid, colors):
        if grid[i][j][2] == 0:
            # Shark dies
            return
        options = [[1,0],[0,1],[-1,0],[0,-1]]
        spaces = []
        alt_spaces = []
        fish = False
        for x, y in options:
            try:
                if grid[i+x][j+y][0] == 1 and new_grid[i+x][j+y][0] == 1:
                    spaces.append([x,y])
                    fish = True
            except IndexError:
                ... # Out of bounds
            try:
                if grid[i+x][j+y][0] == 0 and new_grid[i+x][j+y][0] == 0:
                    alt_spaces.append([x,y])
            except IndexError:
                ... # Out of bounds
        if not spaces:
            spaces = alt_spaces
        if spaces:
            space = random.choice(spaces)
            if fish:
                grid[i][j][2] += 5
            if grid[i][j][1]-1 <= 0:
                new_grid[i+space[0]][j+space[1]] = [2, 20, grid[i][j][2]-1]
                colors[i+space[0]][j+space[1]] = 2
                new_grid[i][j] = [2, 20, 15]
                colors[i][j] = 2
            else:
                new_grid[i+space[0]][j+space[1]] = [2, grid[i][j][1]-1, grid[i][j][2]-1]
                colors[i+space[0]][j+space[1]] = 2
        else:
            new_grid[i][j] = [2, grid[i][j][1]-1, grid[i][j][2]-1]
            colors[i][j] = 2
        
def new_generation(grid: list) -> tuple:
    new_grid = [[[0] for _ in range(len(grid))] for _ in range(len(grid[0]))]
    colors = [[0 for _ in range(len(grid))] for _ in range(len(grid[0]))]
    # for i, line in enumerate(grid):
        # for j, index in enumerate(line):
    coords = [(x,y) for x in range(len(grid)) for y in range(len(grid[0]))]
    random.shuffle(coords)
    for i, j in coords:
        # Nothing
        if grid[i][j][0] == 0:
            continue
        # Fish
        if grid[i][j][0] == 1:
            fish_movement(i, j, grid, new_grid, colors)
        # Shark
        if grid[i][j][0] == 2:
            shark_movement(i, j, grid, new_grid, colors)
```

Creating a UI with pygame.

```python
import pygame as pg
import sys
import numpy as np
import random

def fish_movement(i, j, grid, new_grid, colors):
    options = [[1,0],[0,1],[-1,0],[0,-1]]
    spaces = []
    for x, y in options:
        try:
            if grid[i+x][j+y][0] == 0 and new_grid[i+x][j+y][0] == 0:
                spaces.append([x,y])
        except IndexError:
            ... # Out of bounds
    if spaces:
        space = random.choice(spaces)
        if grid[i][j][1]-1 <= 0:
            new_grid[i+space[0]][j+space[1]] = [1, 5]
            colors[i+space[0]][j+space[1]] = 1
            new_grid[i][j] = [1, 5]
            colors[i][j] = 1
        else:
            new_grid[i+space[0]][j+space[1]] = [1, grid[i][j][1]-1]
            colors[i+space[0]][j+space[1]] = 1
    else:
        new_grid[i][j] = [1, grid[i][j][1]-1]
        colors[i][j] = 1
        
def shark_movement(i, j, grid, new_grid, colors):
        if grid[i][j][2] == 0:
            # Shark dies
            return
        options = [[1,0],[0,1],[-1,0],[0,-1]]
        spaces = []
        alt_spaces = []
        fish = False
        for x, y in options:
            try:
                if grid[i+x][j+y][0] == 1 and new_grid[i+x][j+y][0] == 1:
                    spaces.append([x,y])
                    fish = True
            except IndexError:
                ... # Out of bounds
            try:
                if grid[i+x][j+y][0] == 0 and new_grid[i+x][j+y][0] == 0:
                    alt_spaces.append([x,y])
            except IndexError:
                ... # Out of bounds
        if not spaces:
            spaces = alt_spaces
        if spaces:
            space = random.choice(spaces)
            if fish:
                grid[i][j][2] += 5
            if grid[i][j][1]-1 <= 0:
                new_grid[i+space[0]][j+space[1]] = [2, 20, grid[i][j][2]-1]
                colors[i+space[0]][j+space[1]] = 2
                new_grid[i][j] = [2, 20, 15]
                colors[i][j] = 2
            else:
                new_grid[i+space[0]][j+space[1]] = [2, grid[i][j][1]-1, grid[i][j][2]-1]
                colors[i+space[0]][j+space[1]] = 2
        else:
            new_grid[i][j] = [2, grid[i][j][1]-1, grid[i][j][2]-1]
            colors[i][j] = 2
        
def new_generation(grid: list) -> tuple:
    new_grid = [[[0] for _ in range(len(grid))] for _ in range(len(grid[0]))]
    colors = [[0 for _ in range(len(grid))] for _ in range(len(grid[0]))]
    # for i, line in enumerate(grid):
        # for j, index in enumerate(line):
    coords = [(x,y) for x in range(len(grid)) for y in range(len(grid[0]))]
    random.shuffle(coords)
    for i, j in coords:
        # Nothing
        if grid[i][j][0] == 0:
            continue
        # Fish
        if grid[i][j][0] == 1:
            fish_movement(i, j, grid, new_grid, colors)
        # Shark
        if grid[i][j][0] == 2:
            shark_movement(i, j, grid, new_grid, colors)

    return new_grid, colors

def write_text(string, x, y, font_size, screen):
    text = pg.font.Font('freesansbold.ttf', font_size).render(string, True, (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text, text_rect)

pg.init()

screen_size = (800, 800)
simulation_size = (100, 100)
simulation_frame_rate = 5
frame_cap = 30
iteration = 0
screen = pg.display.set_mode(screen_size)

clock = pg.time.Clock()

WHITE = [255, 255, 255]
RED = [200, 50, 50]
GREEN = [50, 200, 50]

colors = np.array([WHITE, GREEN, RED])
# grid = np.zeros(shape=simulation_size, dtype=int)
animal_options = [[0], [1,5], [2,20,15]]
# print(np.random.choice([0,1,2], 1,  p=[0.8, 0.2, 0]))
grid = [[animal_options[np.random.choice([0,1,2], 1,  p=[0.6, 0.3, 0.1])[0]] for _ in range(simulation_size[0])] for _ in range(simulation_size[1])]
color = [[grid[i][j][0] for i in range(simulation_size[0])] for j in range(simulation_size[1])]
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
        grid, color = new_generation(grid)
        iteration += 1

    surface = pg.surfarray.make_surface(colors[color])
    surface = pg.transform.scale(surface, (800, 800))  # Scaled a bit.
    screen.blit(surface, (0, 0))
    write_text("Press space to pause", 5, 5, 14, screen)
    write_text(f"Paused: {paused}", 5, 20, 14, screen)
    write_text("W - Speed up | S - Slow down | Hold ctrl for fine control", 5, 35, 14, screen)
    write_text(f"Frame rate: {simulation_frame_rate}", 5, 50, 14, screen)
    write_text(f"FPS: {round(clock.get_fps(), 2)}", 5, 65, 14, screen)
    write_text(f"Iteration: {iteration}", 5, 80, 14, screen)
    pg.display.flip()
```