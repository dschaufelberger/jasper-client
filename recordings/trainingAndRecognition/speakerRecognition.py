from piwho import recognition

def greetings():
    recog = recognition.SpeakerRecognizer('/home/pi/jasper/recordings/')
    name = recog.identify_speaker()
    return name[0]

speaker = greetings()
print speaker

#recog = recognition.SpeakerRecognizer('/home/pi/jasper/recordings/trainingAndRecognition/')
#name = recog.identify_speaker()
#print(name[0]) # Recognized speaker
#print(name[1]) # Second best speaker


