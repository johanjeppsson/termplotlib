"""
Convenience functions for colors in terminals
"""

CSI = '\033['
OSC = '\033]'

# Some convenience names for common colors that are outside.
EXTRA_NAMES = {'ORANGE'            : 208,
               'PINK'              : 218,
               'PURPLE'            : 55,
               'GREY'              : 239,
}

# Standard Xterm names
XTERM_NAMES = {'MAROON'            : 1,
               'OLIVE'             : 3,
               'NAVY'              : 4,
               'TEAL'              : 6,
               'SILVER'            : 7,
               'GREY'              : 8,
               'LIME'              : 10,
               'FUCHSIA'           : 13,
               'AQUA'              : 14,
               'GREY0'             : 16,
               'NAVYBLUE'          : 17,
               'DARKBLUE'          : 18,
               'BLUE3'             : 19,
               'BLUE3'             : 20,
               'BLUE1'             : 21,
               'DARKGREEN'         : 22,
               'DEEPSKYBLUE4'      : 23,
               'DEEPSKYBLUE4'      : 24,
               'DEEPSKYBLUE4'      : 25,
               'DODGERBLUE3'       : 26,
               'DODGERBLUE2'       : 27,
               'GREEN4'            : 28,
               'SPRINGGREEN4'      : 29,
               'TURQUOISE4'        : 30,
               'DEEPSKYBLUE3'      : 31,
               'DEEPSKYBLUE3'      : 32,
               'DODGERBLUE1'       : 33,
               'GREEN3'            : 34,
               'SPRINGGREEN3'      : 35,
               'DARKCYAN'          : 36,
               'LIGHTSEAGREEN'     : 37,
               'DEEPSKYBLUE2'      : 38,
               'DEEPSKYBLUE1'      : 39,
               'GREEN3'            : 40,
               'SPRINGGREEN3'      : 41,
               'SPRINGGREEN2'      : 42,
               'CYAN3'             : 43,
               'DARKTURQUOISE'     : 44,
               'TURQUOISE2'        : 45,
               'GREEN1'            : 46,
               'SPRINGGREEN2'      : 47,
               'SPRINGGREEN1'      : 48,
               'MEDIUMSPRINGGREEN' : 49,
               'CYAN2'             : 50,
               'CYAN1'             : 51,
               'DARKRED'           : 52,
               'DEEPPINK4'         : 53,
               'PURPLE4'           : 54,
               'PURPLE4'           : 55,
               'PURPLE3'           : 56,
               'BLUEVIOLET'        : 57,
               'ORANGE4'           : 58,
               'GREY37'            : 59,
               'MEDIUMPURPLE4'     : 60,
               'SLATEBLUE3'        : 61,
               'SLATEBLUE3'        : 62,
               'ROYALBLUE1'        : 63,
               'CHARTREUSE4'       : 64,
               'DARKSEAGREEN4'     : 65,
               'PALETURQUOISE4'    : 66,
               'STEELBLUE'         : 67,
               'STEELBLUE3'        : 68,
               'CORNFLOWERBLUE'    : 69,
               'CHARTREUSE3'       : 70,
               'DARKSEAGREEN4'     : 71,
               'CADETBLUE'         : 72,
               'CADETBLUE'         : 73,
               'SKYBLUE3'          : 74,
               'STEELBLUE1'        : 75,
               'CHARTREUSE3'       : 76,
               'PALEGREEN3'        : 77,
               'SEAGREEN3'         : 78,
               'AQUAMARINE3'       : 79,
               'MEDIUMTURQUOISE'   : 80,
               'STEELBLUE1'        : 81,
               'CHARTREUSE2'       : 82,
               'SEAGREEN2'         : 83,
               'SEAGREEN1'         : 84,
               'SEAGREEN1'         : 85,
               'AQUAMARINE1'       : 86,
               'DARKSLATEGRAY2'    : 87,
               'DARKRED'           : 88,
               'DEEPPINK4'         : 89,
               'DARKMAGENTA'       : 90,
               'DARKMAGENTA'       : 91,
               'DARKVIOLET'        : 92,
               'PURPLE'            : 93,
               'ORANGE4'           : 94,
               'LIGHTPINK4'        : 95,
               'PLUM4'             : 96,
               'MEDIUMPURPLE3'     : 97,
               'MEDIUMPURPLE3'     : 98,
               'SLATEBLUE1'        : 99,
               'YELLOW4'           : 100,
               'WHEAT4'            : 101,
               'GREY53'            : 102,
               'LIGHTSLATEGREY'    : 103,
               'MEDIUMPURPLE'      : 104,
               'LIGHTSLATEBLUE'    : 105,
               'YELLOW4'           : 106,
               'DARKOLIVEGREEN3'   : 107,
               'DARKSEAGREEN'      : 108,
               'LIGHTSKYBLUE3'     : 109,
               'LIGHTSKYBLUE3'     : 110,
               'SKYBLUE2'          : 111,
               'CHARTREUSE2'       : 112,
               'DARKOLIVEGREEN3'   : 113,
               'PALEGREEN3'        : 114,
               'DARKSEAGREEN3'     : 115,
               'DARKSLATEGRAY3'    : 116,
               'SKYBLUE1'          : 117,
               'CHARTREUSE1'       : 118,
               'LIGHTGREEN'        : 119,
               'LIGHTGREEN'        : 120,
               'PALEGREEN1'        : 121,
               'AQUAMARINE1'       : 122,
               'DARKSLATEGRAY1'    : 123,
               'RED3'              : 124,
               'DEEPPINK4'         : 125,
               'MEDIUMVIOLETRED'   : 126,
               'MAGENTA3'          : 127,
               'DARKVIOLET'        : 128,
               'PURPLE'            : 129,
               'DARKORANGE3'       : 130,
               'INDIANRED'         : 131,
               'HOTPINK3'          : 132,
               'MEDIUMORCHID3'     : 133,
               'MEDIUMORCHID'      : 134,
               'MEDIUMPURPLE2'     : 135,
               'DARKGOLDENROD'     : 136,
               'LIGHTSALMON3'      : 137,
               'ROSYBROWN'         : 138,
               'GREY63'            : 139,
               'MEDIUMPURPLE2'     : 140,
               'MEDIUMPURPLE1'     : 141,
               'GOLD3'             : 142,
               'DARKKHAKI'         : 143,
               'NAVAJOWHITE3'      : 144,
               'GREY69'            : 145,
               'LIGHTSTEELBLUE3'   : 146,
               'LIGHTSTEELBLUE'    : 147,
               'YELLOW3'           : 148,
               'DARKOLIVEGREEN3'   : 149,
               'DARKSEAGREEN3'     : 150,
               'DARKSEAGREEN2'     : 151,
               'LIGHTCYAN3'        : 152,
               'LIGHTSKYBLUE1'     : 153,
               'GREENYELLOW'       : 154,
               'DARKOLIVEGREEN2'   : 155,
               'PALEGREEN1'        : 156,
               'DARKSEAGREEN2'     : 157,
               'DARKSEAGREEN1'     : 158,
               'PALETURQUOISE1'    : 159,
               'RED3'              : 160,
               'DEEPPINK3'         : 161,
               'DEEPPINK3'         : 162,
               'MAGENTA3'          : 163,
               'MAGENTA3'          : 164,
               'MAGENTA2'          : 165,
               'DARKORANGE3'       : 166,
               'INDIANRED'         : 167,
               'HOTPINK3'          : 168,
               'HOTPINK2'          : 169,
               'ORCHID'            : 170,
               'MEDIUMORCHID1'     : 171,
               'ORANGE3'           : 172,
               'LIGHTSALMON3'      : 173,
               'LIGHTPINK3'        : 174,
               'PINK3'             : 175,
               'PLUM3'             : 176,
               'VIOLET'            : 177,
               'GOLD3'             : 178,
               'LIGHTGOLDENROD3'   : 179,
               'TAN'               : 180,
               'MISTYROSE3'        : 181,
               'THISTLE3'          : 182,
               'PLUM2'             : 183,
               'YELLOW3'           : 184,
               'KHAKI3'            : 185,
               'LIGHTGOLDENROD2'   : 186,
               'LIGHTYELLOW3'      : 187,
               'GREY84'            : 188,
               'LIGHTSTEELBLUE1'   : 189,
               'YELLOW2'           : 190,
               'DARKOLIVEGREEN1'   : 191,
               'DARKOLIVEGREEN1'   : 192,
               'DARKSEAGREEN1'     : 193,
               'HONEYDEW2'         : 194,
               'LIGHTCYAN1'        : 195,
               'RED1'              : 196,
               'DEEPPINK2'         : 197,
               'DEEPPINK1'         : 198,
               'DEEPPINK1'         : 199,
               'MAGENTA2'          : 200,
               'MAGENTA1'          : 201,
               'ORANGERED1'        : 202,
               'INDIANRED1'        : 203,
               'INDIANRED1'        : 204,
               'HOTPINK'           : 205,
               'HOTPINK'           : 206,
               'MEDIUMORCHID1'     : 207,
               'DARKORANGE'        : 208,
               'SALMON1'           : 209,
               'LIGHTCORAL'        : 210,
               'PALEVIOLETRED1'    : 211,
               'ORCHID2'           : 212,
               'ORCHID1'           : 213,
               'ORANGE1'           : 214,
               'SANDYBROWN'        : 215,
               'LIGHTSALMON1'      : 216,
               'LIGHTPINK1'        : 217,
               'PINK1'             : 218,
               'PLUM1'             : 219,
               'GOLD1'             : 220,
               'LIGHTGOLDENROD2'   : 221,
               'LIGHTGOLDENROD2'   : 222,
               'NAVAJOWHITE1'      : 223,
               'MISTYROSE1'        : 224,
               'THISTLE1'          : 225,
               'YELLOW1'           : 226,
               'LIGHTGOLDENROD1'   : 227,
               'KHAKI1'            : 228,
               'WHEAT1'            : 229,
               'CORNSILK1'         : 230,
               'GREY100'           : 231,
               'GREY3'             : 232,
               'GREY7'             : 233,
               'GREY11'            : 234,
               'GREY15'            : 235,
               'GREY19'            : 236,
               'GREY23'            : 237,
               'GREY27'            : 238,
               'GREY30'            : 239,
               'GREY35'            : 240,
               'GREY39'            : 241,
               'GREY42'            : 242,
               'GREY46'            : 243,
               'GREY50'            : 244,
               'GREY54'            : 245,
               'GREY58'            : 246,
               'GREY62'            : 247,
               'GREY66'            : 248,
               'GREY70'            : 249,
               'GREY74'            : 250,
               'GREY78'            : 251,
               'GREY82'            : 252,
               'GREY85'            : 253,
               'GREY89'            : 254,
               'GREY93'            : 255,
}


