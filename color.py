from colour import Color
import numpy as np

class ColorTransformer:
    def __init__(self, dluminance=0, dsaturation=0, dhue=0):
        self.dluminance = dluminance
        self.dsaturation = dsaturation
        self.dhue = dhue

    # @param{list[float[0,1]} color: [r, g, b]
    def transform_color(self, color):
        c = Color(rgb=color)
        c.luminance = np.clip(c.luminance + self.dluminance, 0, 1)
        c.saturation = np.clip(c.saturation + self.dsaturation, 0, 1)
        c.hue = np.clip(c.hue + self.dhue, 0, 1)
        return np.array(c.rgb)

    def set_luminance(self, luminance):
        self.dluminance = luminance

    def set_saturation(self, saturation):
        self.dsaturation = saturation

    def set_hue(self, hue):
        self.dhue = hue

    def reset(self):
        self.dluminance = 0
        self.dsaturation = 0
        self.dhue = 0