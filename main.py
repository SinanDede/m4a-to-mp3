from os.path import isfile, join
from moviepy.editor import *


m4a_files = ["inputfiles/" + f for f in os.listdir('inputfiles') if isfile(join('inputfiles', f))]
mp3_files = [f.replace('inputfiles', 'outputfiles').replace('.m4a', '.mp3') for f in m4a_files]

for i in range(len(m4a_files)):
    m4aclip = AudioFileClip(m4a_files[i])
    mp3clip = m4aclip.write_audiofile(mp3_files[i])

m4aclip.close()