from PIL import Image

from patches import *
from display import *
from img_utils import *
from colour import Color
import numpy as np



img = Image.open('images/jiggly.png')
img = img.convert("RGB")
np_img = np.asarray(img) / 255
patch = Patch(np_img)

bg_img = Image.open('images/9.png')
bg_img = bg_img.convert("RGB")
npbg_img = np.asarray(bg_img) / 255

display = Display(npbg_img)

corners = [(60, 10), (20, 20), (50, 90), (100, 95)]
corners = [(y, x) for (x, y) in corners]
patch.recalculate_overlay(corners)
overlay = patch.overlay_patch
show_and_wait(overlay)

display.add_patch(patch)



patch.set_saturation(-0.5)
show_and_wait(display.get_display())

patch.set_saturation(0.5)
show_and_wait(display.get_display())

patch.set_hue(0.2)
show_and_wait(display.get_display())

patch.reset_color()
show_and_wait(display.get_display())


