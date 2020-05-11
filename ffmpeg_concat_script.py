import glob
import os
def concatenate():
	stringa = "ffmpeg -i \"concat:"
	elenco_video = glob.glob('/Users/valmik/Downloads/WhatsApp0*')
	elenco_file_temp = []
	for f in elenco_video:
		file = "MEDIA/temp" + str(elenco_video.index(f) + 1) + ".ts"
		os.system("ffmpeg -i " + f + " -c copy -bsf:v h264_mp4toannexb -f mpegts " + file)
		elenco_file_temp.append(file)
	print(elenco_file_temp)
	for f in elenco_file_temp:
		stringa += f
		if elenco_file_temp.index(f) != len(elenco_file_temp)-1:
			stringa += "|"
		else:
			stringa += "\" -c copy  -bsf:a aac_adtstoasc MEDIA/output.mp4"
	print(stringa)
	os.system(stringa)

concatenate()

#Funziona Perfettamente non Toccare
#https://pymotw.com/2/glob/ Riferimento preso per questo file concernete glob.glob
