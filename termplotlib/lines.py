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

    def _get_line_char(self, row, col, n_rows, n_cols):
        raise NotImplementedError('_do_line should be implemented by subclass.')

class HorizontalLine(Line):

    _line_char = unichr(0x2500)

    def _get_line_char(self, row, col, n_rows, n_cols):
        return self._line_char

    def get_rows(self, width=None, height=None, alignment='center'):
        pad_above = np.ceil((height - 4)/(2 * 4.0)).astype(int)
        pad_below = np.floor((height - 4)/(2 * 4.0)).astype(int)
        c_width = np.ceil(width / 2.0).astype(int)
        c_height = pad_above + pad_below + 1

        lines_out = []

        lines_out.extend([self._color_line(' ' * c_width) for i in range(pad_above)])
        line = ''.join([self._get_line_char(pad_above, i, c_height, c_width) for i in range(c_width)])
        lines_out.append(self._color_line(line))
        lines_out.extend([self._color_line(' ' * c_width) for i in range(pad_below)])

        return lines_out

class VerticalLine(Line):

    _line_char = unichr(0x2502)

    def _get_line_char(self, row, col, n_rows, n_cols):
        return self._line_char

    def get_rows(self, width=None, height=None, alignment='center'):
        pad_before = np.ceil((width - 2)/(2 * 2.0)).astype(int)
        pad_after = np.floor((width - 2)/(2 * 2.0)).astype(int)
        c_height = np.ceil(height / 4.0).astype(int)
        c_width = pad_before + pad_after + 1

        lines = [self._color_line(' ' * pad_before +
                                  self._get_line_char(i, pad_before, c_height, c_width) +
                                  ' ' * pad_after)
                 for i in range(c_height)]
        return lines

class HorizontalArrow(HorizontalLine):

    _arrow_right = unichr(0x25b8)
    _arrow_left = unichr(0x25c2)

    def _get_line_char(self, row, col, n_rows, n_cols):
        if col == 0:
            return self._arrow_left
        elif col == n_cols - 1:
            return self._arrow_right
        else:
            return self._line_char

class VerticalArrow(VerticalLine):

    _arrow_up = unichr(0x25B4)
    _arrow_down = unichr(0x25be)

    def _get_line_char(self, row, col, n_rows, n_cols):
        if row == 0:
            return self._arrow_up
        elif row == n_rows - 1:
            return self._arrow_down
        else:
            return self._line_char

if __name__ == '__main__':

    hl = HorizontalLine(color='orange', background='navy')

    print hl.to_unicode(80, 30)

    vl = VerticalLine(color='orange', background='navy')
    print vl.to_unicode(80, 30)

    ha = HorizontalArrow(color='orange', background='navy')
    print ha.to_unicode(80, 30)

    va = VerticalArrow(color='orange', background='navy')
    print va.to_unicode(80, 30)

