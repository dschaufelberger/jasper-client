from piwho import recognition
import glob
import shutil
import os
from  recordings import audiofile_path
recog = recognition.SpeakerRecognizer()
# set the name of the speaker
recog.speaker_name = 'Ruth'
filenames = glob.glob(audiofile_path + 'speakerIdentifierFiles/*.wav')
for filepath in filenames:
    print filepath
    # move the files in recordings for training
    shutil.move(filepath, audiofile_path)
    filename = os.path.basename(filepath)
    print filename
    # create dataset of the files in the directory
    recog.train_new_data(audiofile_path + filename)
