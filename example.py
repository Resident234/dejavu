import warnings
import json
import logging
import datetime
import threading, time
import vlc
import os
import sys
#import multiprocessing
from multiprocessing import Process

warnings.filterwarnings("ignore")

from dejavu import Dejavu
from dejavu.recognize import FileRecognizer, MicrophoneRecognizer
from dejavu.record_stream import RecordStream
import dejavu.logger as logger

# load config from a JSON file (or anything outputting a python dictionary)
with open("dejavu.cnf") as f:
    config = json.load(f)

dejavu_process_logger = logger.get_logger('dejavu_process_logger')
record_stream_logger = logger.get_logger('record_stream_logger')


def dejavu_process():
    ticker = threading.Event()
    while not ticker.wait(60 * 2):#60 * 120
        dejavu_process_logger.info('TIME LABEL')
        djv.fingerprint_translation_record_directory("records", [".mp3"])

def record_stream_process():
    ticker = threading.Event()
    while not ticker.wait(1):
        record_stream_logger.info('TIME LABEL')
        record_stream.record()

def recognize_process():
    ticker = threading.Event()
    # while not ticker.wait(60 * 1):  #
    print "recognize_process"
    dejavu_process_logger.info('recognize_process')
    song = djv.recognize(FileRecognizer, "records/1103_2019-09-14-18-40-43.mp3")
    print "#1 From file we recognized: %s\n" % song

if __name__ == '__main__':

    # create a Dejavu instance
    djv = Dejavu(config)
    #record_stream = RecordStream()
    #dejavu_process = Process(target=dejavu_process)
    #dejavu_process.start()
    #record_stream_process = Process(target=record_stream_process)
    #record_stream_process.start()
    recognize_process = Process(target=recognize_process)
    recognize_process.start()
    #dejavu_process.join()
    #record_stream_process.join()
    recognize_process.join()

    #song = djv.recognize(FileRecognizer, "records/01 Chasing shadows_fragment.mp3")
    #print "#2 From file we recognized: %s\n" % song

    #djv.fingerprint_file("records/2019-02-24_20-41-01.mp3")
    #djv.fingerprint_translation_record_file("records/2019-02-24_20-41-01.mp3")


    # 0 2 21  0 43 50  1 03 05 -> 1 03 32
    # Recognize audio from a file
    #song = djv.recognize(FileRecognizer, "mp3/Sean-Fournier--Falling-For-You.mp3")
    #print "From file we recognized: %s\n" % song

    #song = djv.recognize(FileRecognizer, "records/2019-02-24_20-41-01.mp3")
    #print "#3 From file we recognized: %s\n" % song
    #'offset_seconds': 3784.99193

    #song = djv.recognize(FileRecognizer, "records/2019-02-24_20-41-01_ad.mp3")
    #print "#4 From file we recognized: %s\n" % song

    #recognizer = FileRecognizer(djv)

    #recognizer.recognize_directory("records/splitted", [".mp3"])
    #recognizer.recognize_directory("records/splitted_10", [".mp3"])
    #recognizer.recognize_directory("records/splitted_3", [".mp3"])
    #recognizer.recognize_directory("records/splitted_1", [".mp3"])

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
    #song = recognizer.recognize_file("mp3/Josh-Woodward--I-Want-To-Destroy-Something-Beautiful.mp3")
    #print "No shortcut, we recognized: %s\n" % song
