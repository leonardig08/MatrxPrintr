from PIL import Image


def matrixlink(link, name):
    wi = 8
    he = len(link)
    matr = Image.new(mode="1", size=(wi, he))
    vals = []
    for i in link:
        if ord(i) < 256:
            asciicode = str(bin(ord(i)))[2:]
            if len(asciicode) < 8:
                asciicode = ("0" * (8 - len(asciicode))) + asciicode
            vals.append(asciicode)
    x = 0
    y = 0
    for o in vals:
        for p in o:
            matr.putpixel((x, y), value=int(p))
            x += 1
        x = 0
        y += 1
    matr.save(f"out/{name}.png")


def getlink(image):
    img = Image.open(image)
    link = ""
    for i in range(img.height):
        parola = ""
        for j in range(img.width):
            if img.getpixel((j, i)) == 255:
                val = 1
            else:
                val = 0
            parola = parola + str(val)
        parola = int(parola, 2)
        link = link + chr(parola)
    return link
