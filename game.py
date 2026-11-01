LINES = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)],
]


class Game:
    def __init__(self):
        self.cells = {}

    def cell(self, row, col):
        return self.cells.get((row, col), " ")

    def move(self, row, col):
        if self.winner() is not None:
            raise ValueError("Игра уже окончена")
        if not (0 <= row <= 2 and 0 <= col <= 2):
            raise ValueError("Такой клетки нет")
        if (row, col) in self.cells:
            raise ValueError("Клетка уже занята")
        if len(self.cells) % 2 == 0:
            self.cells[(row, col)] = "X"
        else:
            self.cells[(row, col)] = "O"

    def winner(self):
        for a, b, c in LINES:
            if a in self.cells and self.cells[a] == self.cells.get(b) == self.cells.get(c):
                return self.cells[a]
        return None

    def is_draw(self):
        return len(self.cells) == 9 and self.winner() is None

