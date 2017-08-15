import numpy as np

class Canvas(object):
    """Super class to all canvas objects."""

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
    def __init__(self, width=1, height=1, stretchable=True, alignment='center'):
        """ Create a canvas.

        :param int width: The width of the canvas in dots. There are two dots per character.
        :param int height: The height of the canvas in dots. There are four dots per charachter.
        :param bool stretchable: If the canvas is allowed to be strethed or not when configuring the alignment of multiple canvases.
        :param string alignment: The alignment of the canvas when stretched.
        """
        self.width = width
        self.height = height
        self.stretchable = stretchable
        self.alignment = alignment

    @property
    def c_width(self):
        """Width in characters."""
        return self._to_c_width(self.width)

    @property
    def c_height(self):
        """Height in characters."""
        return self._to_c_height(self.height)

    def _to_c_width(self, width):
        """Convert width in dots to width in characters."""
        return np.ceil(width / 2.0).astype(int)

    def _to_c_height(self, height):
        """Convert height in dots to height in characters."""
        return np.ceil(height / 4.0).astype(int)

    @property
    def alignment(self):
        return self._alignment

    @alignment.setter
    def alignment(self, alignment):
        if alignment not in self._alignments:
            raise ValueError('Invalid alignment "{}"'.format(alignment))
        self._alignment = alignment

    def get_rows(self, width=None, height=None):
        raise NotImplementedError('"get_rows" should be implemented by subclass!')

    def to_unicode(self, width=None, height=None):
        rows = self.get_rows(width, height)
        return '\n'.join(rows).encode('utf-8')

    def __str__(self):
        return self.to_unicode()

    def _check_dimensions(self, width, height):
        if width is None:
            width = self.width
        if height is None:
            height = self.height

        if not self.stretchable:
            return self.width, self.height

        assert width >= self.width and height >= self.height
        return width, height

    def get_padding(self, new_width, new_height):
        assert new_width >= self.width and new_height >= self.height
        if not self.stretchable:
            return np.zeros((2,2), dtype=int)

        # Calculate padding based on the chosen alignment.
        padding = self._alignments[self.alignment].copy()
        padding[0,:] *= new_height - self.height
        padding[1,:] *= new_width - self.width

        # Make sure that we have integer padding, and that
        # the total padding results in the correct width/height.
        padding[0,0] = np.ceil(padding[0,0])
        padding[0,1] = np.floor(padding[0,1])
        padding[1,0] = np.ceil(padding[1,0])
        padding[1,1] = np.floor(padding[1,1])

        return padding.astype(int)
