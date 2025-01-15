import numpy as np

input = open("input.txt", 'r')
lines = input.read().splitlines()
input.close()

def convert_to_2d(lines):
    rows = []
    for line in lines:
        rows.append([c for c in line])
    return np.array(rows)

grid = convert_to_2d(lines)
m, n = grid.shape
print(grid)

def is_valid(i, j, m, n):
    return  i >= 0 and j >= 0 and i < m and j < n


def search_from_pos(grid, r, c):
    m, n = grid.shape
    word = 'DIKU'
    
    if grid[r, c] != 'D':
        return 0
    
    dirX = [-1, 0, 1, 1, 1, 0, -1, -1] # U-L, U-U, U-R, etc.
    dirY = [1, 1, 1, 0, -1, -1, -1, 0]
    
    matches = 0
    
    for x, y in zip(dirX, dirY):
        next_pos = r + x, c + y
        
        k = 1
        while k < 4:
            if not is_valid(next_pos[0], next_pos[1], m, n) or grid[next_pos] != word[k]:
                break
            next_pos = next_pos[0] + x, next_pos[1] + y
            k += 1
        if k == 4:
            matches += 1
    return matches


def loop_through_grid(grid):
    m, n = grid.shape
    
    total = 0
    for i in range(m):
        for j in range(n):
            total += search_from_pos(grid, i, j)
    return total

total = loop_through_grid(grid)
print(total)            