from PIL import Image, ImageEnhance, ImageFilter
import os


# change image format
# img1 = Image.open('pic1.jpg')
# img1.save('pic1.pdf')

# change format of all in directory at onces
# for item in os.listdir():
#     if item.endswith('.jpg'):
#         img1 = Image.open(item)
#         filename,extension = os.path.splitext(item)
#         img1.save(f"{filename}.png")





# change size of image
# max_size = (200,200)
# img1 = Image.open('pic1.jpg')
# img1.thumbnail(max_size)
# img1.save('img1_small.jpg')

# change size of all in directory at once
# max_size = (150,150)
# for item in os.listdir():
#     if item.endswith('.jpg'):
#         img1 = Image.open(item)
#         img1.thumbnail(max_size)
#         img1.save(f'{item}_small.jpg')


# sharpness

# img1 = Image.open('img11.jpg')
# enhancer = ImageEnhance.Sharpness(img1)
# enhancer.enhance(3).save('imh11en.jpg')

# color

# img1 = Image.open('img11.jpg')
# enhancer = ImageEnhance.Color(img1)
# enhancer.enhance(1.5).save('imh11en.jpg')


# brightness

# img1 = Image.open('img11.jpg')
# enhancer = ImageEnhance.Brightness(img1)
# enhancer.enhance(1.1).save('imh11en.jpg')

# contrast

# img1 = Image.open('img11.jpg')
# enhancer = ImageEnhance.Contrast(img1)
# enhancer.enhance(1.1).save('imh11en.jpg')

# blurr

# img1 = Image.open('img11.jpg')
# img1.filter(ImageFilter.GaussianBlur(radius = 3)).save('img11burr.jpg')
