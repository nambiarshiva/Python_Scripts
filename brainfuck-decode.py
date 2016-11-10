from PIL import Image
from pybrainfuck import BrainFck


# Read image and get pixel data as list
pixels = list(Image.open('brainfun.png').getdata())

# Extract just get the blocks. Fun fact: PIL's resize with PIL.Image.NEAREST
# for nearest neighbor messes with the values, but mtPaint does it correctly.
pixels = [pixels[r*512 + c] \
		for r in range(0, 512, 16) \
		for c in range(0, 512, 16)]

# Sort the pixels by RGB value
pixels.sort(key=lambda p: (p[0]<<8) + (p[1]<<4) + p[2])

# Run the alpha values as Brainfuck
BrainFck().run(u"".join([chr(p[3]) for p in pixels]))
