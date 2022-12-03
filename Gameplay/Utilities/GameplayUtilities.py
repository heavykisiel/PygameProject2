import random

from pygame.rect import Rect

from roomData import roomData


def opted_walls(gameplay):
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
                                tileC == self.texture_count_per_tiley - 2 or tileC == self.texture_count_per_tiley - 1 or tileC == 0 or tileC == 1:
                            border_pos = Rect(tile[0] * self.rectSizex + rowC * self.block_pixelsx,
                                              tile[1] * self.rectSizey + tileC * self.block_pixelsy,
                                              self.block_pixelsx, self.block_pixelsy)
                            lista.append(border_pos)
    for door in self.doorlistv2:
        for xx in lista:
            if xx.contains(door):
                lista.remove(xx)
    print(f"door length: {len(self.doorlistv2)}  |  lista length after: {len(lista)} ")
    return lista

def BossRoomDoors(self):
    listb = list()
    for y, row in enumerate(self.map_Data.ChunkMap):
        for x, tile in enumerate(row):
            print(tile)
            if tile[4].roomCode == 'Boss':
                if not tile[2].__contains__('w'):
                    offset_pos = Rect(tile[0] * self.rectSizex + 9 * self.block_pixelsx,
                                      tile[1] * self.rectSizey - 60, self.block_pixelsx, self.block_pixelsy)
                    listb.append(offset_pos)
                    offset_pos = Rect(tile[0] * self.rectSizex + 8 * self.block_pixelsx,
                                      tile[1] * self.rectSizey - 60, self.block_pixelsx, self.block_pixelsy)
                    listb.append(offset_pos)
                    offset_pos = Rect(tile[0] * self.rectSizex + 10 * self.block_pixelsx,
                                      tile[1] * self.rectSizey - 60, self.block_pixelsx, self.block_pixelsy)
                    listb.append(offset_pos)
                    print(f"{tile[2]} w, current chunk {tile[0]}{tile[1]}")
                elif not tile[2].__contains__('e'):
                    offset_pos = Rect(tile[0] * self.rectSizex + 9 * self.block_pixelsx,
                                      tile[1] * self.rectSizey + self.rectSizey + 60, self.block_pixelsx,
                                      self.block_pixelsy)
                    listb.append(offset_pos)
                    offset_pos = Rect(tile[0] * self.rectSizex + 8 * self.block_pixelsx,
                                      tile[1] * self.rectSizey + self.rectSizey + 60, self.block_pixelsx,
                                      self.block_pixelsy)
                    listb.append(offset_pos)
                    offset_pos = Rect(tile[0] * self.rectSizex + 10 * self.block_pixelsx,
                                      tile[1] * self.rectSizey + self.rectSizey + 60, self.block_pixelsx,
                                      self.block_pixelsy)
                    listb.append(offset_pos)
                    print(f"{tile[2]} e, current chunk {tile[0]}{tile[1]}")
                elif not tile[2].__contains__('n'):
                    offset_pos = Rect(tile[0] * self.rectSizex - 60,
                                      tile[1] * self.rectSizey + 6 * self.block_pixelsx, self.block_pixelsx,
                                      self.block_pixelsy)
                    listb.append(offset_pos)
                    offset_pos = Rect(tile[0] * self.rectSizex - 60,
                                      tile[1] * self.rectSizey + 5 * self.block_pixelsx, self.block_pixelsx,
                                      self.block_pixelsy)
                    listb.append(offset_pos)
                    offset_pos = Rect(tile[0] * self.rectSizex - 60,
                                      tile[1] * self.rectSizey + 7 * self.block_pixelsx, self.block_pixelsx,
                                      self.block_pixelsy)
                    listb.append(offset_pos)
                    print(f"{tile[2]} n, current chunk {tile[0]}{tile[1]}")
                elif not tile[2].__contains__('s'):
                    offset_pos = Rect(tile[0] * self.rectSizex + self.rectSizex,
                                      tile[1] * self.rectSizey + 6 * self.block_pixelsx, self.block_pixelsx,
                                      self.block_pixelsy)
                    listb.append(offset_pos)
                    offset_pos = Rect(tile[0] * self.rectSizex + self.rectSizex,
                                      tile[1] * self.rectSizey + 5 * self.block_pixelsx, self.block_pixelsx,
                                      self.block_pixelsy)
                    listb.append(offset_pos)
                    offset_pos = Rect(tile[0] * self.rectSizex + self.rectSizex,
                                      tile[1] * self.rectSizey + 7 * self.block_pixelsx, self.block_pixelsx,
                                      self.block_pixelsy)
                    listb.append(offset_pos)
                    print(f"{tile[2]} s, current chunk {tile[0]}{tile[1]}")
                else:
                    raise Exception(f"cannot find bossRoom's walls, {tile[2]}")

    return listb

def addBossDoors(self):
    lista = self.doorBoss
    listb = self.wall_collider_rect
    for x in lista:
        listb.append(x)
    return listb

def removeBossDoors(self):
    lista = self.doorBoss
    listb = self.wall_collider_rect
    for x in lista:
        listb.remove(x)
    return listb
def one_door_rooms(self):
    list_c = list()
    for y, row in enumerate(self.map_Data.ChunkMap):
        for x, tile in enumerate(row):
            if tile:
                door_str = "wnse"
                if str(tile[2]).__contains__('w'):
                    door_str = door_str.replace('w', '')
                if str(tile[2]).__contains__('n'):
                    door_str = door_str.replace('n', '')
                if str(tile[2]).__contains__('s'):
                    door_str = door_str.replace('s', '')
                if str(tile[2]).__contains__('e'):
                    door_str = door_str.replace('e', '')
                if len(door_str) == 1:
                    list_c.append(tile)

    return list_c


