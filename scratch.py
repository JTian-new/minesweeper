width = 4
height = 4

cell = (1,2)
mines = set((1,3),(2,2))
safes = set((0,2))

board = [
    [(0,0),(0,1),(0,2),(0,3)],
    [(1,0),(1,1),(1,2),(1,3)],
    [(2,0),(2,1),(2,2),(2,3)],
    [(3,0),(3,1),(3,2),(3,3)],
]

neighbors = set()
for i in range(cell[0] - 1, cell[0] + 2):
    for j in range(cell[1] - 1, cell[1] + 2):
        
        # Ignore the cell itself
        if (i, j) == cell:
            continue

        # Update count if cell in bounds and is mine
        if 0 <= i < height and 0 <= j < width and (i,j) not in mines and (i,j) not in safes:
            neighbors.add((i,j))  

print(set(neighbors))

