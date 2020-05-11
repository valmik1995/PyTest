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
#CORRISPONDERE FORMATO ALTRIMENTI NON FUNZIONA 1280x720 (TUTTI DELLE STESSE DIMENSIONI)
ffmpeg -i BeSureToWear.mp4 -i BeSureToWear.mp4 -filter_complex '[0:v] [0:a:0] [1:v] [1:a:0] concat=n=2:v=1:a=1 [v] [a]' -map '[v]' -map '[a]' BeSureToWearConcat.mp4

ffmpeg -i ../../Downloads/WhatsApp03.mp4 -i ../../Downloads/WhatsApp01.mp4 -filter_complex \
"[0:v]scale=640:480:force_original_aspect_ratio=decrease,pad=640:480:(ow-iw)/2:(oh-ih)/2[v0]; \
 [v0][0:a][1:v][1:a]concat=n=2:v=1:a=1[v][a]" \
-map "[v]" -map "[a]" -c:v libx264 -c:a aac -movflags +faststart /Users/valmik/Downloads/conc_diff.mp4

ffmpeg -y -loglevel warning
-i 5sec_640x480.mp4
-i 5sec_1920x1080.mp4
-i 5sec_720x1280.mp4
-filter_complex "
[0:v] scale=w=min(iw*480/ih\,640):h=min(480\,ih*640/iw), pad=w=640:h=480:x=(640-iw)/2:y=(480-ih)/2  [video0];
[1:v] scale=w=min(iw*480/ih\,640):h=min(480\,ih*640/iw), pad=w=640:h=480:x=(640-iw)/2:y=(480-ih)/2  [video1];
[2:v] scale=w=min(iw*480/ih\,640):h=min(480\,ih*640/iw), pad=w=640:h=480:x=(640-iw)/2:y=(480-ih)/2  [video2];
[video0][video1][video2] concat=n=3:v=1 [v]
" -map "[v]" -an -c:v h264 -crf 18 -preset veryfast -f mp4 output.mp4


ffmpeg -y -loglevel warning ../../Downloads/WhatsApp03.mp4 -i ../../Downloads/WhatsApp01.mp4 -filter_complex "[0:v] scale=w=min(iw*
480/ih\,640):h=min(480\,ih*640/iw), pad=w=640:h=480:x=(640-iw)/2:y=(480-ih)/2  [video0]; [1:v] scale=w=min(iw*480/ih\,640):h=min(480\,ih*640/iw), pad=w=640:
h=480:x=(640-iw)/2:y=(480-ih)/2  [video1]; [video0][video1] concat=n=2:v=1 [v]" -map "[v]" -an -c:v h264 -crf 18 -preset veryfast -f mp4 /Users/valmik/Downl
oads/conc_diff.mp4


file1 = '/Users/valmik/Downloads/WhatsApp01.mp4'
file2 = '/Users/valmik/Downloads/WhatsApp01.mp4'
file3 = '/Users/valmik/Downloads/WhatsApp01.mp4'

ffmpeg -y -loglevel warning -i /Users/valmik/Downloads/WhatsApp03.mp4 -i /Users/valmik/Downloads/WhatsApp02.mp4 -i /Users/valmik/Downloads/WhatsApp01.mp4 -filter_complex "[0:v] split=2 [video0-1][video0-2]; [1:v] split=2 [video1-1][video1-2]; [2:v] split=2 [video2-1][video2-2]; [video0-1] scale=w=1280:h=720,boxblur=luma_radius=min(h\,w)/20:luma_power=1:chroma_radius=min(cw\,ch)/20:chroma_power=1, setsar=1  [bg0]; [video1-1] scale=w=1280:h=720,boxblur=luma_radius=min(h\,w)/20:luma_power=1:chroma_radius=min(cw\,ch)/20:chroma_power=1, setsar=1  [bg1]; [video2-1] scale=w=1280:h=720,boxblur=luma_radius=min(h\,w)/20:luma_power=1:chroma_radius=min(cw\,ch)/20:chroma_power=1, setsar=1  [bg2]; [video0-2] scale=w=min( iw\, min(iw*720/ih\,1280)):h=min( ih\, min(720\,ih*1280/iw)), setsar=1 [video0-2-scaled]; [video1-2] scale=w=min( iw\, min(iw*720/ih\,1280)):h=min( ih\, min(720\,ih*1280/iw)), setsar=1 [video1-2-scaled]; [video2-2] scale=w=min( iw\, min(iw*720/ih\,1280)):h=min( ih\, min(720\,ih*1280/iw)), setsar=1 [video2-2-scaled]; [bg0][video0-2-scaled] overlay=x=(W-w)/2:y=(H-h)/2 [video0]; [bg1][video1-2-scaled] overlay=x=(W-w)/2:y=(H-h)/2 [video1]; [bg2][video2-2-scaled] overlay=x=(W-w)/2:y=(H-h)/2 [video2]; [video0][video1][video2] concat=n=3:v=1[v]"  -map "[v]" -an -c:v h264 -crf 18 -preset veryfast -f mp4 /Users/valmik/Downloads/WhatsAppConc.mp4


