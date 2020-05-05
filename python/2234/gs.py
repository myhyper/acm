import sys
DEBUG = True
# DEBUG = False
if DEBUG:
    f = open("input2.txt")
else:
    f = sys.stdin
# Global variable
direction = [[-1,0],[1,0],[0,-1],[0,1]]
south, east, north, west = 0,1,2,3
# Class
class room_info(object):
    room_count = 0
    def __init__(self):
        self.__wall = list()
        self.__room_number = 0
        self.__visit = False
        self.__maximum_numberOfRoom_withNoOneWall = 0
    @staticmethod
    def get_room_count():
        return room_info.room_count
    @property
    def wall(self):
        return self.__wall
    @property
    def room_number(self):
        return self.__room_number
    @property
    def visit(self):
        return self.__visit
    @property
    def maximum_numberOfRoom_withNoOneWall(self):
        return self.__maximum_numberOfRoom_withNoOneWall
    @wall.setter
    def wall(self, wall):
        if not isinstance(wall, list):
            raise TypeError("Must be a list!")
        self.__wall = wall
    @room_number.setter
    def room_number(self, room_number):
        if not isinstance(room_number, int):
            raise TypeError("Must be an int!")
        self.__room_number = room_number
    @visit.setter
    def visit(self, visit):
        if not isinstance(visit, bool):
            raise TypeError("Must be a bool!")
        self.__visit = visit
    @maximum_numberOfRoom_withNoOneWall.setter
    def maximum_numberOfRoom_withNoOneWall(self, maximum_numberOfRoom_withNoOneWall):
        if not isinstance(maximum_numberOfRoom_withNoOneWall, int):
            raise TypeError("Must be an int!")
        self.__maximum_numberOfRoom_withNoOneWall = maximum_numberOfRoom_withNoOneWall
# Function
def get_wall_direction(wall_num):
    wall = list(map(int, list(format(wall_num, 'b').zfill(4))))
    return wall
def traverse(x, y):
    room_info.room_count += 1
    queue = [[x,y]]
    x_cord, y_cord = 0, 0
    while len(queue) > 0:
        x_cord, y_cord = queue[0]
        queue.remove(queue[0])
        castle_rooms[x_cord][y_cord].visit = True
        castle_rooms[x_cord][y_cord].room_number = room_info.get_room_count()
        for row, col in direction:
            if (x_cord+row) < 0 or (x_cord+row) >= m or (y_cord+col) < 0 or (y_cord+col) >= n:
                continue
            if castle_rooms[x_cord+row][y_cord+col].visit:
                continue
            if ((row == -1) and (col == 0) and (castle_rooms[x_cord][y_cord].wall[north] == False)) or ((row == 1) and (col == 0) and (castle_rooms[x_cord][y_cord].wall[south] == False)) or ((row == 0) and (col == -1) and (castle_rooms[x_cord][y_cord].wall[west] == False)) or ((row == 0) and (col == 1) and (castle_rooms[x_cord][y_cord].wall[east] == False)):
                queue.append([x_cord+row, y_cord+col])
# Input
n, m = list(map(int, f.readline().split()))
castle_wall = [list(map(int, f.readline().split())) for _ in range(m)]
castle_rooms = [[room_info() for __ in range (n)] for _ in range(m)]
# Wall assignment
for x in range(m):
    for y in range(n):
        castle_rooms[x][y].wall = get_wall_direction(castle_wall[x][y])
# Traverse
for x in range(m):
    for y in range(n):
        if not castle_rooms[x][y].visit:
            traverse(x,y)
# Seek for answers
# -prob2.
area = [0 for _ in range(room_info.get_room_count())]
max_area = 0
for x in range(m):
    for y in range(n):
        index = castle_rooms[x][y].room_number-1
        area[index]+=1
for _ in area:
    max_area = max(max_area, _)
# -prob3.
max_area_withoutWall = 0
for x in range(m):
    for y in range(n):
        for row, col in direction:
            if (x+row) < 0 or (x+row) >= m or (y+col) < 0 or (y+col) >= n:
                continue
            if ((row == -1) and (col == 0) and (castle_rooms[x][y].wall[north] == True)) or ((row == 1) and (col == 0) and (castle_rooms[x][y].wall[south] == True)) or ((row == 0) and (col == -1) and (castle_rooms[x][y].wall[west] == True)) or ((row == 0) and (col == 1) and (castle_rooms[x][y].wall[east] == True)):
                if castle_rooms[x][y].room_number != castle_rooms[x+row][y+col].room_number:
                    castle_rooms[x][y].maximum_numberOfRoom_withNoOneWall = max(castle_rooms[x][y].maximum_numberOfRoom_withNoOneWall, area[castle_rooms[x][y].room_number-1]+area[castle_rooms[x+row][y+col].room_number-1])
        max_area_withoutWall = max(max_area_withoutWall, castle_rooms[x][y].maximum_numberOfRoom_withNoOneWall)
# End
print(room_info.get_room_count())
print(max_area)
print(max_area_withoutWall)
f.close()