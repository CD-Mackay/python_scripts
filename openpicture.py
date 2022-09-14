from PIL import Image

with Image.open("ongo-gablogian.jpg") as im:
  im.rotate(89).show()