ffmpeg -y -loglevel warning
-i 5sec_640x480.mp4
-i 5sec_1920x1080.mp4
-i 5sec_720x1280.mp4
-filter_complex "
[0:v] split=2 [video0-1][video0-2];
[1:v] split=2 [video1-1][video1-2];
[2:v] split=2 [video2-1][video2-2];
[video0-1] scale=w=1280:h=720,boxblur=luma_radius=min(h\,w)/20:luma_power=1:chroma_radius=min(cw\,ch)/20:chroma_power=1, setsar=1  [bg0];
[video1-1] scale=w=1280:h=720,boxblur=luma_radius=min(h\,w)/20:luma_power=1:chroma_radius=min(cw\,ch)/20:chroma_power=1, setsar=1  [bg1];
[video2-1] scale=w=1280:h=720,boxblur=luma_radius=min(h\,w)/20:luma_power=1:chroma_radius=min(cw\,ch)/20:chroma_power=1, setsar=1  [bg2];
[video0-2] scale=w=min( iw\, min(iw*720/ih\,1280)):h=min( ih\, min(720\,ih*1280/iw)), setsar=1 [video0-2-scaled];
[video1-2] scale=w=min( iw\, min(iw*720/ih\,1280)):h=min( ih\, min(720\,ih*1280/iw)), setsar=1 [video1-2-scaled];
[video2-2] scale=w=min( iw\, min(iw*720/ih\,1280)):h=min( ih\, min(720\,ih*1280/iw)), setsar=1 [video2-2-scaled];
[bg0][video0-2-scaled] overlay=x=(W-w)/2:y=(H-h)/2 [video0];
[bg1][video1-2-scaled] overlay=x=(W-w)/2:y=(H-h)/2 [video1];
[bg2][video2-2-scaled] overlay=x=(W-w)/2:y=(H-h)/2 [video2];
[video0][video1][video2] concat=n=3:v=1[v]"
-map "[v]" -an -c:v h264 -crf 18 -preset veryfast -f mp4 output.mp4



ffmpeg -report -i "./video/big_buck_bunny.mp4" -i "./video/big_buck_bunny.mp4" -an \
    -filter_complex \
    "[0:v]trim=start=0:end=9,setpts=PTS-STARTPTS[firstclip]; \
    [1:v]trim=start=1,setpts=PTS-STARTPTS[secondclip]; \
    [0:v]trim=start=9:end=10,setpts=PTS-STARTPTS[fadeoutsrc]; \
    [1:v]trim=start=0:end=1,setpts=PTS-STARTPTS[fadeinsrc]; \
    [fadeinsrc]format=pix_fmts=yuva420p,fade=t=in:st=0:d=1:alpha=1[fadein]; \
    [fadeoutsrc]format=pix_fmts=yuva420p,fade=t=out:st=0:d=1:alpha=1[fadeout]; \
    [fadein]fifo[fadeinfifo]; \
    [fadeout]fifo[fadeoutfifo]; \
    [fadeoutfifo][fadeinfifo]overlay[crossfade]; \
    [firstclip][crossfade][secondclip]concat=n=3" \
./rendered/outputname.mp4



# FUNZIONA METTE WATERMARK CON CODINO FINALE
ffmpeg -y -loglevel warning -i /Users/valmik/Downloads/FFmpegProject.mp4 -i /Users/valmik/Pictures/logo.png -i /Users/valmik/Downloads/CoEmSicurezza.mov -filter_complex "[0:v] scale=w=min( iw\, min(iw*720/ih\,1280)):h=min( ih\, min(720\,ih*1280/iw)), setsar=1 [video-scaled];[2:v] scale=w=min( iw\, min(iw*720/ih\,1280)):h=min( ih\, min(720\,ih*1280/iw)), setsar=1 [video2];[1:v][video-scaled] overlay=x=(W-w)/2:y=(H-h)/2 [video0];[video0][video2] concat=n=2:v=1[v]" -map "[v]" -an -c:v h264 -crf 18 -preset veryfast -f mp4 /Users/valmik/Downloads/WhatsApp003.mp4
