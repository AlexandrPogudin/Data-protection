from PIL import Image

p = [8, 6, 5, 4]
bit = p[0]

image = Image.open("tux.png")
image_bytes = image.convert("RGB").tobytes()

pixels = list(image.getdata())

def chifr(color):
    w = list(map(int, list(bin(color)[2:].zfill(8))))
    feedback = w[-1]
    for j in range(bit-1, 0, -1):
        if bit-j in p[1:]:
            w[j] = int(feedback != w[j-1])
        else:
            w[j] = w[j-1]
    w[0] = feedback
    return int("".join(list(map(str, w))), 2)

for i in range(len(pixels)):
    r, g, b, a = pixels[i]
    pixels[i] = (chifr(r), chifr(g), chifr(b), chifr(a))

image_ecb = Image.new(image.mode, image.size)
image_ecb.putdata(pixels)
image_ecb.save(f"tuxNEW.png", "PNG")
