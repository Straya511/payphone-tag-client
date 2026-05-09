from dataclasses import dataclass


@dataclass
class Payphone:
    idx: int
    longitude: float
    latitude: float
    indentifier: int
    status: str
    last_captured: str
    zero: int


@dataclass
class Player:
    name: str
    emoji: str
    colour: str
    shape: str
    cellId: int = 0


class Map:
    def __init__(self):
        self.cells = []
        self.payphones = []
        self.players: list[Player] = []
        self.reported: list[int] = []
        self.version: int = None