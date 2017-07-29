#!/usr/bin/env python
from __future__ import unicode_literals

import numpy as np

UNICODE_SPACE = unichr(0x20).encode('utf-8')
UNICODE_NEWLINE = '\n'.encode('utf-8')

class Cell(object):
    """
    A class representing a cell of 2x4 dots.
    """

    _dots = 0x2800 + np.array([[0x40, 0x80],
                               [0x04, 0x20],
                               [0x02, 0x10],
                               [0x01, 0x08]])

    def __init__(self, pattern=None):
        if pattern is not None:
            h, w = pattern.shape
            self.pattern = np.pad(pattern, ((0, 4-h),(0, 2-w)), mode='constant')
        else:
            self.reset()

    def set(self, x, y):
        assert 0 <= x < 2 and 0 <= y < 4
        self.pattern[y, x] = True

    def get(self, x, y):
        assert 0 <= x < 2 and 0 <= y < 4
        return self.pattern[y, x]

    def reset(self):
        self.pattern = np.zeros((4, 2), dtype=bool)

    def __str__(self):
        return self._to_unicode()

    def _to_unicode(self):
        code = 0
        for dot in (self._dots * self.pattern).flatten():
            code |= dot
        if code == 0:
            return UNICODE_SPACE
        return unichr(code).encode('utf-8')


class Canvas(object):
    """
    A class representing a canvas of braille cells.
    """

    def __init__(self, width, height, pattern=None):
        if pattern is not None:
            h, w = pattern.shape
            self._set_size(w, h)

            self._cells = np.empty((self._c_height, self._c_width), dtype=object)
            for y in np.arange(self._c_height):
                for x in np.arange(self._c_width):
                    y_start = y * 4
                    x_start = x * 2
                    cell_pat = pattern[y_start:y_start + 4, x_start:x_start + 2]
                    self._cells[y, x] = Cell(cell_pat)
        else:
            self._set_size(width, height)
            self.reset()

    def _set_size(self, width, height):
        self.width = width
        self.height = height

        self._c_width = np.ceil(width/2.0).astype(int)
        self._c_height = np.ceil(height/4.0).astype(int)

    def reset(self):
        self._cells = np.empty(self._c_height * self._c_width, dtype=object)
        for i in np.arange(len(self._cells)):
            self._cells[i] = Cell()
        self._cells = self._cells.reshape((self._c_height, self._c_width))

    def set(self, x, y):
        # Find cell coordinates.
        c_x = x // 2
        c_y = y // 4
        self._cells[c_y, c_x].set(x % 2, y % 4)

    def _to_unicode(self):
        rows = []
        for y in np.arange(self._c_height - 1, -1, -1):
            row = ''.encode('utf-8')
            for x in np.arange(self._c_width):
                row += str(self._cells[y, x]._to_unicode())
            rows.append(row)
        return UNICODE_NEWLINE.join(rows)

    def __str__(self):
        return self._to_unicode()

if __name__ == '__main__':
    cell = Cell()
    cell.set(0,0)
    cell2 = Cell()
    cell2.set(1,0)
    cell2.set(0,3)

    canvas = Canvas(100, 100)
    x = np.linspace(0, 2*np.pi, 100)
    y = 50 * np.sin(x) + 50
    for i, y_ in enumerate(y):
        canvas.set(i, int(y_))

    # canvas.set(0, 0)
    # canvas.set(10, 0)
    # canvas.set(0, 39)
    print canvas

    pattern = np.array([[1, 0, 0, 1],
                        [1, 0, 0, 1],
                        [1, 1, 1, 1],
                        [1, 0, 0, 1],
                        [1, 0, 0, 1],
                        [0, 1, 1, 0]], dtype=bool)

    canvas = Canvas(5,5, pattern=pattern)
    print canvas
