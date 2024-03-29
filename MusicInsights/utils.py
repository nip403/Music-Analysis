import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np

from MusicInsights.Waveform import Waveform

def overload(Type):
    def decorator(func):
        def wrapper(*args):
            if len(args) == 2:
                return func(*args)
            
            elif len(args) == 1 and isinstance(args[0], Type):
                return func(args[0].samples, args[0].sample_rate)
            
            else:
                raise TypeError("Invalid args")
            
        return wrapper
    return decorator

@overload(Waveform)
def playback(samples: list[float], sample_rate: int) -> None:
    """ Playback audio sampled from mp3

    Args:
        samples (list[float]): np.ndarray of (normalised) amplitudes
        sample_rate (int): sample rate of samples
        
    Args:
        waveform (Waveform): Waveform object instance
    """
    
    assert sample_rate >= 8000, "Sample rate must be >= 8000" # replayer requires >= 8000
        
    sd.play(samples, sample_rate)  
    sd.wait() 

@overload(Waveform)

def visualise(samples: list[float], sample_rate: int) -> None:
    """ Visualise amplitudes in audio waveform

    Args:
        samples (list[float]): np.ndarray of (normalised) amplitudes
        sample_rate (int): sample rate of samples
        
    Args:
        waveform (Waveform): Waveform object instance
    """
    
    time = np.arange(len(samples)) / sample_rate

    plt.plot(time, samples)
    
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    
    plt.title('Waveform')
    
    plt.grid(True)
    plt.show()