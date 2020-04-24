import sys

if __name__ == '__main__':
    if len(sys.argv)<=1:
        print('python pillow3.py <the_image_name>')
        exit(1)
    the_image = sys.argv[1]
    if the_image is None or len(the_image)==0:
        print('python pillow3.py <the_image_name>')
        exit(1)
    else:
        print('else')
