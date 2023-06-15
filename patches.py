import numpy as np

from transformation_utils import *
from math_utils import *
from img_utils import *
from color import *


class Patch:
    # @param{np.array[float[0,1]]} base_patch: dimension h x w x 3
    def __init__(self, base_patch, x_init=0, y_init=0):
        self.base_patch = base_patch
        self.base_height = base_patch.shape[0]
        self.base_width = base_patch.shape[1]

        self.overlay_patch = base_patch
        self.overlay_height = base_patch.shape[0]
        self.overlay_width = base_patch.shape[1]
        self.overlay_x, self.overlay_y = x_init, y_init
        self.overlay_quad_points = {(x, y) for x in range(base_patch.shape[1]) for y in range(base_patch.shape[0])}

        self.seen_overlay_patch = base_patch

        self.color_transformer = ColorTransformer()

    # @param{list[int * int]} corners: [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
    def recalculate_overlay(self, corners):
        xmin, xmax, ymin, ymax = get_bounds(corners)

        overlay_height = ymax - ymin + 1
        overlay_width = xmax - xmin + 1

        overlay = np.zeros((overlay_height, overlay_width, 3), dtype=float)
        overlay_corners = [(x - xmin, y - ymin) for (x, y) in corners]
        overlay_patch_quad = Polygon(overlay_corners)
        overlay_quad_points = set()

        for y in range(overlay_height):
            for x in range(overlay_width):
                pixel = Point(x, y)
                if pixel.within(overlay_patch_quad):
                    overlay_quad_points.add((x, y))
                    patch_x, patch_y = find_patch_point((self.base_height, self.base_width), overlay_corners, (x, y))
                    overlay[y, x] = self.base_patch[patch_y, patch_x]

        self.overlay_patch = overlay
        self.overlay_height = overlay_height
        self.overlay_width = overlay_width
        self.overlay_x = xmin
        self.overlay_y = ymin
        self.overlay_quad_points = overlay_quad_points

        self.recalculate_seen_overlay()

    def set_luminance(self, luminance):
        self.color_transformer.set_luminance(luminance)
        self.recalculate_seen_overlay()

    def set_saturation(self, saturation):
        self.color_transformer.set_saturation(saturation)
        self.recalculate_seen_overlay()

    def set_hue(self, hue):
        self.color_transformer.set_hue(hue)
        self.recalculate_seen_overlay()

    def reset_color(self):
        self.color_transformer.reset()
        self.recalculate_seen_overlay()

    def transform_color(self, color):
        return self.color_transformer.transform_color(color)

    def recalculate_seen_overlay(self):
        seen_overlay = np.copy(self.overlay_patch)
        for y in range(self.overlay_height):
            for x in range(self.overlay_width):
                seen_overlay[y, x] = self.transform_color(self.overlay_patch[y, x])
        self.seen_overlay_patch = seen_overlay





