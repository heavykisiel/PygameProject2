import random


class Map:
    def __init__(self):
        self.ChunksX = 4  # 64
        self.ChunksY = 4  # 64
        self.ChunkMap = [[[0, 0, 0] for _ in range(self.ChunksX)] for _ in range(self.ChunksY)]
        self.maze_start_x = random.randint(1, self.ChunksX - 2)
        self.maze_start_y = random.randint(1, self.ChunksY - 2)
        self.last_visited = None
        self.isMap_invalid = True
        self.MapGen()

    def MapGen(self):
        i = 0
        while self.isMap_invalid:
            i += 1
            self.mapPrinter()
        print(f"map generation with doors on {i} attempt")
        for x in self.ChunkMap:
            print(x)
        print("end")

    def mapPrinter(self):
        # render map coords
        for enumx, x in enumerate(self.ChunkMap):
            for enumy, y in enumerate(x):
                self.ChunkMap[enumx][enumy] = [enumx, enumy, 'wnse', 0, ""]
        # random spawn
        # [0] maze_start_x = random.randint(1, self.ChunksX - 2)
        # [1]maze_start_y = random.randint(1, self.ChunksY - 2)
        # [2] walls
        # [3] visited
        # [4] room Function
        visited = list()
        backtracked_rooms = list()
        visited.append([self.maze_start_x, self.maze_start_y])
        self.ChunkMap[self.maze_start_x][self.maze_start_y] = [self.maze_start_x, self.maze_start_y, 'wnse', 1, ""]
        backtrack_count = 0

        while self.ChunksX * self.ChunksY > len(visited) + backtrack_count:
            # neighbours / breaking wall options
            stri = ""
            x_pos, y_pos = visited[len(visited) - 1]
            if x_pos > 0 and self.ChunkMap[x_pos - 1][y_pos][3] == 0:
                stri += 'n'
            if y_pos > 0 and self.ChunkMap[x_pos][y_pos - 1][3] == 0:
                stri += 'w'
            if x_pos < self.ChunksX - 1 and self.ChunkMap[x_pos + 1][y_pos][3] == 0:
                stri += 's'
            if y_pos < self.ChunksY - 1 and self.ChunkMap[x_pos][y_pos + 1][3] == 0:
                stri += 'e'
            if stri != "":
                random_wall = random.choice(stri)
                if random_wall.__contains__('n'):
                    self.setRoomValue(x_pos, y_pos, 'n', 1)  # delete north wall
                    self.setRoomValue(x_pos - 1, y_pos, 's', 1)  # delete south wall next room
                    visited.append([x_pos - 1, y_pos])
                if random_wall.__contains__('w'):
                    self.setRoomValue(x_pos, y_pos, 'w', 1)  # delete west wall
                    self.setRoomValue(x_pos, y_pos - 1, 'e', 1)  # delete east wall next room
                    visited.append([x_pos, y_pos - 1])
                if random_wall.__contains__('s'):
                    self.setRoomValue(x_pos, y_pos, 's', 1)  # delete south wall
                    self.setRoomValue(x_pos + 1, y_pos, 'n', 1)  # delete north wall next room
                    visited.append([x_pos + 1, y_pos])
                if random_wall.__contains__('e'):
                    self.setRoomValue(x_pos, y_pos, 'e', 1)  # delete south wall
                    self.setRoomValue(x_pos, y_pos + 1, 'w', 1)  # delete north wall next room
                    visited.append([x_pos, y_pos + 1])
            else:
                a = visited.pop()
                backtracked_rooms.append(a)
                backtrack_count += 1
            # set random mob spawn locations
            # self.ChunkMap[x_pos][y_pos][4] = random.randint(0, 1)

        if len(backtracked_rooms) > 2:
            visited[len(visited)-1]
            self.isMap_invalid = False
        # TODO
        # można testy też do tego napisac

    def setRoomValue(self, x, y, wall, visited):
        self.ChunkMap[x][y][2] = str(self.ChunkMap[x][y][2]).replace(wall, "")
        self.ChunkMap[x][y][3] = 1 if visited else 0
# ChunkSize = {'x': 8, 'y': 8}
