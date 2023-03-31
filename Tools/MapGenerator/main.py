from PIL import Image
from cairosvg import svg2png
from datetime import datetime
import os

def rgba2hex(rgba):
    r = int(rgba[0])
    g = int(rgba[1])
    b = int(rgba[2])
    a = int(rgba[3])
    return f'{r:02x}{g:02x}{b:02x}{a:02x}'.upper()

folder = f"{datetime.now().year}-{datetime.now().month}-{datetime.now().day} {datetime.now().hour}.{datetime.now().minute}.{datetime.now().second}"
os.mkdir(folder)
os.mkdir(folder+"/tiles")

with open("input.svg") as file:
    text = file.read()
    svg2png(bytestring=text, write_to=folder+'/out.png', scale=2)

img = Image.open(folder+"/out.png")
outs = {}
px_outs = {}
py_outs = {}
l_outs = {}

total = img.size[0] * img.size[1]
z = 0
for x in range(img.size[0]):
    for y in range(img.size[1]):
        z += 1
        if z % 3000 == 0:
            print(z/total)
        col = (img.getpixel((x, y)))
        if col not in outs:
            outs[col] = Image.new("RGBA", img.size, (0,0,0,0))
            px_outs[col] = []
            py_outs[col] = []
            l_outs[col] = 0
        outs[col].putpixel((x, y), (255, 255, 255, 255))
        l_outs[col] += 1
        px_outs[col].append(x)
        py_outs[col].append(y)


i = 0
keys = {
    "00AAFFFF": "united kingdom",
    "0088CCFF": "france",
    "FF0000FF": "russia",
    "990000FF": "belarus",
    "CC0000FF": "ukraine",
    "00FF00FF": "saudi arabia",
    "FFFF00FF": "china",
    "B9B9B9FF": "other",
    "FFFFFFFF": None,
    "00000000": None
}
coords = "{"
for col in outs:
    i += 1
    key = i
    if rgba2hex(col) in keys:
        key = keys[rgba2hex(col)]
        if key == None:
            continue
        
    concs = ( int(sum(px_outs[col])/l_outs[col]), int(sum(py_outs[col])/l_outs[col] ))
    outs[col].save(f"{folder}/tiles/{str(key)}.png")
    coords += f"\n\t\"{key}\": [{concs[0]}, {concs[1]}],"

with open(folder+"/coords.json", 'w') as file:
    coords = coords[:-1] + "\n}"
    file.write(coords)
