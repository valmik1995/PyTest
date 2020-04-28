import os
from PIL import Image
import sys

image_path = '/Users/valmik/PycharmProjects/vigilfuoco/multimedia/photos/DSC00119.JPG'
watermark = '/Users/valmik/PycharmProjects/vigilfuoco/multimedia/watermarks/IMG_4156.PNG'
final_image_path = '/Users/valmik/Downloads/DSC00100.JPG'
# subprocess.call(['/usr/local/bin/convert', input_file_path, '-resize', '64x64', output_file_path])
def create_watermark(image_path, final_image_path, watermark):
    main = Image.open(image_path)
    mark = Image.open(watermark)
    main_width = 1024
    wpercent = (main_width/float(main.size[0]))
    main_height = int((float(main.size[1])*float(wpercent)))

    # Trasparenza Logo
    # mask = mark.convert('L').point(lambda x: min(x, 25))
    # mark.putalpha(mask)

    mark_width, mark_height = mark.size
    aspect_ratio = mark_width / mark_height
    new_mark_width = main_width * 0.25
    mark.thumbnail((new_mark_width, new_mark_width / aspect_ratio), Image.ANTIALIAS)
    mark_width, mark_height = mark.size
    wt_width = main_width - mark_width


    transparent = Image.new('RGB', (main.size), (0,0,0,0))
    transparent.paste(main, (0,0))
    transparent.paste(mark, (wt_width,0), mask=mark)
    transparent.save(final_image_path)
    # image = Image.open(final_image_path)
    # new_image = image.resize((main_width, main_height))
    # new_image.save(final_image_path)

create_watermark(image_path, final_image_path, watermark)
