import copy
import logging
from typing import List

from numpy import array

from models import Figure, HeightOptions, FillingOptions, ColorOptions, ShapeOptions

logger = logging.getLogger("__name__")


class Board:
    def __init__(self):
        self.size = 4
        self.fields: array = array(self.__create_field(), dtype=Figure)

    def __create_field(self) -> List[List]:
        fields = list()
        rows = list()

        for j in range(self.size):
            for i in range(self.size):
                rows.append(None)
            fields.append(copy.deepcopy(rows))
            rows.clear()

        return fields

    def __repr__(self) -> str:
        to_print: str = "=================\nBoard with pieces\n\n"

        for row in self.fields:
            to_print = to_print + str(row) + "\n"

        to_print = to_print + "\n=================\n"

        return to_print

    def place(self, figure: Figure, x: int, y: int):
        assert 0 <= x < self.size
        assert 0 <= y < self.size

        if self.fields[x][y] is None:
            self.fields[x][y] = figure
        else:
            raise ValueError(f"Field {x}{y} already taken")

    def is_quarto(self) -> bool:
        return self._check_rows() or self._check_columns() or self._check_diagonals()

    def _check_rows(self) -> bool:
        for row in self.fields:
            if row.count(None) == 0:
                row_value = self._is_matching(figures=row)
                if row_value:
                    return True
        return False

    def _check_columns(self) -> bool:
        for i in range(self.size):
            entries = list()
            for j in range(self.size):
                entries.append(self.fields[j][i])

            if entries.count(None) == 0:
                column_matches = self._is_matching(figures=entries)
                if column_matches:
                    return True

        return False

    def _check_diagonals(self) -> bool:
        entries = list()
        for i in range(self.size):
            entries.append(self.fields[i][i])
        diagonal_1 = self._is_matching(figures=entries)

        entries = list()
        for i in range(self.size):
            entries.append(self.fields[self.size - i][self.size - i])
        diagonal_2 = self._is_matching(figures=entries)
        return diagonal_1 or diagonal_2

    def _is_matching(self, figures: List[Figure]) -> bool:
        figures = copy.deepcopy(figures)
        last = figures.pop()
        properties = ["height", "colour", "shape", "filling"]

        for prop in properties:
            for figure in figures:
                if figure.__getattribute__(prop) != last.__getattribute__(prop):
                    break
                return True
        return False


if __name__ == "__main__":
    board = Board()
    piece1 = Figure(
        height=HeightOptions.TALL,
        colour=ColorOptions.LIGHT,
        shape=ShapeOptions.ROUND,
        filling=FillingOptions.FULL,
    )

    piece2 = Figure(
        height=HeightOptions.TALL,
        colour=ColorOptions.LIGHT,
        shape=ShapeOptions.ROUND,
        filling=FillingOptions.FULL,
    )

    piece3 = Figure(
        height=HeightOptions.TALL,
        colour=ColorOptions.LIGHT,
        shape=ShapeOptions.ROUND,
        filling=FillingOptions.FULL,
    )

    piece4 = Figure(
        height=HeightOptions.SHORT,
        colour=ColorOptions.DARK,
        shape=ShapeOptions.SQUARE,
        filling=FillingOptions.EMPTY,
    )

    board.place(figure=piece1, x=0, y=0)
    board.place(figure=piece2, x=1, y=0)
    board.place(figure=piece3, x=2, y=0)
    board.place(figure=piece4, x=3, y=0)

    # print(piece.__getattribute__("height"))

    print(board)
    print(board.is_quarto())
