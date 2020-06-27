from PIL import Image, ImageEnhance, ImageFilter

vip=Image.open("1.jpg")
vip=vip.convert("L")
vip=vip.filter(ImageFilter.FIND_EDGES)
vip=vip.filter(ImageFilter.EDGE_ENHANCE_MORE)
vip.show()