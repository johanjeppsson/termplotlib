

class Canvas(object):
    """Super class to all canvas objects."""

    def get_rows(self, width=None, height=None, alignment='center'):
        raise NotImplementedError('"get_rows" should be implemented by subclass!')

    def _to_unicode(self):
        rows = self.get_rows()
        return '\n'.join(reversed(rows)).encode('utf-8')

    def __str__(self):
        return self._to_unicode()

    def _check_dimensions(self, width, height):
        if width is None:
            width = self.width
        if height is None:
            height = self.height
        assert width >= self.width and height >= self.height
        return width, height
