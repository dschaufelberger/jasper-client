from piwho import recognition
from recordings import audiofile_path

def greetings():
    recog = recognition.SpeakerRecognizer(audiofile_path + 'speakerIdentifierFiles/')
    name = recog.identify_speaker()
    return 'Speaker ' + name[0]

speaker = greetings()
print speaker

