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