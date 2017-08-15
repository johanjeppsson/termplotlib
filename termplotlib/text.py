import numpy as np

from termplotlib.canvas import Canvas
from termplotlib.colors import fg, bg, st

class TextCanvas(Canvas):

    def __init__(self, width=1, height=1, stretchable=True, alignment='center', text=None, color=None, background=None):
        super(TextCanvas, self).__init__(width, height, stretchable, alignment)

        if text is not None:
            self.text = text
        else:
            self.text = ''

        self.color = color
        self.background = background

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        setattr(self, '_text', text)
        self._lines = text.split('\n')

        self.width = max(map(len, self._lines)) * 2
        self.height = len(self._lines) * 4

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

    def get_rows(self, width=None, height=None):
        width, height = self._check_dimensions(width, height)
        padding = self.get_padding(width, height)
        pad_above = np.ceil(padding[0,0] / 4.0).astype(int)
        pad_below = np.floor(padding[0,1] / 4.0).astype(int)
        pad_before = np.floor(padding[1,0] / 2.0).astype(int)
        pad_after = np.ceil(padding[1,1] / 2.0).astype(int)
        c_width = self._to_c_width(width)
        c_height = self._to_c_height(height)
        empty_lines = c_height - len(self._lines) - (pad_above + pad_below)

        lines_out = []

        lines_out.extend([self._color_line(' ' * c_width) for i in range(pad_above + empty_lines)])
        for line in self._lines:
            line_pad = c_width - (len(line) + pad_before + pad_after)
            lines_out.append(self._color_line(' ' * pad_before + line + ' ' * (pad_after + line_pad)))
        lines_out.extend([self._color_line(' ' * c_width) for i in range(pad_below)])

        return lines_out

class TextBox(TextCanvas):

    def __init__(self, width=1, height=1, stretchable=True, alignment='center', text=None, color=None, background=None, border_color=None, border_style='solid'):
        super(TextBox, self).__init__(width, height, stretchable, alignment, text, color, background)
        self.border_color = border_color
        self.border_style = border_style

    _box_chars = {'solid': {'ul': unichr(0x250c),
                            'ur': unichr(0x2510),
                            'll': unichr(0x2514),
                            'lr': unichr(0x2518),
                            'h' : unichr(0x2500),
                            'v' : unichr(0x2502)},
                  'bold':  {'ul': unichr(0x250f),
                            'ur': unichr(0x2513),
                            'll': unichr(0x2517),
                            'lr': unichr(0x251b),
                            'h' : unichr(0x2501),
                            'v' : unichr(0x2503)},
                  'double': {'ul': unichr(0x2554),
                             'ur': unichr(0x2557),
                             'll': unichr(0x255a),
                             'lr': unichr(0x255d),
                             'h' : unichr(0x2550),
                             'v' : unichr(0x2551)},
                  'dashed': {'ul': unichr(0x250c),
                             'ur': unichr(0x2510),
                             'll': unichr(0x2514),
                             'lr': unichr(0x2518),
                             'h' : unichr(0x254c),
                             'v' : unichr(0x254e)}}


    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        setattr(self, '_text', text)
        self._lines = text.split('\n')

        self.width = (max(map(len, self._lines)) + 2) * 2
        self.height = (len(self._lines) + 2) * 4

    @property
    def border_color(self):
        return self._b_fg

    @border_color.setter
    def border_color(self, color):
        self._b_fg = fg[color] if color else self.color

    @property
    def border_style(self):
        return self._b_st

    @border_style.setter
    def border_style(self, style):
        if style in self._box_chars:
            self._b_st = style
            self._box = self._box_chars[style]
        else:
            raise ValueError('Invalid box style: {}'.format(style))

    def get_rows(self, width=None, height=None):
        width, height = self._check_dimensions(width, height)
        padding = self.get_padding(width, height)
        pad_above = max(np.ceil(padding[0,0] / 4.0).astype(int), 0)
        pad_below = max(np.floor(padding[0,1] / 4.0).astype(int), 0)
        pad_before = max(np.floor(padding[1,0] / 2.0).astype(int) - 1, 0)
        pad_after = max(np.ceil(padding[1,1] / 2.0).astype(int) - 1, 0)
        c_width = self._to_c_width(width)
        c_height = self._to_c_height(height)
        empty_lines = c_height - len(self._lines) - (pad_above + pad_below) - 2

        lines_out = []
        lines_out.append(self._b_fg + self._bg + self._box['ul'] +
                         self._box['h'] * (c_width - 2) +
                         self._box['ur'] + st.RESET_ALL)
        pad_line = self._b_fg + self._bg + self._box['v'] + \
                   ' ' * (c_width - 2) + \
                   self._box['v'] + st.RESET_ALL
        lines_out.extend([pad_line] * (pad_above + empty_lines))

        for line in self._lines:
            line_pad = (c_width - 2) - (len(line) + pad_before + pad_after)
            lines_out.append(self._b_fg + self._bg + self._box['v'] +
                             self._fg + ' ' * pad_before +
                             line +
                             ' ' * (pad_after + line_pad) +
                             self._b_fg + self._box['v'] + st.RESET_ALL)
        lines_out.extend([pad_line] * pad_below)
        lines_out.append(self._b_fg + self._bg + self._box['ll'] +
                         self._box['h'] * (c_width - 2) +
                         self._box['lr'] + st.RESET_ALL)

        return lines_out

if __name__ == '__main__':

    t = TextCanvas(text='This is a text canvas\nWith multiple lines', color='orange', background='navy')
    print t.to_unicode(80, 32)

    bt = TextBox(text='This is a\n textbox', color='red', background='black', border_color='orange', border_style='dashed'
)
    print bt.to_unicode(80, 32)
