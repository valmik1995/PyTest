from PIL import Image

TRANSPARENCY = 100       # percentage

image = Image.open('/Users/valmik/PycharmProjects/vvf_online/media/ajaximage/miki_2.jpg')
watermark = Image.open('/Users/valmik/PycharmProjects/vvf_online/media/watermarks/IMG_4156.PNG')
mask = watermark.convert('L').point(lambda x: min(x, 25))
watermark.putalpha(mask)

watermark_width, watermark_height = watermark.size
image_width, image_height = image.size

aspect_ratio = watermark_width / watermark_height

new_watermark_width = image_width * 0.25
watermark.thumbnail((new_watermark_width, new_watermark_width / aspect_ratio), Image.ANTIALIAS)

watermark.save('/Users/valmik/Downloads/logo_thumbail.png')
watermark.show()
# if watermark.mode!='RGBA':
#     alpha = Image.new('L', watermark.size, 255)
#     watermark.putalpha(alpha)
#
# paste_mask = watermark.split()[3].point(lambda i: i * TRANSPARENCY / 100.)
# temp_image.paste(watermark, (0,0), mask=paste_mask)
# temp_image.save('/Users/valmik/Downloads/ponte_watermark.jpeg')
