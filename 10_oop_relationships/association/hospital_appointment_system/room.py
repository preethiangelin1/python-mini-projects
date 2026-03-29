class Room:
    def __init__(self, number: str, floor: int):
        self._number = number
        self._floor = floor

    @property
    def number(self):
        return self._number

    @property
    def floor(self):
        return self._floor