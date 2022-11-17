from pygame.rect import Rect


def OptedWalls(gameplay):
    # currently unused
    a = list()
    for x in gameplay.wall_collider_rect:
        if x.x < 1100:
            a.append(x)
        elif x.y < 800:
            a.append(x)
    return a


def detect_rect_colliders(self):
    lista = list()
    for y, row in enumerate(self.map_Data.ChunkMap):
        for x, tile in enumerate(row):
            if tile:
                for rowC in range(self.texture_count_per_tilex):
                    for tileC in range(self.texture_count_per_tiley):
                        if rowC == self.texture_count_per_tilex - 1 or rowC == 0 or \
                                tileC == self.texture_count_per_tiley - 1 or tileC == 0:
                            border_pos = Rect(tile[0] * self.rectSizex + rowC * self.block_pixelsx,
                                              tile[1] * self.rectSizey + tileC * self.block_pixelsy,
                                              self.block_pixelsx, self.block_pixelsy)
                            lista.append(border_pos)
                            # if (rowC == self.texture_count_per_tilex / 2 and (
                            #         tileC == self.texture_count_per_tiley - 1 or tileC == 0)) or \
                            #         (tileC == self.texture_count_per_tiley / 2 and (
                            #                 rowC == self.texture_count_per_tilex - 1 or rowC == 0)):
                            #     door_pos = Rect(tile[0] * self.rectSizex + rowC * self.block_pixelsx,
                            #                     tile[1] * self.rectSizey + tileC * self.block_pixelsy,
                            #                     self.block_pixelsx, self.block_pixelsy)
                            #     listb.append(door_pos)
    print(f"lista len before: {len(lista)}")
    for door in self.doorlistv2:
        for xx in lista:
            if xx.contains(door):
                print(f"{door}")
                lista.remove(xx)
    print(f"door length: {len(self.doorlistv2)}  |  lista length after: {len(lista)} ")
    return lista
def one_door_rooms(self):
    listC = list()
    for y, row in enumerate(self.map_Data.ChunkMap):
        for x, tile in enumerate(row):
            if tile:
                doorStr = "wnse"
                print(f"{tile[2]}")
                if str(tile[2]).__contains__('w'):
                    doorStr = doorStr.replace('w', '')
                if str(tile[2]).__contains__('n'):
                    doorStr = doorStr.replace('n', '')
                if str(tile[2]).__contains__('s'):
                    doorStr = doorStr.replace('s', '')
                if str(tile[2]).__contains__('e'):
                    doorStr = doorStr.replace('e', '')
                if len(doorStr) == 1:
                    listC.append(tile)

    return listC
# def one_door_rooms_validation(listOneDoor):
#     if len(listOneDoor) == 3:

def doors(self):
    listC = list()
    for y, row in enumerate(self.map_Data.ChunkMap):
        for x, tile in enumerate(row):
            if tile:
                doorStr = "wnse"
                print(f"{tile[2]}")
                if str(tile[2]).__contains__('w'):
                    doorStr = doorStr.replace('w', '')
                if str(tile[2]).__contains__('n'):
                    doorStr = doorStr.replace('n', '')
                if str(tile[2]).__contains__('s'):
                    doorStr = doorStr.replace('s', '')
                if str(tile[2]).__contains__('e'):
                    doorStr = doorStr.replace('e', '')
                if len(tile[2]) == 1:
                    self.map_Data
                print(f"kierunek drzwii {doorStr} w chunku x:{tile[0]} y:{tile[1]}")
                for rowC in range(self.texture_count_per_tilex):
                    for tileC in range(self.texture_count_per_tiley):
                        if doorStr.__contains__('n') and (rowC == 0 and
                                                          tileC == self.texture_count_per_tiley / 2):
                            door_pos = Rect(tile[0] * self.rectSizex + rowC * self.block_pixelsx,
                                            tile[1] * self.rectSizey + tileC * self.block_pixelsy,
                                            self.block_pixelsx, self.block_pixelsy)
                            listC.append(door_pos)
                            door_pos = Rect(tile[0] * self.rectSizex + rowC * self.block_pixelsx,
                                            tile[1] * self.rectSizey + (tileC - 1) * self.block_pixelsy,
                                            self.block_pixelsx, self.block_pixelsy)
                            listC.append(door_pos)
                            door_pos = Rect(tile[0] * self.rectSizex + rowC * self.block_pixelsx,
                                            tile[1] * self.rectSizey + (tileC + 1) * self.block_pixelsy,
                                            self.block_pixelsx, self.block_pixelsy)
                            listC.append(door_pos)
                        if doorStr.__contains__('w') and (
                                rowC == self.texture_count_per_tilex / 2 and
                                tileC == 0):
                            door_pos = Rect(tile[0] * self.rectSizex + rowC * self.block_pixelsx,
                                            tile[1] * self.rectSizey + tileC * self.block_pixelsy,
                                            self.block_pixelsx, self.block_pixelsy)
                            listC.append(door_pos)
                            door_pos = Rect(tile[0] * self.rectSizex + (rowC + 1) * self.block_pixelsx,
                                            tile[1] * self.rectSizey + tileC * self.block_pixelsy,
                                            self.block_pixelsx, self.block_pixelsy)
                            listC.append(door_pos)
                            door_pos = Rect(tile[0] * self.rectSizex + (rowC - 1) * self.block_pixelsx,
                                            tile[1] * self.rectSizey + tileC * self.block_pixelsy,
                                            self.block_pixelsx, self.block_pixelsy)
                            listC.append(door_pos)

                        if doorStr.__contains__('s') and (tileC == self.texture_count_per_tiley / 2 and
                                                          rowC == self.texture_count_per_tilex - 1):
                            door_pos = Rect(tile[0] * self.rectSizex + rowC * self.block_pixelsx,
                                            tile[1] * self.rectSizey + tileC * self.block_pixelsy,
                                            self.block_pixelsx, self.block_pixelsy)
                            listC.append(door_pos)
                            door_pos = Rect(tile[0] * self.rectSizex + rowC * self.block_pixelsx,
                                            tile[1] * self.rectSizey + (tileC - 1) * self.block_pixelsy,
                                            self.block_pixelsx, self.block_pixelsy)
                            listC.append(door_pos)
                            door_pos = Rect(tile[0] * self.rectSizex + rowC * self.block_pixelsx,
                                            tile[1] * self.rectSizey + (tileC + 1) * self.block_pixelsy,
                                            self.block_pixelsx, self.block_pixelsy)
                            listC.append(door_pos)

                        if doorStr.__contains__('e') and (tileC == self.texture_count_per_tiley - 1 and
                                                          rowC == self.texture_count_per_tilex / 2):
                            door_pos = Rect(tile[0] * self.rectSizex + rowC * self.block_pixelsx,
                                            tile[1] * self.rectSizey + tileC * self.block_pixelsy,
                                            self.block_pixelsx, self.block_pixelsy)
                            listC.append(door_pos)
                            door_pos = Rect(tile[0] * self.rectSizex + (rowC + 1) * self.block_pixelsx,
                                            tile[1] * self.rectSizey + tileC * self.block_pixelsy,
                                            self.block_pixelsx, self.block_pixelsy)
                            listC.append(door_pos)
                            door_pos = Rect(tile[0] * self.rectSizex + (rowC - 1) * self.block_pixelsx,
                                            tile[1] * self.rectSizey + tileC * self.block_pixelsy,
                                            self.block_pixelsx, self.block_pixelsy)
                            listC.append(door_pos)

    return listC
