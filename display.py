import numpy as np
from patches import *

class Display:
    # @param{np.array[float[0,1]]} img: dimension h x w x 3
    def __init__(self, background):
        self.components = [Patch(background)]
        self.height = background.shape[0]
        self.width = background.shape[1]

    def get_display(self):
        display = np.zeros((self.height, self.width, 3), dtype=float)
        for comp in self.components:
            seen_overlay = comp.seen_overlay_patch
            for o_y in range(comp.overlay_height):
                for o_x in range(comp.overlay_width):
                    if (o_x, o_y) in comp.overlay_quad_points:
                        display[o_y + comp.overlay_y, o_x + comp.overlay_x] = seen_overlay[o_y, o_x]

        return display

    def add_patch(self, patch):
        self.components.append(patch)


