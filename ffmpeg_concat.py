import os
import subprocess

file1 = '/Users/valmik/Downloads/WhatsApp01.mp4'
file2 = '/Users/valmik/Downloads/WhatsApp02.mp4'
file3 = '/Users/valmik/Downloads/WhatsApp03.mp4'
watermark = '/Users/valmik/Pictures/logo.png'
output = 'MEDIA/FFmpegConcat.mp4'

width = 1280
height = int(width/16*9)

if width == 1920:
    bitrate = '10000k'
else:
    bitrate = '4000k'

subprocess.call(['ffmpeg',
'-i', 'concat:{}|{}|{}'.format(file1, file2, file3),
'-c', 'copy',
'-s',
'{}:{}'.format(width, height),
'-vcodec',
'mpeg4',
'-b:v', bitrate,
output
])


# subprocess.call(['ffmpeg',
# '-i', input,
# '-i', watermark,
# '-filter_complex', '[1:v][0:v]scale2ref=({}/{})*ih/1/sar:ih/1[wm][base];[base][wm]overlay=10:10'.format(width, height),
# '-s',
# '{}:{}'.format(width, height),
# '-vcodec',
# 'mpeg4',
# '-b:v', bitrate,
# output
# ])