def one_door_rooms_validation(self):
    if len(self.OneDoorRooms) > 2:
        SpawnRoom = None
        Extraction_list_of_rooms = list()
        BonusRoomList = list()
        for x in self.OneDoorRooms:
            Extraction_list_of_rooms.append(x)
            if x[0] == self.map_Data.maze_start_x and x[1] == self.map_Data.maze_start_y:
                SpawnRoom = x
        if SpawnRoom is None:
            print("error")
            raise Exception("NONE SPAWNROOM")

        if SpawnRoom is not None:
            Extraction_list_of_rooms.remove(SpawnRoom)
            random_boos_room = random.choice(Extraction_list_of_rooms)
            Extraction_list_of_rooms.remove(random_boos_room)
            random_key_room = random.choice(Extraction_list_of_rooms)
            Extraction_list_of_rooms.remove(random_key_room)
            if len(Extraction_list_of_rooms) > 0:
                while len(Extraction_list_of_rooms) > 0:
                    BonusRoomList.append(Extraction_list_of_rooms.pop())
                print(f"BonusRoomList: {BonusRoomList}")
                print(f"Extraction_list_of_rooms: {Extraction_list_of_rooms} len : {len(Extraction_list_of_rooms)}")

            if len(Extraction_list_of_rooms) == 0:
                returnData = {
                    "SpawnRoom": SpawnRoom,
                    "BossRoom": random_boos_room,
                    "KeyRoom": random_key_room,
                    "BonusRooms": BonusRoomList
                }
                print(returnData)
                return returnData
            else:
                raise Exception(
                    f"Propably not all elements are properly deleted in Extraction_list_of_rooms: {Extraction_list_of_rooms}")
        else:
            raise Exception(f"SpawnRoom is None. SpawnRoom: {SpawnRoom}")
    else:
        raise Exception(
            f"OneDoorRooms.len is less than 2. OneDoorRooms.len: {self.OneDoorRooms} OneDoorRooms.len {len(self.OneDoorRooms)}")


def add_mob_chunks(self):
    for enumx, x in enumerate(self.map_Data.ChunkMap):
        for enumy, y in enumerate(x):
            if y[4] == '':
                self.map_Data.ChunkMap[enumx][enumy][4] = roomData("Room", (enumx, enumy), self.wall_collider_rect)

                # TODO
    declared_mobs = 20
    while declared_mobs >= 0:
        rX = random.randint(0, 3)
        rY = random.randint(0, 3)
        self.map_Data.ChunkMap[rX][rY][4].mobsCount = 1
        declared_mobs -= 1
    print(self.map_Data.ChunkMap)
    return self.map_Data


def room_function_setter(self):
    special_room_data = self.isOneDoorRoomsvalidData
    if special_room_data is None:
        raise Exception("None!!!")
    if special_room_data['SpawnRoom'] is None:
        raise Exception("None SpawnRoom")
    for enumx, x in enumerate(self.map_Data.ChunkMap):
        for enumy, y in enumerate(x):
            # print(f"{special_room_data['SpawnRoom'][1]}=={y[1]},  {special_room_data['SpawnRoom'][0]}=={y[0]}")
            if special_room_data["SpawnRoom"][0] == y[0] and special_room_data["SpawnRoom"][1] == y[1]:
                self.map_Data.ChunkMap[enumx][enumy][4] = roomData("Spawn", (enumx, enumy), self.wall_collider_rect)
            if special_room_data["KeyRoom"][0] == y[0] and special_room_data["KeyRoom"][1] == y[1]:
                self.map_Data.ChunkMap[enumx][enumy][4] = roomData("Key", (enumx, enumy), self.wall_collider_rect)
            if special_room_data["BossRoom"][0] == y[0] and special_room_data["BossRoom"][1] == y[1]:
                self.map_Data.ChunkMap[enumx][enumy][4] = roomData("Boss", (enumx, enumy), self.wall_collider_rect)
            if special_room_data is not None:
                for i in special_room_data["BonusRooms"]:
                    if i[0] == y[0] and i[1] == y[1]:
                        self.map_Data.ChunkMap[enumx][enumy][4] = roomData("Bonus", (enumx, enumy),
                                                                           self.wall_collider_rect)
    return self.map_Data


def doors(self):
    listC = list()
    for y, row in enumerate(self.map_Data.ChunkMap):
        for x, tile in enumerate(row):
            if tile:
                doorStr = "wnse"
                if str(tile[2]).__contains__('w'):
                    doorStr = doorStr.replace('w', '')
                if str(tile[2]).__contains__('n'):
                    doorStr = doorStr.replace('n', '')
                if str(tile[2]).__contains__('s'):
                    doorStr = doorStr.replace('s', '')
                if str(tile[2]).__contains__('e'):
                    doorStr = doorStr.replace('e', '')
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
                        if doorStr.__contains__('w') and ((rowC == self.texture_count_per_tilex / 2 and
                                                           tileC == 0) or (rowC == self.texture_count_per_tilex / 2 and
                                                                           tileC == 1)):
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

                        if doorStr.__contains__('e') and ((tileC == self.texture_count_per_tiley - 1 and
                                                           rowC == self.texture_count_per_tilex / 2) or (
                                                                  tileC == self.texture_count_per_tiley - 2 and
                                                                  rowC == self.texture_count_per_tilex / 2)):
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
