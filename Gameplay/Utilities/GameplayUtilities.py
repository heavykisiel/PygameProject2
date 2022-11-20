import random

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
    for door in self.doorlistv2:
        for xx in lista:
            if xx.contains(door):
                lista.remove(xx)
    print(f"door length: {len(self.doorlistv2)}  |  lista length after: {len(lista)} ")
    return lista


def one_door_rooms(self):
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
                if len(doorStr) == 1:
                    listC.append(tile)

    return listC


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
                raise Exception(f"Propably not all elements are properly deleted in Extraction_list_of_rooms: {Extraction_list_of_rooms}")
                return 1234 # will cause error
        else:
            raise Exception(f"SpawnRoom is None. SpawnRoom: {SpawnRoom}")
            return 1235 # will cause error

    else:
        raise Exception(f"OneDoorRooms.len is less than 2. OneDoorRooms.len: {self.OneDoorRooms} OneDoorRooms.len {len(self.OneDoorRooms)}")
        return 1236 # will cause error

def room_function_setter(self):
    specialRoomData = self.isOneDoorRoomsvalidData
    if specialRoomData is None:
        raise Exception("None!!!")
    if specialRoomData['SpawnRoom'] is None:
        raise Exception("None SpawnRoom")
    for enumx, x in enumerate(self.map_Data.ChunkMap):
        for enumy, y in enumerate(x):
            # print(f"{specialRoomData['SpawnRoom'][1]}=={y[1]},  {specialRoomData['SpawnRoom'][0]}=={y[0]}")
            if specialRoomData["SpawnRoom"][0] == y[1] and specialRoomData["SpawnRoom"][1] == y[0]:
                self.map_Data.ChunkMap[enumx][enumy][4] = "Spawn"
            if specialRoomData["KeyRoom"][0] == y[0] and specialRoomData["KeyRoom"][1] == y[1]:
                self.map_Data.ChunkMap[enumx][enumy][4] = "Key"
            if specialRoomData["BossRoom"][0] == y[1] and specialRoomData["BossRoom"][1] == y[0]:
                self.map_Data.ChunkMap[enumx][enumy][4] = "Boss"
            if specialRoomData is not None:
                for i in specialRoomData["BonusRooms"]:
                    if i[0] == y[0] and i[1] == y[1]:
                        self.map_Data.ChunkMap[enumx][enumy][4] = "Bonus"
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
                if len(tile[2]) == 1:
                    self.map_Data
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
