from PIL import Image, ImageFilter

myImage = Image.open(r'C:\it3038c-scripts\images\land.jpg')


# Blurr the image
blurred_image = myImage.filter(ImageFilter.BoxBlur(5))
blurred_image.show()

# Rotate the image
rotated_image = myImage.rotate(-180)
rotated_image.show()

# Create a Thumbnail
thumbnail_size = (100,100)
thumbnail = myImage.copy()
thumbnail.thumbnail(thumbnail_size)
thumbnail.show()
