from PIL import Image
from PIL.ExifTags import TAGS

image = Image.open('/Users/valmik/Downloads/ponte_thumbail.jpeg')
info = image._getexif()

for tag, value in info.items():
    key = TAGS.get(tag)
    if key == 'Make':
        print(key + ': ' + str(value))
    elif key == 'Model':
        print(key + ': ' + str(value))
    elif key == 'Orientation':
        print(key + ': ' + str(value))
    elif key == 'Flash':
        print(key + ': ' + str(value))
