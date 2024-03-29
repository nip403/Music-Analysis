import sys
import os
import numpy as np

sys.path.append(parent_dir := os.getcwd() + "\\src")

from MusicInsights.Waveform import Waveform
from MusicInsights.utils import playback, visualise, to_json

np.set_printoptions(threshold=np.inf)

rate = 8000
duration = 5

if __name__ == "__main__":
    bohemian = Waveform(fp=parent_dir + "\\music\\Bohemian Rhapsody.mp3", sample_rate=rate, duration=duration)

    dev = bohemian.deviation[:]
    print([p for p, i in enumerate(dev) if i > 0.1]) # significant samples
    print(bohemian.beat_frames) # beats
    print(dev[np.array([[i-1, i, i+1] for i in bohemian.beat_frames]).flatten()]) # sample "energy" at beat frame edges

    to_json(bohemian, os.path.dirname(__file__))