

from PIL import Image
import system
from PIL import ImageFont
from PIL import ImageDraw
image = sys.argv[1]

img = Image.open(image)

imgx, imgy = img.size

sixthx = int(imgx/6)
sixthy = int(imgy/6)

img2 = Image.open("frog.jpeg")

img2 = img2.resize((sixthx,sixthy), Image.ANTIALIAS)

img.paste(img2, ((imgx-2*sixthx),(imgy-2*sixthy)))

draw = ImageDraw.Draw(img)
font = ImageFont.truetype("papyrus.ttf", 16)
draw.text((sixthx,sixthy),"Graphic Design is my Passion",(255,0,0),font=font)

img.save("new-image.jpg")
