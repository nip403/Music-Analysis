# Music Analysis
 
Basic tool for a larger project using animateddiff for generative advertisements/music videos (tbd)

https://pypi.org/project/MusicInsights/1.0/

```
pip install MusicInsights
```

```
>>> import MusicInsights as mi
>>> w = mi.Waveform.Waveform("path\\to\\file.mp3", sample_rate>=8000) # hassle free processing
>>> mi.utils.playback(w) # cues the sampled file
>>> mi.utils.visualise(w) # plt of the waveform
>>> mi.utils.to_json(w, path\\to\\dest\\) # save to json
```

### Exciting new features
- no planned cmd support
- no planned updates
