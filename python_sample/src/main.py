import sys
import os
from audio.sound_pool import SoundPool
from time import sleep

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)
pool=SoundPool()
pool.behind_pitch_decrease=5
a=pool.play_3d(r"C:\caio\teste.wav", 0, 0, 0, 10, 0, 0, 180.0, True)
sleep(5)
