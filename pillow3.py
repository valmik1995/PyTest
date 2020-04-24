from PIL import Image
import sys

def watermark_with_transparency(input_image_path, output_image_path, watermark_image_path):
    base_image = Image.open(input_image_path).convert("RGBA") # convert to RGBA is important

    watermark = Image.open(watermark_image_path).convert("RGBA")
    width, height = base_image.size
    mark_width, mark_height = watermark.size
    position = (width-mark_width,height-mark_height) # put the watermark at the lower-right corner

    watermark_width, watermark_height = watermark.size
    image_width, image_height = base_image.size

    aspect_ratio = watermark_width / watermark_height


    new_watermark_width = image_width * 0.25
    watermark.thumbnail((new_watermark_width, new_watermark_width / aspect_ratio), Image.ANTIALIAS)
    watermark_width, watermark_height = watermark.size
    wt_width = width - watermark_width

    transparent = Image.new('RGB', (width, height), (0,0,0,0))
    transparent.paste(base_image, (0,0))
    transparent.paste(watermark, (wt_width,0), mask=watermark)
    transparent.show()
    transparent.save(output_image_path)



if __name__ == '__main__':
    if len(sys.argv)<=1:
        print('python pillow3.py <the_image_name>')
        exit(1)
    the_image = sys.argv[1]
    if the_image is None or len(the_image)==0:
        print('python pillow3.py <the_image_name>')
        exit(1)
    else:
        watermark_with_transparency('./images_origin/%s'%the_image, './images_watermarked/%s'%the_image, './logo.png')
