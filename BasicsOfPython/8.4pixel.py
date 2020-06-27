from PIL import Image

img= Image.open("1.jpg")
w,h=img.size
img.show()

#reverse the pixel values
for x in range(w):
    for y in range(h):

        cord=(x,y)
        r,b,g=img.getpixel(cord)
        neg_color=(255-r,255-g,255-b)
        img.putpixel(cord,neg_color)

img.show()