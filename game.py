"""Игра «Крестики-нолики» на поле 3 на 3.

Первым ходит X, дальше игроки ходят по очереди. Побеждает тот,
кто первым займёт три клетки подряд по горизонтали, вертикали
или диагонали. Если поле заполнено, а победителя нет, это ничья.
"""

__version__ = "1.0.0"

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
"""Все линии, которые дают победу: три строки, три столбца и две диагонали."""


class Game:
    """Одна партия. Клетки задаются номером строки и столбца от 0 до 2."""

    def __init__(self):
        self.cells = {}

    def cell(self, row, col):
        """Возвращает "X", "O" или пробел, если клетка пустая."""
        return self.cells.get((row, col), " ")

    def move(self, row, col):
        """Ставит знак игрока, чей сейчас ход, в клетку (row, col).

        Вызывает ValueError, если игра уже окончена, такой клетки нет
        или клетка занята.
        """
        if self.winner() is not None:
            raise ValueError("Игра уже окончена")
        if not (0 <= row <= 2 and 0 <= col <= 2):
            raise ValueError("Такой клетки нет")
        if (row, col) in self.cells:
            raise ValueError("Клетка уже занята")
        self.cells[(row, col)] = self.current_player()

    def winner(self):
        """Возвращает "X" или "O", если кто-то собрал линию, иначе None."""
        for a, b, c in LINES:
            if a in self.cells and self.cells[a] == self.cells.get(b) == self.cells.get(c):
                return self.cells[a]
        return None

    def is_draw(self):
        """True, если поле заполнено и победителя нет."""
        return len(self.cells) == 9 and self.winner() is None

    def current_player(self):
        """Чей сейчас ход: "X" или "O". None, если уже есть победитель."""
        if self.winner() is not None:
            return None
        if len(self.cells) % 2 == 0:
            return "X"
        return "O"
