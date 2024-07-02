from copy import copy
from src.constants import LARGE_NUMBER
import random
import math


class Vec2:
    @classmethod
    def two_points(self, point1: tuple[int | float, int | float], point2: tuple[int | float, int | float]) -> 'Vec2':
        return Vec2(point1[0] - point2[0], point1[1] - point2[1])
    
    @classmethod
    def random(self):
        return Vec2(random.randint(-LARGE_NUMBER, LARGE_NUMBER), 
                    random.randint(-LARGE_NUMBER, LARGE_NUMBER)).normalize()

    def __init__(self, x: int | float = 0, y: int | float = 0) -> None:
        self._x = x
        self._y = y

    def copy(self):
        return Vec2(copy(self._x), copy(self._x))

    def __add__(self, vec2):
        return Vec2(self._x + vec2.x, self._y + vec2.y)
    
    def __sub__(self, vec2):
        return Vec2(self._x - vec2.x, self._y - vec2.y)
    
    def __iadd__(self, vec2):
        return Vec2(self._x + vec2.x, self._y + vec2.y)
    
    def __isub__(self, vec2):
        return Vec2(self._x - vec2.x, self._y - vec2.y)
    
    def __mul__(self, value):
        return Vec2(self._x * value, self._y * value)
    
    def __len__(self):
        return self.lenght()
    
    def __str__(self):
        return f'Vector <{self._x, self._y}>'
    
    @property
    def x(self): return self._x

    @property
    def y(self): return self._y

    @property
    def xy(self): return [self._x, self._y]

    @x.setter
    def x(self, x: int | float):
        self._x = x

    @y.setter
    def y(self, y: int | float):
        self._y = y

    def lenght(self):
        return math.sqrt(self._x ** 2 + self._y ** 2) + 0.0001
    
    def normalize_at(self):
        l = self.lenght()
        self._x /= l
        self._y /= l

    def normalize(self) -> 'Vec2':
        l = self.lenght()
        return Vec2(self._x / l, self._y / l)
    
    @property
    def angle(self):
        return abs(math.degrees((math.atan2(self._y, self._x) - math.pi)))
    
    @property
    def is_dot(self):
        if self._x == 0 and self._y == 0:
            return True
        return False
    
    def rotate(self, angle: float | int):
        angle = math.radians(angle)
        x = copy(self._x)
        y = copy(self._y)
        rotated_x = x * math.cos(angle) - y * math.sin(angle)
        rotated_y = x * math.sin(angle) + y * math.cos(angle)
        self._x = rotated_x
        self._y = rotated_y
        
        return self

def vec2_to_list(value):
    if isinstance(value, Vec2):
        return value.xy
    elif isinstance(value, (list, tuple)):
        return value

def distance(pos1: list | Vec2, pos2: list | Vec2) -> int | float:
    pos1 = vec2_to_list(pos1)
    pos2 = vec2_to_list(pos2)
    return math.sqrt(
        (pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2
    )

def distance_x(pos1: list | Vec2, pos2: list | Vec2) -> int | float:
    pos1 = vec2_to_list(pos1)
    pos2 = vec2_to_list(pos2)
    return abs(pos1[0] - pos2[0])

def distance_y(pos1: list | Vec2, pos2: list | Vec2) -> int | float:
    pos1 = vec2_to_list(pos1)
    pos2 = vec2_to_list(pos2)
    return abs(pos1[1] - pos2[1])

def rect_in_rect(pos1: list | Vec2, size1: list, pos2: list | Vec2, size2: list) -> bool:
    pos1 = vec2_to_list(pos1)
    pos2 = vec2_to_list(pos2)

    center1 = [
        pos1[0] + size1[0] / 2,
        pos1[1] + size1[1] / 2
    ]
    center2 = [
        pos2[0] + size2[0] / 2,
        pos2[1] + size2[1] / 2
    ]
    x_dist = size1[0] / 2 + size2[0] / 2
    y_dist = size1[1] / 2 + size2[1] / 2

    if (distance_x(center1, center2) < x_dist and
        distance_y(center1, center2) < y_dist):
        return True
    return False