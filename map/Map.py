

class Map:
    def __init__(self):
        self.ChunksX = 8  # 64
        self.ChunksY = 8  # 64

        self.ChunkMap = [[[0, 0] for x in range(self.ChunksX)] for y in range(self.ChunksY)]
        self.mapPrinter()

    def mapPrinter(self):

        for enumi, i in enumerate(self.ChunkMap):
            for enumj, j in enumerate(i):
                self.ChunkMap[enumi][enumj] = [enumi, enumj]

        print(self.ChunkMap)

    def rendaerMap(self):
        pass


ChunkSize = {'x': 8, 'y': 8}
