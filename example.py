import warnings
import json

warnings.filterwarnings("ignore")

from dejavu import Dejavu
from dejavu.recognize import FileRecognizer, MicrophoneRecognizer

# load config from a JSON file (or anything outputting a python dictionary)
with open("dejavu.cnf.SAMPLE") as f:
    config = json.load(f)

if __name__ == '__main__':

    # create a Dejavu instance
    djv = Dejavu(config)

    # Fingerprint all the mp3's in the directory we give it
    #djv.fingerprint_directory("mp3", [".mp3"])
    #djv.fingerprint_directory("AC-DC", [".mp3"])
    #djv.fingerprint_directory("28 scorpions", [".mp3"])

    djv.fingerprint_file("records/01 Chasing shadows.mp3")

    song = djv.recognize(FileRecognizer, "records/01 Chasing shadows.mp3")
    print "#1 From file we recognized: %s\n" % song

    song = djv.recognize(FileRecognizer, "records/01 Chasing shadows_fragment.mp3")
    print "#2 From file we recognized: %s\n" % song

    djv.fingerprint_file("records/2019-02-24_20-41-01.mp3")
    djv.fingerprint_file__get_hashes("records/2019-02-24_20-41-01.mp3")


    # 0 2 21  0 43 50  1 03 05 -> 1 03 32
    # Recognize audio from a file
    #song = djv.recognize(FileRecognizer, "mp3/Sean-Fournier--Falling-For-You.mp3")
    #print "From file we recognized: %s\n" % song

    song = djv.recognize(FileRecognizer, "records/2019-02-24_20-41-01.mp3")
    print "#3 From file we recognized: %s\n" % song

    song = djv.recognize(FileRecognizer, "records/2019-02-24_20-41-01_ad.mp3")
    print "#4 From file we recognized: %s\n" % song

    #song = djv.recognize(FileRecognizer, "records/2019-02-24_00-59-46.mp3")
    #print "From file we recognized: %s\n" % song

    # Or recognize audio from your microphone for `secs` seconds
    #secs = 5
    #song = djv.recognize(MicrophoneRecognizer, seconds=secs)
    #if song is None:
    #    print "Nothing recognized -- did you play the song out loud so your mic could hear it? :)"
    #else:
    #    print "From mic with %d seconds we recognized: %s\n" % (secs, song)

    # Or use a recognizer without the shortcut, in anyway you would like
    recognizer = FileRecognizer(djv)
    song = recognizer.recognize_file("mp3/Josh-Woodward--I-Want-To-Destroy-Something-Beautiful.mp3")
    print "No shortcut, we recognized: %s\n" % song
