from PIL import Image
import sys

image = Image.open('/Users/valmik/PycharmProjects/vigilfuoco/multimedia/photos/DSC00119.JPG')
new_image = image.resize((400, 400))
new_image.save('/Users/valmik/Downloads/image_400.jpg')

print(image.size) # Output: (1200, 776)
print(new_image.size) # Output: (400, 400)
