import dejavu.fingerprint as fingerprint
import dejavu.decoder as decoder
import numpy as np
import pyaudio
import time
import logging
import datetime
import threading, time
import vlc
import os
import sys
import dejavu.logger as logger

class RecordStream(object):#
    #type = None

    def __init__(self):
        super(RecordStream, self).__init__()
        self.logger = logger.get_logger('record_stream_logger')
        self.interval = 60 * 120

    def record(self):
        filepath = 'https://rt-news.secure.footprint.net/1103.m3u8'
        movie = os.path.expanduser(filepath)
        if 'https://' not in filepath:
            if not os.access(movie, os.R_OK):
                msg = 'Error: %s file is not readable' % movie
                print msg
                self.logger.error(msg)
                return

        recording_duration = self.interval

        # while (1):
        filename_record = "records/1103_" + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + "_recording.mp3"
        filename_record_final = "records/1103_" + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".mp3"

        msg = "Starting recording to file %s" % filename_record
        print msg
        self.logger.info(msg)

        filename_and_command = "--sout=#transcode{vcodec=none,acodec=mp3,ab=320,channels=2,samplerate=44100}:file{dst=" + filename_record + "}"
        print filename_and_command
        #    filename_and_command = "--sout=file/ts:example" + str(clipNumber) + ".mp3"
        instance = vlc.Instance(filename_and_command)
        try:
            media = instance.media_new(movie)
        except NameError:
            msg = 'NameError: % (%s vs Libvlc %s)' % (sys.exc_info()[1], vlc.__version__, vlc.libvlc_get_version())
            print msg
            self.logger.error(msg)
            return
        player = instance.media_player_new()
        player.set_media(media)
        player.play()
        time.sleep(recording_duration)
        # exit()
        player.stop()
        os.rename(filename_record, filename_record_final)

        msg = "Ending recording to file"
        print (msg)
        self.logger.info(msg)
