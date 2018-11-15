from PIL import Image
import system
image = sys.argv[1]

img = Image.open(image)

imgx, imgy = img.size

sixthx = int(imgx/6)
sixthy = int(imgy/6)