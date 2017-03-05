from piwho import recognition
recog = recognition.SpeakerRecognizer('/home/pi/jasper/recordings/')
name = []
name = recog.identify_speaker()
print(name[0]) # Recognized speaker
print(name[1]) # Second best speaker
