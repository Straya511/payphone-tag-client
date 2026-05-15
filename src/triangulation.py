from dataclasses import dataclass


@dataclass
class Coordinate:
    longitude: float
    latitude: float


@dataclass
class Edge:
    payphone_1: int
    payphone_2: int


@dataclass
class Triangle:
    payphone_1: int
    payphone_2: int
    payphone_3: int
    area: float  # TODO confirm name/value


class Triangulation:
    def __init__(self):
        self.coords: dict[int: Coordinate] = {}
        self.edges: list[Edge] = []
        self.triangles: list[Triangle] = []
