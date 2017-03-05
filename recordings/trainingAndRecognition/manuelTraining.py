from piwho import recognition
recog = recognition.SpeakerRecognizer()
# set the name of the speaker
recog.speaker_name = 'Ruth1'
# create dataset of the files in the directory
recog.train_new_data('/home/pi/jasper/recordings/')