class AnsiCodes(object):

    def __init__(self):
        attrs = [n for n in dir(self) if not n.startswith('_')]
        for name in attrs:
            value = getattr(self, name)
            setattr(self, name, AnsiCodes.code_to_str(value))

        if hasattr(self, '_256_ESC'):
            for name, val in XTERM_NAMES.iteritems():
                code = list(self._256_ESC)
                code.append(val)
                setattr(self, name, AnsiCodes.code_to_str(code))
            for name, val in EXTRA_NAMES.iteritems():
                code = list(self._256_ESC)
                code.append(val)
                setattr(self, name, AnsiCodes.code_to_str(code))

        if hasattr(self, '_RGB_ESC'):
            setattr(self, 'RGB', self._RGB)

    @staticmethod
    def code_to_str(code):
        if type(code) == int:
            return CSI + str(code) + 'm'
        elif type(code) == list:
            return CSI + ';'.join(map(str, code)) + 'm'

    def _RGB(self, r, g, b):
        assert min([r, g, b]) >= 0 and max([r, g, b]) < 256
        code = list(self._RGB_ESC)
        code.extend([r, g, b])
        return AnsiCodes.code_to_str(code)

    def __getitem__(self, name):
        return getattr(self, name.upper())

class AnsiForeGround(AnsiCodes):
    BLACK           = 30
    RED             = 31
    GREEN           = 32
    YELLOW          = 33
    BLUE            = 34
    MAGENTA         = 35
    CYAN            = 36
    WHITE           = 37
    RESET           = 39

    # Outside standard, but works in most modern terminals
    LIGHT_BLACK   = 90
    LIGHT_RED     = 91
    LIGHT_GREEN   = 92
    LIGHT_YELLOW  = 93
    LIGHT_BLUE    = 94
    LIGHT_MAGENTA = 95
    LIGHT_CYAN    = 96
    LIGHT_WHITE   = 97

    _256_ESC = [38, 5]
    _RGB_ESC = [38, 2]

