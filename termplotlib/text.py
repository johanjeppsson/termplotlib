import numpy as np

from termplotlib.canvas import Canvas
from termplotlib.colors import fg, bg, st

class TextCanvas(Canvas):

    def __init__(self, text=None, color=None, background=None):
        super(Canvas, self).__init__()

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

    def get_rows(self, width=None, height=None, alignment='center'):
        width, height = self._check_dimensions(width, height)
        padding = self.get_padding(width, height, alignment)
        above = np.ceil(padding[0,0] / 4.0).astype(int)
        below = np.floor(padding[0,1] / 4.0).astype(int)
        before = np.floor(padding[1,0] / 2.0).astype(int)
        after = np.ceil(padding[1,1] / 2.0).astype(int)
        c_width = np.ceil(width / 2.0).astype(int)

        lines_out = []

        lines_out.extend([self._color_line(' ' * c_width) for i in range(above)])
        for line in self._lines:
            lines_out.append(self._color_line(' ' * before + line + ' ' * after))
        lines_out.extend([self._color_line(' ' * c_width) for i in range(below)])

        return lines_out

if __name__ == '__main__':

    t = TextCanvas('This is a text canvas', color='orange', background='navy')

    for row in t.get_rows(80, 30):
        print row
