from PIL import Image
import sys
import os

try:
    print('converting...')
    img = None
    i = 0
    j = 0
    for root, dirs, files in os.walk("."):
        for filename in files:
            if filename.endswith(".jpg"):
                img = Image.open(filename).convert("RGB")
                img.save(filename.replace("jpg", "png"), "png")
                i+=1
            elif filename.endswith('.png'):
                img = Image.open(filename).convert("RGB")
                img.save(filename.replace('png', 'jpg'), 'jpeg')
                j+=1
            else:
                continue
    print(f"Converting {i} image(s) from jpg to png")
    print(f"Converting {j} image(s) from png to jpeg")
except IOError:
    print('directroy empty!')
    sys.exit()