import os
import subprocess
input_01 = '/Users/valmik/Downloads/mp4/WhatsApp01.mp4'
input ='/Users/valmik/Downloads/FFmpegProject.mp4'
watermark = '/Users/valmik/PycharmProjects/vvf_online/media/watermarks/logo_vertical.png'
codino = '/Users/valmik/PycharmProjects/vvf_online/media/watermarks/CoEmSicurezza.mov'
scaled = '/Users/valmik/Pictures/scaled.png'
output = '/Users/valmik/Downloads/mp4/ffmpeg/FFmpeg-Vertical.mp4'

width = 1280
height = int(width/16*9)

if width == 1920:
    bitrate = '10000k'
else:
    bitrate = '4000k'


subprocess.call(['ffmpeg',
'-y', '-loglevel', 'warning', '-i',
input_01,
'-i', watermark,
'-i', codino,
'-f', 'lavfi', '-t', '0.1', '-i', 'anullsrc', #TRACCIA FITTIZIA AUDIO [3:a]
'-filter_complex',
'[0:v] split=2 [video0-1][video0-2]; \
[video0-1] scale=w={0}:h={1},boxblur=luma_radius=min(h\,w)/20:luma_power=1:chroma_radius=min(cw\,ch)/20:chroma_power=1, setsar=1  [bg0]; \
[video0-2] scale=-1:{1}, setsar=1 [video0-2-scaled]; \
[bg0][video0-2-scaled] overlay=x=(W-w)/2:y=(H-h)/2 [video-scaled]; \
[1:v] scale=w={0}:h={1}, setsar=1 [video-watermarks]; \
[2:v] scale=w={0}:h={1}, setsar=1 [video2]; \
[video-scaled][video-watermarks]overlay=0:0 [video0]; \
[video0][0:a][video2][3:a] concat=n=2:v=1:a=1[v][a]'.format(width, height),
'-map', '[v]',
'-map', '[a]',
'-crf', '18',
'-preset', 'veryfast', '-f', 'mp4',
output
])
