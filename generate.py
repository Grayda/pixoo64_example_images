# This file generates the source images that you can upload to Divoom to retrieve the binary files

from PIL import Image, ImageOps

images = [
    {
        "size": 64,
        "colours": [(255, 0, 0)],
        "filename": "red64.png"
    },
    {
        "size": 32,
        "colours": [(0, 255, 0)],
        "filename": "green32.png"
    },
    {
        "size": 16,
        "colours": [(0, 0, 255)],
        "filename": "blue16.png"
    },
    {
        "size": 16,
        "colours": [(255, 255, 0)],
        "filename": "yellow16.png"
    },
    {
        "size": 64,
        "colours": [(0, 0, 0), (255, 255, 255)] * 32 + [(255, 255, 255), (0, 0, 0)] * 32,
        "filename": "checkerboard64.png"
    }, {
        "size": 128,
        "colours": [(255, 255, 255)],
        "filename": "white128.png"
    }, {
        "size": 128,
        "colours": [(255, 0, 255)],
        "filename": "magenta128.png"
    },
    {
        "size": 128,
        "colours": [(255, 0, 0), (255, 255, 0), (255, 255, 255), (0, 255, 255), (0, 0, 255), (0, 0, 0), (0, 255, 0), (255, 0, 255)],
        "filename": "rainbow128.png"
    }
]

for image in images:
    # Create a new image
    img = Image.new("RGB", (image["size"], image["size"]))

    # The pixels to save to the image. The result will look something like this for an alternating black / white image: [255, 255, 255, 0, 0, 0, 255, 255, 255 ...]
    pixels = []

    # Loop through all the pixels in the image
    for n in range(int(image["size"] * image["size"] / len(image["colours"]))):
        # Loop through all the colours
        for colour in image["colours"]:
            pixels.append(colour)

    img.putdata(pixels)

    img.save("images/{i}".format(i=image["filename"]))
