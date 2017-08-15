"""
Classes to control the layout of multiple canvases.
"""
from __future__ import unicode_literals

import numpy as np

from raster import RasterCanvas
from canvas import Canvas

class Row(Canvas):
    """
    Places all canvases in a row with a height equal to the largest
    canvas.
    """

    def __init__(self, canvases=None, width=0, height=0, stretchable=True, alignment='center'):
        super(Row, self).__init__(width, height, stretchable, alignment)
        self.width = 0
        self.height = 0
        self.canvases = []
        if canvases:
            for canvas in canvases:
                self.add_canvas(canvas)

    def add_canvas(self, canvas):
        self.height = max(self.height, canvas.height)
        self.width += canvas.width
        self.canvases.append(canvas)

    def get_rows(self, width=None, height=None):
        width, height = self._check_dimensions(width, height)
        total_stretch_width = width - self.width
        n_stretchable = len([c for c in self.canvases if c.stretchable])
        if n_stretchable > 0:
            stretch_width = int(total_stretch_width / float(n_stretchable))
        else:
            stretch_width = 0

        rows = []
        canvas_rows = []
        for canvas in self.canvases:
            c_rows = canvas.get_rows(canvas.width + stretch_width, height)
            canvas_rows.append(c_rows)
        for row_tuple in zip(*canvas_rows):
            rows.append(''.join(row_tuple))
        return rows

class Column(Canvas):
    """
    Places all canvases in a column with a width equal to the largest
    canvas.
    """

    def __init__(self, canvases=None, width=0, height=0, stretchable=True, alignment='center'):
        self.width = 0
        self.height = 0
        self.canvases = []
        if canvases:
            for canvas in canvases:
                self.add_canvas(canvas)
        super(Column, self).__init__(self.width, self.height, stretchable, alignment)

    def add_canvas(self, canvas):
        self.width = max(self.width, canvas.width)
        self.height += canvas.height
        self.canvases.append(canvas)

    def get_rows(self, width=None, height=None):
        width, height = self._check_dimensions(width, height)

        rows = []
        for canvas in self.canvases:
            rows.extend(canvas.get_rows(width, canvas.height))
        return rows

if __name__ == '__main__':

    c1 = RasterCanvas(30, 30, background='white')
    c2 = RasterCanvas(50, 50, background='grey')

    x1 = np.linspace(0, 2*np.pi, 30)
    x2 = np.linspace(0, 4*np.pi, 50)
    y1 = 30 * np.abs(np.sin(x1))
    y2 = 25 * np.sin(x2) + 25
    c1.set(range(len(y1)), y1.astype(int), color='blue')
    c2.set(range(len(y2)), y2.astype(int), color='red')

    r = Row([c1, c2])
    print r

    print "="*80

    c = Column([c1, c2])
    print c

    print "="*80

    c2 = Column([c, r])
    print c2

    print "="*80

    r2 = Row([c, r])
    print r2
