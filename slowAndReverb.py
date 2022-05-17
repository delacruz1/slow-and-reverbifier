from pedalboard import Pedalboard, Reverb
from pedalboard.io import AudioFile
import os



# Function for slowing down and reverbing songs (.wav file format).

def processAudio(filename, roomSize, sampleRate):
    with AudioFile(filename, 'r') as f:
        audio = f.read(f.frames)
    board = Pedalboard([Reverb(roomSize)])
    effected = board(audio, sampleRate)
    fname = os.path.basename(filename)
    with AudioFile(f'{roomSize}_{sampleRate}_slowAndReverb_{fname}', 'w', sampleRate, effected.shape[0]) as out:
        out.write(effected)

# Function for handling multiple audio files
def processMultipleAudioFiles(fileList, roomSize, sampleRate):
    for f in fileList:
        processAudio(f, roomSize, sampleRate)
