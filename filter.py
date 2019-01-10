from PIL import Image
import sys
from PIL import ImageFont
from PIL import ImageDraw
image = sys.argv[1]

img = Image.open(image)

imgx, imgy = img.size

sixthx = int(imgx/6)
sixthy = int(imgy/6)

img2 = Image.open("frog.jpg")

img2 = img2.resize((int(3*sixthx/2),int(3*sixthy/2)), Image.ANTIALIAS)

img.paste(img2, ((imgx-int(7*sixthx/4)),(sixthy)))

draw = ImageDraw.Draw(img)
font = ImageFont.truetype("papyrus.ttf", int(sixthx/4))
draw.text((sixthx/2,2*sixthy),"Graphic Design is my Passion",(255,0,0),font=font)

img.save("new-image.jpg")
img.show()
