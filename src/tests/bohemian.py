import sys
import os
import numpy as np

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from MusicInsights.Waveform import Waveform
from MusicInsights.utils import playback, visualise, to_json

np.set_printoptions(threshold=np.inf)

rate = 8000
duration = 5


"""
print([p for p, i in enumerate(dev) if i > 0.1])
print(bohemian.beat_frames)
#print(dev[np.array([[i-1, i, i+1] for i in bohemian.beat_frames]).flatten()])
"""

if __name__ == "__main__":
    bohemian = Waveform(fp=parent_dir + "\\music\\Bohemian Rhapsody.mp3", sample_rate=rate, duration=duration)

    to_json(bohemian, os.path.dirname(__file__))