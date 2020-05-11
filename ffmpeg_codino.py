import os
import subprocess
input_01 = '/Users/valmik/Downloads/mp4/WhatsAppBottino.mp4'
input ='/Users/valmik/Downloads/FFmpegProject.mp4'
watermark = '/Users/valmik/PycharmProjects/vvf_online/media/watermarks/Logo16_9.png'
scaled = '/Users/valmik/Pictures/scaled.png'
output = '/Users/valmik/Downloads/mp4/ffmpeg/FFmpeg-Codino.mp4'
codino = '/Users/valmik/PycharmProjects/vvf_online/media/watermarks/CoEmSicurezza.mov'

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
'[0:v] scale=w=min( iw\, min(iw*{1}/ih\,{0})):h=min( ih\, min({1}\,ih*{0}/iw)), setsar=1 [video-scaled]; \
[2:v] scale=w=min( iw\, min(iw*{1}/ih\,{0})):h=min( ih\, min({1}\,ih*{0}/iw)), setsar=1 [video2]; \
[1:v][video-scaled] scale2ref=({0}/{1})*ih/3/sar:ih/3[wm][base]; [base][wm]overlay=W-w [video0]; \
[video0][0:a][video2][3:a] concat=n=2:v=1:a=1[v][a]'.format(width, height),
'-map', '[v]',
'-map', '[a]',
'-crf', '18',
'-preset', 'veryfast', '-f', 'mp4',
output
])
