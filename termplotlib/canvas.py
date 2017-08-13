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

    def get_rows(self, width=None, height=None, alignment='center'):
        raise NotImplementedError('"get_rows" should be implemented by subclass!')

    def to_unicode(self, width=None, height=None, alignment='center'):
        rows = self.get_rows(width, height, alignment)
        return '\n'.join(rows).encode('utf-8')

    def __str__(self):
        return self.to_unicode()

    def _check_dimensions(self, width, height):
        if width is None:
            width = self.width
        if height is None:
            height = self.height
        assert width >= self.width and height >= self.height
        return width, height

    def get_padding(self, new_width, new_height, alignment='center'):
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
