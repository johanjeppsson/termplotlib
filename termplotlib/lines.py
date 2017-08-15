import numpy as np

from termplotlib.canvas import Canvas
from termplotlib.colors import fg, bg, st

class Line(Canvas):
    def __init__(self, width=1, height=1, stretchable=True, alignment='center', color=None, background=None, style='solid'):
        super(Line, self).__init__(width, height, stretchable, alignment)

        self.width = width
        self.height = height
        self.color = color
        self.background = background
        self.style = style

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

    @property
    def style(self):
        return self._style

    @style.setter
    def style(self, style):
        if style not in self._line_chars:
            raise ValueError('Invalid style "{}"'.format(style))
        self._style = style
        self._line_char = self._line_chars[style]

    def _color_line(self, line):
        return self._fg + self._bg + line + st.RESET_ALL

    def _get_line_char(self, row, col, n_rows, n_cols):
        raise NotImplementedError('_do_line should be implemented by subclass.')

class HorizontalLine(Line):

    _line_chars = {'solid':  unichr(0x2500),
                   'bold' :  unichr(0x2501),
                   'double': unichr(0x2550),
                   'dashed': unichr(0x254c)}

    def _get_line_char(self, row, col, n_rows, n_cols):
        return self._line_char

    def get_rows(self, width=None, height=None, alignment='center'):
        width, height = self._check_dimensions(width, height)
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

    _line_chars = {'solid': unichr(0x2502),
                   'bold' : unichr(0x2503),
                   'double': unichr(0x2551),
                   'dashed': unichr(0x254e)}

    def _get_line_char(self, row, col, n_rows, n_cols):
        return self._line_char

    def get_rows(self, width=None, height=None, alignment='center'):
        width, height = self._check_dimensions(width, height)
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

    directions = ['left', 'right', 'both']

    def __init__(self, *args, **kwargs):
        self.direction = kwargs.pop('direction', 'right')
        super(HorizontalLine, self).__init__(*args, **kwargs)

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, direction):
        if direction not in self.directions:
            raise ValueError('Invalid direction "{}"'.format(direction))
        self._direction = direction

    def _get_line_char(self, row, col, n_rows, n_cols):
        if col == 0 and self.direction in ['left', 'both']:
            return self._arrow_left
        elif col == n_cols - 1 and self.direction in ['right', 'both']:
            return self._arrow_right
        else:
            return self._line_char

class VerticalArrow(VerticalLine):

    _arrow_up = unichr(0x25B4)
    _arrow_down = unichr(0x25be)

    directions = ['up', 'down', 'both']

    def __init__(self, *args, **kwargs):
        self.direction = kwargs.pop('direction', 'up')
        super(VerticalLine, self).__init__(*args, **kwargs)

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, direction):
        if direction not in self.directions:
            raise ValueError('Invalid direction "{}"'.format(direction))
        self._direction = direction

    def _get_line_char(self, row, col, n_rows, n_cols):
        if row == 0 and self.direction in ['up', 'both']:
            return self._arrow_up
        elif row == n_rows - 1 and self.direction in ['down', 'both']:
            return self._arrow_down
        else:
            return self._line_char

if __name__ == '__main__':
    from termplotlib.layout import Row, Column
    from termplotlib.text import TextBox
    for sty in ['solid', 'bold', 'double', 'dashed']:
        hl = HorizontalLine(width=20, height=20, color='orange', background='navy', style=sty)
        vl = VerticalLine(width=20, height=20, color='orange', background='navy', style=sty)

        ha = HorizontalArrow(width=20, height=20, color='orange', background='navy', style=sty)

        va = VerticalArrow(width=20, height=20, color='orange', background='navy', style=sty)
        va.direction = 'both'

        row = Row([hl, vl, ha, va])
        tb = TextBox(text=sty, border_style=sty)
        col = Column([tb, row])
        print col.to_unicode(160, 80)


