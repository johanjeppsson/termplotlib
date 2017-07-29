import numpy as np
from raster import Cell, Canvas

LETTERS = {
    'A' : np.array([[1, 0, 1, 0],
                    [1, 0, 1, 0],
                    [1, 1, 1, 0],
                    [1, 0, 1, 0],
                    [0, 1, 0, 0]], dtype=bool),
    'B' : np.array([[1, 1, 0, 0],
                    [1, 0, 1, 0],
                    [1, 1, 0, 0],
                    [1, 0, 1, 0],
                    [1, 1, 0, 0]], dtype=bool),
    'C' : np.array([[0, 1, 1, 0],
                    [1, 0, 0, 0],
                    [1, 0, 0, 0],
                    [1, 0, 0, 0],
                    [0, 1, 1, 0]], dtype=bool),
    'D' : np.array([[1, 1, 0, 0],
                    [1, 0, 1, 0],
                    [1, 0, 1, 0],
                    [1, 0, 1, 0],
                    [1, 1, 0, 0]], dtype=bool),
    'F' : np.array([[1, 0, 0, 0],
                    [1, 0, 0, 0],
                    [1, 1, 0, 0],
                    [1, 0, 0, 0],
                    [1, 1, 1, 0]], dtype=bool),
    'E' : np.array([[1, 1, 1, 0],
                    [1, 0, 0, 0],
                    [1, 1, 0, 0],
                    [1, 0, 0, 0],
                    [1, 1, 1, 0]], dtype=bool),
    'G' : np.array([[0, 1, 1, 0],
                    [1, 0, 1, 0],
                    [1, 0, 1, 0],
                    [1, 0, 0, 0],
                    [0, 1, 1, 0]], dtype=bool),

}

class Letter(Canvas):
    def __init__(self, char):
        pattern = LETTERS[char]
        h, w = pattern.shape
        super(Letter, self).__init__(h, w, pattern=pattern)

class Text(Canvas):
    def __init__(self, text):
        w = 0
        h = 0
        for c in text:
            l_h, l_w = LETTERS[c].shape
            w += l_w
            h = max(h, l_h)
        pattern = np.zeros((h, w), dtype=bool)
        i = 0
        for c in text:
            l_h, l_w = LETTERS[c].shape
            pattern[:, i:i+l_w] = LETTERS[c].copy()
            i += l_w
        super(Text, self).__init__(w, h, pattern)

if __name__ == '__main__':
    print Text('ABCDEFG')

