#!/usr/bin/env python
from __future__ import unicode_literals

import numpy as np

from termplotlib.colors import fg, bg
from termplotlib.canvas import Canvas

class RasterCanvas(Canvas):
    """
    A class representing a canvas of braille dots.
    """

    # A matrix containing the separate unicode values for each dot.
    _dots = 0x2800 + np.array([[0x40, 0x80],
                               [0x04, 0x20],
                               [0x02, 0x10],
                               [0x01, 0x08]])

    def __init__(self, width, height, stretchable=True, alignment='center', pattern=None, background=None):
        """Create a canvas.

        :param int width: The width (in dots) of the canvas.
        :param int height: The height (in dots) of the canvas.
        :param ndarray pattern: (optional) Initial pattern for the canvas. If no pattern is given
        an empty canvas is created.
        :param string background: The background color of the canvas.
        """
        super(RasterCanvas, self).__init__(width, height, stretchable, alignment)
        if pattern is not None:
            height, width = pattern.shape
            self._set_size(width, height)
            self.pattern = pattern.copy()
            self._color_map = np.zeros((self.height, self.width), dtype=str)
        else:
            self._set_size(width, height)
            self.reset()

        if background:
            self.background = bg[background]
        else:
            self.background = ''

    def _get_cell_dimensions(self, width, height):
        c_width  = np.ceil(width/2.0).astype(int)
        c_height = np.ceil(height/4.0).astype(int)
        return c_width, c_height

    def _set_size(self, width, height):
        self.width, self.height = width, height
        self._c_width, self._c_height = self._get_cell_dimensions(width, height)

    def reset(self):
        self.pattern = np.zeros((self.height, self.width), dtype=bool)
        self._color_map = np.chararray((self.height, self.width), itemsize=64)
        # Make sure the color map is initialized with empty strings.
        self._color_map[:] = ''

    def stretch(self, new_width, new_height):
        padding = self.get_padding(new_width, new_height)
        self.pattern = np.pad(self.pattern, padding, mode='constant')
        self._color_map = np.pad(self._color_map, padding, mode='constant')
        new_width = self.width + padding[1,:].sum()
        new_height = self.height + padding[0,:].sum()
        self._set_size(new_width, new_height)

    def set(self, x, y, color=None):
        # Check if the coordinates are iterable, otherwise put them into lists.
        if hasattr(x, '__iter__'):
            assert hasattr(y, '__iter__') and len(y) == len(x)
        else:
            x = [x]
            y = [y]

        color_str = fg[color] if color else ''

        # Add all coordinates, one by one.
        for xi, yi in zip(x, y):
            if xi >= self.width or yi >= self.height:
                raise ValueError('Coordinate ({}, {})is outside canvas size ({}, {})'
                                 .format(xi, yi, self.width, self.height))
            self.pattern[yi, xi] = True
            self._color_map[yi, xi] = color_str

    def _get_cell_pattern(self, pattern, x, y):
        cell = pattern[y*4:(y+1)*4, x*2:(x+1)*2]
        h, w = cell.shape
        return np.pad(cell, ((0, 4-h),(0, 2-w)), mode='constant')

    def _get_cell_color(self, cmap, x, y):
        colors = cmap[y*4:(y+1)*4, x*2:(x+1)*2].flatten()
        # Get the most used color for the cell
        counts = {}
        for c in colors:
            if len(c) > 0:
                counts[c] = counts.get(c, 0) + 1
        if len(counts) > 0:
            return sorted(counts, key=counts.get, reverse=True)[0]
        return ''

    def get_rows(self, width=None, height=None):
        width, height = self._check_dimensions(width, height)
        padding = self.get_padding(width, height)
        pattern = np.pad(self.pattern, padding, mode='constant')
        color_map = np.pad(self._color_map, padding, mode='constant')

        c_width, c_height = self._get_cell_dimensions(width, height)

        rows = []
        for y in reversed(np.arange(c_height)):
            row = self.background
            for x in np.arange(c_width):
                code = 0
                for dot in (self._dots * self._get_cell_pattern(pattern, x, y)).flatten():
                    code |= dot
                if code == 0:
                    row += ' '
                else:
                    color = self._get_cell_color(color_map, x, y)
                    row += color
                    row += unichr(code)
                    row += fg.RESET
            row += bg.RESET
            rows.append(row)
        return rows


if __name__ == '__main__':
    from letters import Text
    print Text('This is a plot!')
