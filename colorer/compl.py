# Module compl.py -- calculating contrast color to given color
import math

# A color is stored internally using sRGB (standard RGB) values in the range 0-1
Color = [0.0, 0.0, 0.0]
D65 = [0.95047, 1.00000, 1.08883]
def lab_finv(t):
    if t > 6.0/29.0:
        return t * t * t
    return 3.0 * 6.0 / 29.0 * 6.0 / 29.0 * (t - 4.0/29.0)

def LabToXyzWhiteRef(l, a, b, wref):
    l2 = (l + 0.16) / 1.16
    x = wref[0] * lab_finv(l2+a/5.0)
    y = wref[1] * lab_finv(l2)
    z = wref[2] * lab_finv(l2-b/2.0)
    return x, y, z

# XyzToLinearRgb converts from CIE XYZ-space to Linear RGB space.
def XyzToLinearRgb(x, y, z):
    r = 3.2404542*x - 1.5371385*y - 0.4985314*z
    g = -0.9692660*x + 1.8760108*y + 0.0415560*z
    b = 0.0556434*x - 0.2040259*y + 1.0572252*z
    return r, g, b

def delinearize(v):
    if v <= 0.0031308:
        return 12.92 * v
    return 1.055 * math.pow(v, 1.0/2.4) - 0.055

# LinearRgb creates an sRGB color out of the given linear RGB color
def LinearRgb(r, g, b):
    return delinearize(r), delinearize(g), delinearize(b)

def Xyz(x, y, z):
    x, y, z = XyzToLinearRgb(x, y, z)
    return LinearRgb(x, y, z)

# Generates a color by using data given in CIE L*a*b* space, taking
# into account a given reference white. (i.e. the monitor's white)
def LabWhiteRef(l, a, b, wref):
    x, y, z = LabToXyzWhiteRef(l, a, b, wref)
    return Xyz(x, y, z)

def HclToLab(h, c, l):
    H = 0.01745329251994329576 * h # Deg2Rad
    a = c * math.cos(H)
    b = c * math.sin(H)
    L = l
    return L, a, b

# Generates a color by using data given in HCL space, taking
# into account a given reference white. (i.e. the monitor's white)
# H values are in [0..360], C and L values are in [0..1]
def HclWhiteRef(h, c, l, wref):
    L, a, b = HclToLab(h, c, l)
    return LabWhiteRef(L, a, b, wref)

# Generates a color by using data given in HCL space using D65 as reference white.
# H values are in [0..360], C and L values are in [0..1]
# WARNING: many combinations of `l`, `a`, and `b` values do not have corresponding
#          valid RGB values, check the FAQ in the README if you're unsure.
def Hcl(h, c, l):
    return HclWhiteRef(h, c, l, D65)

# Implement the Color interface.
def RGBA(col):
    r = col[0]*65535.0 + 0.5
    g = col[1]*65535.0 + 0.5
    b = col[2]*65535.0 + 0.5
    a = 0xFFFF
    return r, g, b, a

# Constructs a colorful.Color from something implementing color.Color
def MakeColor(col):
    r, g, b, a = RGBA(col)
    if a == 0:
        return Color
    # Since color.Color is alpha pre-multiplied, we need to divide the
    # RGB values by alpha again in order to get back the original RGB.
    r *= 0xffff
    r /= a
    g *= 0xffff
    g /= a
    b *= 0xffff
    b /= a

    return [float(r) / 65535.0, float(g) / 65535.0, float(b) / 65535.0]

# Contrast returns the color with the most contrast (hence either black or white)
def contrast(c):
    col = MakeColor(hex_to_srgb(c))
    wf = [1, 1, 1]
    bf = [0, 0, 0]

    a, b, l = Hcl(col[0], col[1], col[2])
    if l < 0.5:
        return rgb_to_hex(srgb_to_rgb(wf))

    return rgb_to_hex(srgb_to_rgb(bf))

def hex_to_srgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return list(int(value[i:i + lv // 3], 16)/255. for i in range(0, lv, lv // 3))

def srgb_to_rgb(value):
    lv = len(value)
    return tuple(int(value[i]*255) for i in range(0, lv))

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

def hex_to_rgba(value, a):
    value = value.lstrip('#')
    lv = len(value)
    li = list(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
    return 'rgba({}, {}, {}, {})'.format(li[0], li[1], li[2], a)