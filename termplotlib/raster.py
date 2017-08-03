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
    _alignments = {'bottomleft' : np.array([[0, 1],[0, 1]]),
                   'topleft'    : np.array([[1, 0],[0, 1]]),
                   'bottomright': np.array([[0, 1],[1, 0]]),
                   'topright'   : np.array([[1, 0],[1, 0]])}

    def __init__(self, width, height, pattern=None, background=None):
        if pattern is not None:
            height, width = pattern.shape
            self._set_size(width, height)
            self.pattern = pattern.copy()

        else:
            self._set_size(width, height)
            self.pattern = np.zeros((self.height, self.width), dtype=bool)

        if background:
            self.background = bg[background]
        else:
            self.background = ''

    def _set_size(self, width, height):
        self.width = width
        self.height = height

        self._c_width  = np.ceil(width/2.0).astype(int)
        self._c_height = np.ceil(height/4.0).astype(int)

    def reset(self):
        self.pattern = np.zeros((self.height, self.width), dtype=bool)

    def stretch(self, new_width, new_height, alignment='bottomleft'):
        assert new_width >= self.width and new_height >= self.height
        assert alignment in self._alignments.keys()
        padding = self._alignments[alignment]
        padding[0,:] *= new_height - self.height
        padding[1,:] *= new_width - self.width
        self.pattern = np.pad(self.pattern, padding, mode='constant')
        self._set_size(new_width, new_height)

    def set(self, x, y):
        # Find cell coordinates.
        assert 0 <= x < self.width and 0 <= y < self.height
        self.pattern[y, x] = True

    def _get_cell_pattern(self, x, y):
        pattern = self.pattern[y*4:(y+1)*4, x*2:(x+1)*2]
        h, w = pattern.shape
        return np.pad(pattern, ((0, 4-h),(0, 2-w)), mode='constant')

    def _to_unicode(self):
        rows = []
        for y in np.arange(self._c_height):
            row = self.background.encode('utf-8')
            for x in np.arange(self._c_width):
                code = 0
                for dot in (self._dots * self._get_cell_pattern(x, y)).flatten():
                    code |= dot
                if code == 0:
                    row += UNICODE_SPACE
                else:
                    row += unichr(code).encode('utf-8')
            row += bg.RESET.encode('utf-8')
            rows.append(row)
        return UNICODE_NEWLINE.join(reversed(rows))

    def __str__(self):
        return self._to_unicode()

if __name__ == '__main__':

    canvas = Canvas(100, 100)
    x = np.linspace(0, 2*np.pi, 100)
    y = 48 * np.sin(x) + 50
    y2 = 48 * np.cos(x) + 50
    y3 =  (x - np.pi)**3
    y3 -= min(y3)
    for i, (y_, y2_, y3_) in enumerate(zip(y, y2, y3)):
        canvas.set(i, int(y_))
        canvas.set(i, int(y2_))
        canvas.set(i, int(y3_))

    print canvas

    from letters import Text
    print Text('This is a plot!')