class AnsiBackGround(AnsiCodes):
    BLACK           = 40
    RED             = 41
    GREEN           = 42
    YELLOW          = 43
    BLUE            = 44
    MAGENTA         = 45
    CYAN            = 46
    WHITE           = 47
    RESET           = 49

    # Outside standard, but works in most modern terminals
    LIGHT_BLACK   = 100
    LIGHT_RED     = 101
    LIGHT_GREEN   = 102
    LIGHT_YELLOW  = 103
    LIGHT_BLUE    = 104
    LIGHT_MAGENTA = 105
    LIGHT_CYAN    = 106
    LIGHT_WHITE   = 107

    _256_ESC = [48, 5]
    _RGB_ESC = [48, 2]

class AnsiStyle(AnsiCodes):
    BRIGHT    = 1
    BOLD      = 1
    DIM       = 2
    ITALIC    = 3
    UNDERLINE = 4
    NORMAL    = 22
    INVERSE   = 7
    RESET_ALL = 0

fg = AnsiForeGround()
bg = AnsiBackGround()
st = AnsiStyle()

def color_str(s, fg=None, bg=None, styles=None):
    """Return a string with ANSI formatting codes."""
    s_out = ''
    if fg:
        try:
            if type(fg) == tuple:
                s_out += globals()['fg'].RGB(*fg)
            else:
                s_out += getattr(globals()['fg'], fg.upper())
        except AttributeError:
            raise AttributeError('No foreground color named {}'.format(fg))
    if bg:
        try:
            if type(bg) == tuple:
                s_out += globals()['bg'].RGB(*bg)
            else:
                s_out += getattr(globals()['bg'], bg.upper())
        except AttributeError:
            raise AttributeError('No background color named {}'.format(bg))

    if styles:
        if type(styles) == str:
            styles = [styles]
        try:
            for style in styles:
                s_out += getattr(st, style.upper())
        except AttributeError:
            raise AttributeError('No style named {}'.format(style))

    s_out += s
    s_out += st.RESET_ALL
    return s_out

