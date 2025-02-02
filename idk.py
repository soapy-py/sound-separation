import h5py
import matplotlib.pyplot as plt  
import torch
import IPython
from IPython.display import Audio

filename='/om2/user/msaddler/spatial_audio_pipeline/assets/GISE-51/processed_isolated_events.hdf5'

with h5py.File(filename, 'r') as f:
    print(f.keys())
    signal_1=(f['signal'])[0]
    signal_2=(f['signal'])[166]
    s_r1= (f['sr'])[0]
    s_r2= (f['sr'])[166]

min_len = min(len(signal_1), len(signal_2))
signal_1 = signal_1[:min_len]
signal_2 = signal_2[:min_len]


overlap=signal_1+signal_2
print(len(overlap), len(signal_1),len(signal_2))


IPython.display.Audio(overlap,rate=s_r1,autoplay=True) 




