import random
class Map:
    def __init__(self):
        self.ChunksX = 8  # 64
        self.ChunksY = 8  # 64

        self.ChunkMap = [[[0, 0, 0] for x in range(self.ChunksX)] for y in range(self.ChunksY)]
        self.mapPrinter()

    def mapPrinter(self):

        mazeStart_X = random.randint(1, self.ChunksX - 2)
        mazeStart_Y = random.randint(1, self.ChunksY - 2)
        wall_types = ['w', 'n', 's', 'e']
        walls = []

        for enumx, x in enumerate(self.ChunkMap):
            for enumy, y in enumerate(x):
                self.ChunkMap[enumx][enumy] = [enumx, enumy, 0]
        self.ChunkMap[mazeStart_X][mazeStart_Y] = [mazeStart_X, mazeStart_Y, 'wnse']
        walls.append([mazeStart_X - 1, mazeStart_Y])    # wall west
        walls.append([mazeStart_X, mazeStart_Y - 1])    # wall north
        walls.append([mazeStart_X, mazeStart_Y + 1])    # wall south
        walls.append([mazeStart_X + 1, mazeStart_Y])    # wall east

        # current_cell = self.ChunkMap[mazeStart_X][mazeStart_Y]
        # x = random.randint(0, 3)
        # print(has_walls(current_cell))
        # # if x == 0:
        # #     wall_types[0]
        # #     if current_cell[2].:
        #
        # print(mazeStart_X, mazeStart_Y)
        # for x in self.ChunkMap:
        #     print(x)
        # self.ChunkMap[1][1] = [1, 1, 1]

def has_walls(cell, wall):
    str_wall = ""
    for char in cell:
        if char == 'w':
            str_wall += 'w'
        if char == 'n':
            str_wall += 'n'
        if char == 's':
            str_wall += 's'
        if char == 'e':
            str_wall += 'e'
    return str_wall

# ChunkSize = {'x': 8, 'y': 8}
