import pytest

from game import Game


def play(*moves):
    game = Game()
    for row, col in moves:
        game.move(row, col)
    return game


def test_create_game():
    Game()


def test_new_cell_is_empty():
    assert Game().cell(0, 0) == " "


def test_can_make_move():
    Game().move(0, 0)


def test_move_puts_x():
    assert play((0, 0)).cell(0, 0) == "X"


def test_move_does_not_touch_other_cells():
    assert play((0, 0)).cell(1, 1) == " "


def test_second_move_is_o():
    assert play((0, 0), (1, 1)).cell(1, 1) == "O"


def test_third_move_is_x():
    assert play((0, 0), (1, 1), (2, 2)).cell(2, 2) == "X"


def test_cannot_move_to_taken_cell():
    with pytest.raises(ValueError):
        play((0, 0), (0, 0))

def test_cannot_move_outside_board():
    with pytest.raises(ValueError):
        play((3, 3))


def test_no_winner_at_start():
    assert Game().winner() is None


def test_x_wins_by_row():
    assert play((0, 0), (1, 0), (0, 1), (1, 1), (0, 2)).winner() == "X"


def test_o_wins_by_column():
    assert play((0, 0), (0, 1), (1, 0), (1, 1), (2, 2), (2, 1)).winner() == "O"


def test_x_wins_by_diagonal():
    assert play((0, 0), (0, 1), (1, 1), (0, 2), (2, 2)).winner() == "X"


def test_full_board_without_winner_is_draw():
    game = play((0, 0), (0, 1), (0, 2), (1, 1), (1, 0), (1, 2), (2, 1), (2, 0), (2, 2))
    assert game.is_draw()


def test_cannot_move_after_win():
    with pytest.raises(ValueError):
        play((0, 0), (1, 0), (0, 1), (1, 1), (0, 2), (2, 2))
