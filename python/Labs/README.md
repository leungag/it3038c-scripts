# Lab 7 
This is a Python script using the plugin Pillow to maniupate an image.
On a Windows computer, open PowerShell to install Pillow in using the command :
```
pip install pillow
```
Download and save an image online to your compuer.

Create a file named Lab7.py then open a text editor like notepad to add the Python code:
```powershell
> touch Lab7.py
> notepad Lab7.py
```
In the Python file, Lab7.py, add the following code in the file:
``` python
from PIL import Image, ImageFilter

myImage = Image.open(r'C:\path\to\image.jpg')
```

Next add the body of code.
The body of the code will manipulate the image in 3 different ways and open three different images.
Save the file before running the code.
``` python
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
```
The syntax will alter the image and then display the modified version of the image.

To run the python file use the command:
```powershell
> python Lab7.py
```
It will take a few seconds to display all 3 the modified image.
