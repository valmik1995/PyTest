import os
import subprocess
input = '/Users/valmik/Downloads/WhatsApp.mp4'
watermark = '/Users/valmik/PycharmProjects/vvf_online/media/watermarks/IMG_4156.PNG'
output = '/Users/valmik/Downloads/FFmpegProject.mp4'
bitrate = '4000k'

subprocess.call(['ffmpeg', '-i', input, '-i', watermark, '-filter_complex', 'overlay=W-w', '-s', '1280:720', '-vcodec', 'mpeg4', '-b:v', bitrate, output])
