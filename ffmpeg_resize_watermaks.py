import os
import subprocess
input = '/Users/valmik/Downloads/VID-20200511-WA0020.mp4'
watermark = '/Users/valmik/Pictures/logo.png'
scaled = '/Users/valmik/Pictures/scaled.png'
output = '/Users/valmik/Downloads/FFmpegProject.mp4'
codino = '/Users/valmik/Downloads/WhatsApp02.mp4'

width = 1280
height = int(width/16*9)

if width == 1920:
    bitrate = '10000k'
else:
    bitrate = '4000k'


subprocess.call(['ffmpeg',
'-i', input,
'-i', codino,
'-i', watermark,
'-filter_complex', '[2:v][0:v]scale2ref=({}/{})*ih/1/sar:ih/1[wm][base];[base][wm]overlay=10:10;'.format(width, height),
'-s',
'{}:{}'.format(width, height),
'-vcodec',
'mpeg4',
'-b:v', bitrate,
output
])
