import random


class Map:
    def __init__(self):
        self.ChunksX = 4  # 64
        self.ChunksY = 4  # 64
        self.ChunkMap = [[[0, 0, 0] for _ in range(self.ChunksX)] for _ in range(self.ChunksY)]
        self.maze_start_x = random.randint(1, self.ChunksX - 2)
        self.maze_start_y = random.randint(1, self.ChunksY - 2)

        self.mapPrinter()

    def mapPrinter(self):
        # render map coords
        for enumx, x in enumerate(self.ChunkMap):
            for enumy, y in enumerate(x):
                self.ChunkMap[enumx][enumy] = [enumx, enumy, 'wnse', 0, 0]
        # random spawn
        # [0] maze_start_x = random.randint(1, self.ChunksX - 2)
        # [1]maze_start_y = random.randint(1, self.ChunksY - 2)
        # [2] walls
        # [3] visited
        # [4] mobs can spawn
        visited = list()
        visited.append([self.maze_start_x, self.maze_start_y])
        self.ChunkMap[self.maze_start_x][self.maze_start_y] = [self.maze_start_x, self.maze_start_y, 'wnse', 1, 0]
        backtrack_count = 0
        backtracked_room = False
        while self.ChunksX * self.ChunksY > len(visited) + backtrack_count:
            print(len(visited))
            print(self.ChunksX*self.ChunksY)
            # neighbours / breaking wall options
            stri = ""
            x_pos, y_pos = visited[len(visited) - 1]
            print(x_pos, y_pos)
            if x_pos > 0 and self.ChunkMap[x_pos - 1][y_pos][3] == 0:
                stri += 'n'
            if y_pos > 0 and self.ChunkMap[x_pos][y_pos - 1][3] == 0:
                stri += 'w'
            if x_pos < self.ChunksX - 1 and self.ChunkMap[x_pos + 1][y_pos][3] == 0:
                stri += 's'
            if y_pos < self.ChunksY - 1 and self.ChunkMap[x_pos][y_pos + 1][3] == 0:
                stri += 'e'

            if stri != "":
                if backtracked_room and backtrack_count == 1:
                    self.ChunkMap[x_pos][y_pos][4] = 1
                    backtracked_room = False
                print(f"stri: {stri}")
                random_wall = random.choice(stri)
                print(f"randomchaince: {random_wall}")
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
                backtracked_room = True
                visited.pop()
                backtrack_count += 1
            # set random mob spawn locations
            self.ChunkMap[x_pos][y_pos][4] = random.randint(0, 1)
        for x in self.ChunkMap:
            print(x)
        print("end")
        # TODO
        # można testy też do tego napisac

    def setRoomValue(self, x, y, wall, visited):
        self.ChunkMap[x][y][2] = str(self.ChunkMap[x][y][2]).replace(wall, "")
        self.ChunkMap[x][y][3] = 1 if visited else 0
# ChunkSize = {'x': 8, 'y': 8}
