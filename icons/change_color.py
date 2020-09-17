from __future__ import unicode_literals, print_function, absolute_import
from PIL import Image

images = ["pencil.png", "lightbulb.png", "eighth_note.png", "treble_clef.png"]

for filename in images:
    print("Converting:", filename)
    img = Image.open(filename)
    img.convert("RGB")
    pixelSizeTuple = img.size
    print(pixelSizeTuple[0], 'x', pixelSizeTuple[1])
    if pixelSizeTuple[0] > 750:
        print("This may take a while.")
    img2 = Image.new('RGBA', img.size)

    for i in range(pixelSizeTuple[0]):
        for j in range(pixelSizeTuple[1]):
            pixel = img.getpixel((i, j))
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            if r == 255 and b == 255 and g == 255:
                img2.putpixel((i, j), (255, 255, 255, 0))
            else:
                img2.putpixel((i, j), (127, 127, 127, 255))

    img2.save(filename)
    print("Finished\n")
