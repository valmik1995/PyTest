import os
import subprocess
input = '/Users/valmik/Downloads/VID_20200425_163715.mp4'
watermark = '/Users/valmik/Pictures/logo.png'
scaled = '/Users/valmik/Pictures/scaled.png'
output = '/Users/valmik/Downloads/FFmpegProject.mp4'
bitrate = '4000k'
width = '4000'


subprocess.call([
'ffprobe',
'-v', 'quiet', '-show_entries', 'stream=width,height', '-of',
'default=noprint_wrappers=1', input
])

subprocess.call([
'ffmpeg', '-i', watermark, '-y', '-v', 'quiet', '-vf', 'scale={}*0.45:-1'.format(width), scaled
])

subprocess.call(['ffmpeg', '-i', input,
'-i', scaled,
'-filter_complex', 'overlay=W-w',
'-s',
'1280:720',
'-vcodec',
'mpeg4',
'-b:v', bitrate,
output
])