def ycbcr2rgb(y, cB, cR):
    r = int(np.clip((1.0 * y    + 0        * cB    + 1.402 * cR) * 255, 0, 255))
    g = int(np.clip((1.0 * y    - 0.344136 * cB - 0.714136 * cR) * 255, 0, 255))
    b = int(np.clip((1.0 * y    + 1.772    * cB        + 0 * cR) * 255, 0, 255))
    return r, g, b

if __name__ == '__main__':
    import numpy as np
    s = ''
    max_len = 0
    width = 8

    for name, val in bg.__dict__.iteritems():
        if name.startswith('_') and name != 'RESET':
            continue
        max_len = max(max_len, len(name))

    print "Test standard colors:"

    n_colors = 0
    for i, (name, val) in enumerate(bg.__dict__.iteritems()):
        if name.startswith('_') or name in ['RESET', 'RGB', 'code_to_str'] or name in XTERM_NAMES:
            continue
        s += val + name.ljust(max_len) + bg.RESET
        n_colors += 1
        if n_colors % width == 0:
            s += '\n'
    print s + '\n' * 3

    print "Test xterm 256 colors:"
    s = ''
    n_colors = 0
    for i, (name, val) in enumerate(bg.__dict__.iteritems()):
        if name.startswith('_') or name in ['RESET', 'RGB', 'code_to_str'] or name not in XTERM_NAMES:
            continue
        s += val + name.ljust(max_len) + bg.RESET
        n_colors += 1
        if n_colors % width == 0:
            s += '\n'
    print s + '\n' * 3

    print "Test RGB colors"
    s = ''
    for cR in np.arange(1.0, -1.01, -0.05):
        for cB in np.arange(-1.0, 1.01, 0.05):
            r, g, b = ycbcr2rgb(0.5, cB, cR)
            s += bg.RGB(r, g, b) + '  '
        s += bg.RESET + '\n'
    print s

    # Some examples:
    print "Some examples"
    print color_str('Hello world', fg='red', bg='green', styles=['bold'])
    print color_str('Some RGB values', fg=(0, 128, 255), bg='pink', styles=['underline', 'italic'])
    print fg.ORANGE + "Manually " + bg.CYAN + "assembled " + fg.MAGENTA + "string" + st.RESET_ALL
    print fg['blue'] + "Manually " + bg['orange'] + "assembled " + fg.RGB(255, 0, 0) + "string" + st.RESET_ALL
