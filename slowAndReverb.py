from pedalboard import Pedalboard, Reverb
from pedalboard.io import AudioFile


'''
Function for slowing down and reverbing songs (.wav file format).
'''
def processAudio(filename, roomSize, sampleRate):
    with AudioFile(filename, 'r') as f:
        audio = f.read(f.frames)
    board = Pedalboard([Reverb(room_size=roomSize)])
    effected = board(audio, sampleRate)
    splitFileName = filename.split("/")
    fname = splitFileName[len(splitFileName) - 1]
    with AudioFile(f'{roomSize}_{sampleRate}_slowAndReverb_{fname}', 'w', sampleRate, effected.shape[0]) as out:
        out.write(effected)


def processMultipleAudioFiles(fileList, roomSize, sampleRate):
    for f in fileList:
        processAudio(f, roomSize, sampleRate)

