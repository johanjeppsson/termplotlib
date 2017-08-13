import numpy as np

from termplotlib.canvas import Canvas
from termplotlib.colors import fg, bg, st

class Line(Canvas):
    def __init__(self, color=None, background=None):
        super(Canvas, self).__init__()

        self.color = color
        self.background = background

    @property
    def color(self):
        return self._fg

    @color.setter
    def color(self, color):
        self._fg = fg[color] if color else ''

    @property
    def background(self):
        return self._fg

    @background.setter
    def background(self, background):
        self._bg = bg[background] if background else ''

    def _color_line(self, line):
        return self._fg + self._bg + line + st.RESET_ALL

class HorizontalLine(Line):

    _line_char = unichr(0x2500)

    def get_rows(self, width=None, height=None, alignment='center'):
        pad_above = np.ceil((height - 4)/(2 * 4.0)).astype(int)
        pad_below = np.floor((height - 4)/(2 * 4.0)).astype(int)
        c_width = np.ceil(width / 2.0).astype(int)

        lines_out = []

        lines_out.extend([self._color_line(' ' * c_width) for i in range(pad_above)])
        lines_out.append(self._color_line(self._line_char * c_width))
        lines_out.extend([self._color_line(' ' * c_width) for i in range(pad_below)])

        return lines_out

class VerticalLine(Line):

    _line_char = unichr(0x2502)

    def get_rows(self, width=None, height=None, alignment='center'):
        pad_before = np.ceil((width - 2)/(2 * 2.0)).astype(int)
        pad_after = np.floor((width - 2)/(2 * 2.0)).astype(int)
        c_height = np.ceil(height / 4.0).astype(int)

        line = self._color_line(' ' * pad_before + self._line_char + ' ' * pad_after)
        return [line] * c_height


if __name__ == '__main__':

    hl = HorizontalLine(color='orange', background='navy')

    print hl.to_unicode(80, 30)

    vl = VerticalLine(color='orange', background='navy')
    print vl.to_unicode(80, 30)

