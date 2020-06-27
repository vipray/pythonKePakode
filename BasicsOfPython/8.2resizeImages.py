from PIL import Image

def resize(img_names,size=(200,200)):
    for img_name in img_names:
        img=Image.open(img_name)
        img=img.resize(size)
        img.save("resized"+img_name)
    

img_names=["1.jpg","2.jpg","3.jpg"]

resize(img_names)

print("____________\n\n")

#cropping
img=Image.open("1.jpg")
img.show()
img=img.crop((100,100,400,400))
img=img.rotate(90)
img.show()


