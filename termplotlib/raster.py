#!/usr/bin/env python
from __future__ import unicode_literals

import numpy as np

from colors import fg, bg

UNICODE_SPACE = unichr(0x20).encode('utf-8')
UNICODE_NEWLINE = '\n'.encode('utf-8')

class Canvas(object):
    """
    A class representing a canvas of braille dots.
    """

    # A matrix containing the separate unicode values for each dot.
    _dots = 0x2800 + np.array([[0x40, 0x80],
                               [0x04, 0x20],
                               [0x02, 0x10],
                               [0x01, 0x08]])

    # Possible alignment values and their paddings used when stretching
    # the canvas.
    _alignments = {'bottomleft'   : np.array([[0, 1],    [0, 1]]),
                   'topleft'      : np.array([[1, 0],    [0, 1]]),
                   'bottomright'  : np.array([[0, 1],    [1, 0]]),
                   'topright'     : np.array([[1, 0],    [1, 0]]),
                   'center'       : np.array([[0.5, 0.5],[0.5, 0.5]]),
                   'centerleft'   : np.array([[0.5, 0.5],[0, 1]]),
                   'centerright'  : np.array([[0.5, 0.5],[1, 0]]),
                   'bottomcenter' : np.array([[0, 1],    [0.5, 0.5]]),
                   'topcenter'    : np.array([[1, 0],    [0.5, 0.5]]),
    }

    def __init__(self, width, height, pattern=None, background=None):
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

    def _get_cell_dim(self, width, height):
        c_width  = np.ceil(width/2.0).astype(int)
        c_height = np.ceil(height/4.0).astype(int)
        return c_width, c_height

    def _set_size(self, width, height):
        self.width, self.height = width, height
        self._c_width, self._c_height = self._get_cell_dim(width, height)

    def reset(self):
        self.pattern = np.zeros((self.height, self.width), dtype=bool)
        self._color_map = np.chararray((self.height, self.width), itemsize=15)

    def stretch(self, new_width, new_height, alignment='bottomleft'):
        padding = self.get_padding(new_width, new_height, alignment)
        self.pattern = np.pad(self.pattern, padding, mode='constant')
        self._color_map = np.pad(self._color_map, padding, mode='constant')
        self._set_size(new_width, new_height)

    def get_padding(self, new_width, new_height, alignment='bottomleft'):
        assert new_width >= self.width and new_height >= self.height
        assert alignment in self._alignments.keys()

        # Calculate padding based on the chosen alignment.
        padding = self._alignments[alignment].copy()
        padding[0,:] *= new_height - self.height
        padding[1,:] *= new_width - self.width

        # Make sure that we have integer padding, and that
        # the total padding results in the correct width/height.
        padding[0,0] = np.ceil(padding[0,0])
        padding[0,1] = np.floor(padding[0,1])
        padding[1,0] = np.ceil(padding[1,0])
        padding[1,1] = np.floor(padding[1,1])

        return padding.astype(int)

    def set(self, x, y, color=None):
        if hasattr(x, '__iter__'):
            assert hasattr(y, '__iter__') and len(y) == len(x)
        else:
            x = [x]
            y = [y]
        for xi, yi in zip(x, y):
            if xi >= self.width or yi >= self.height:
                raise ValueError('Coordinate ({}, {})is outside canvas size ({}, {})'
                                 .format(xi, yi, self.width, self.height))
            self.pattern[yi, xi] = True
            if color:
                self._color_map[yi, xi] = fg[color]

    def _get_cell_pattern(self, x, y, full_pattern):
        pattern = full_pattern[y*4:(y+1)*4, x*2:(x+1)*2]
        h, w = pattern.shape
        return np.pad(pattern, ((0, 4-h),(0, 2-w)), mode='constant')

    def _get_cell_color(self, x, y, full_cmap):
        colors = full_cmap[y*4:(y+1)*4, x*2:(x+1)*2].flatten()
        # Get the most used color for the cell
        counts = {}
        for c in colors:
            if c != '':
                counts[c] = counts.get(c, 0) + 1
        if len(counts) > 0:
            return sorted(counts, key=counts.get, reverse=True)[0]
        return ''

    def get_rows(self, width=None, height=None, alignment='bottomleft'):
        if width is None:
            width = self.width
        if height is None:
            height = self.height
        assert width >= self.width and height >= self.height
        padding = self.get_padding(width, height, alignment)
        pattern = np.pad(self.pattern, padding, mode='constant')
        color_map = np.pad(self._color_map, padding, mode='constant')

        c_width, c_height = self._get_cell_dim(width, height)

        rows = []
        for y in np.arange(c_height):
            row = self.background.encode('utf-8')
            for x in np.arange(c_width):
                code = 0
                for dot in (self._dots * self._get_cell_pattern(x, y, pattern)).flatten():
                    code |= dot
                if code == 0:
                    row += UNICODE_SPACE
                else:
                    color = self._get_cell_color(x, y, color_map)
                    row += color.encode('utf-8')
                    row += unichr(code).encode('utf-8')
                    row += fg.RESET.encode('utf-8')
            row += bg.RESET.encode('utf-8')
            rows.append(row)
        return rows

    def _to_unicode(self):
        rows = self.get_rows()
        return UNICODE_NEWLINE.join(reversed(rows))

    def __str__(self):
        return self._to_unicode()

if __name__ == '__main__':

    canvas = Canvas(100, 100, background='grey')
    x = np.linspace(0, 2*np.pi, 100)
    y = (48 * np.sin(x) + 50).astype(int)
    y2 = (48 * np.cos(x) + 50).astype(int)
    y3 =  ((x - np.pi)**3).astype(int)
    y3 -= min(y3)
    canvas.set(range(len(y)), y, color='red')
    canvas.set(range(len(y2)), y2, color='green')
    canvas.set(range(len(y3)), y3, color='orange')
    canvas.set(75, 75, color='purple')
    canvas.stretch(140, 140, 'center')
    print canvas

    from letters import Text
    print Text('This is a plot!')
