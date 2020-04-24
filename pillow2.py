# importing Image class from PIL package
from PIL import Image

# creating a object
image = Image.open("/Users/valmik/Downloads/ponte.jpeg")
MAX_SIZE = (500, 500)

image.thumbnail(MAX_SIZE)

# creating thumbnail
image.save('/Users/valmik/Downloads/ponte_thumbail.jpeg')
image.show()
