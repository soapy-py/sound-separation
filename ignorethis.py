
import h5py
import random
import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader

class AudioDataset(Dataset):
    def __init__(self, hdf5_file, num_samples):
        self.hdf5_file = hdf5_file
        self.event_names = list(hdf5_file.keys())[4]
        self.num_samples = num_samples

    def __len__(self):
        return self.num_samples

    def __getitem__(self, index):
        event1, event2 = random.sample(self.event_names, 2)
        audio1 = self.hdf5_file[event1][8]
        audio2 = self.hdf5_file[event2][8]
        overlapped = audio1 + audio2 #is this allowed
        return overlapped, f"{event1}_{event2}"

hdf5_path = '/om2/user/msaddler/spatial_audio_pipeline/assets/GISE-51/processed_isolated_events.hdf5'
hdf5_file = h5py.File(hdf5_path, 'r')

# number of overlapped sound samples to create
num_overlapped_samples = 10

# Createing audiodataset 
audio_dataset = AudioDataset(hdf5_file, num_overlapped_samples)

batch_size = 32
num_workers = 4

dataloader = DataLoader(audio_dataset, batch_size=batch_size, shuffle=True, num_workers=num_workers)

for batch_audio, batch_labels in dataloader:
    # Convert batch_audio and batch_labels to tensors? am i doing this right
    batch_audio = torch.Tensor(batch_audio)
    batch_labels = torch.Tensor(batch_labels)
    
    
    print(f"Batch audio shape: {batch_audio.shape}")
    print(f"Batch labels: {batch_labels}")

    for i in range(batch_audio.size(0)):
        audio = batch_audio[i].numpy()
        label = batch_labels[i]
        filename = f"batch_{i}.wav"
    
    break




