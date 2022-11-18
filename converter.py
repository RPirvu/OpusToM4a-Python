import os
from pydub import AudioSegment
path = os.getcwd()

#Change working directory
os.chdir(path)
audio_files = os.listdir()
# You dont need the number of files in the folder, just iterate over them directly using:
filecount = 0
for file in audio_files:
    name, ext = os.path.splitext(file)
    if ext == ".opus":
        filecount=filecount+1
k=1
for file in audio_files:
    #spliting the file into the name and the extension
    name, ext = os.path.splitext(file)
    if ext == ".opus":
       mp3_sound = AudioSegment.from_file(file)
       #rename them using the old name + ".wav"
       mp3_sound.export("{0}.m4a".format(name), format="mp4")
       print("{0} out of {1}".format(k,filecount))
       k=k+1
