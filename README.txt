A program to convert image filetypes in python 3.6.0 using the tkinter GUI module.

Can be run using 'python convertpic.py' in the windows command line (requires python 3.6.0 and Pillow 5.0.0).

Using the picture converter:
The picture converter has a display listing the images currently marked for conversion, and four buttons.
Add Pictures - opens a file browser which can be used to add images to the list.
Clear List - clears all images marked for conversion.
Convert to jpg - converts all images in the list to jpg format (RGB data).
Convert to jpg - converts all images in the list to png format (RGBA data).
Converted images are saved to a folder, 'ConvertPic', in the same location as the original images (i.e. there may be multiple 'ConvertPic' folders created if the images in the list are in different locations).

Future improvements:
Add scrolling to the display.
Add choices for where converted pictures are saved.
Add more filetypes (tiff, etc).