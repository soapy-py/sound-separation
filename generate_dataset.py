import h5py
import matplotlib.pyplot as plt  
#import torch
import IPython
from IPython.display import Audio
import numpy as np
import tqdm



filename='/om2/user/msaddler/spatial_audio_pipeline/assets/GISE-51/processed_isolated_events.hdf5'
rng=np.random.default_rng()



#start off with 50 samples, end goal is 500k --nope now its 100k
num_samples=100000

#empty lists to append info later to add to hdf5 file
signal_list=[]
label1_name=[]
label2_name=[]

sig_length = 1 # in seconds


with h5py.File(filename, 'r') as f:
    num_events = len(f['signal'])
    # find the sampling rate (assumed to be uniform across events)
    sr = f['sr'][0]
    
    for i in tqdm.tqdm(range(num_samples)):
        while True:
            #random assignment using rng.choice, numpy.random.Generator.choice
            indexes =rng.choice(num_events, 2, replace=False)
            ind1=indexes[0]
            ind2=indexes[1]

            #signal numpy array
            event1=f['signal'][ind1]
            event2=f['signal'][ind2]

            #making it the same length
            min_len = min(len(event1), len(event2))
            #print(min_len)
            if min_len > sig_length * sr:
                event1 = event1[:sig_length * sr]
                event2 = event2[:sig_length * sr]
                #generating overlapped audio file
                overlap=event1+event2
            
                signal_list.append(overlap)
                label1_name.append(f['label'][ind1])
                label2_name.append(f['label'][ind2])
                break
        
#print(len(signal_list))



hf = h5py.File('/om2/user//schen77/overlapping_dataset_test.h5', 'w')#get rid of t
signal_list=np.vstack(signal_list)
arr1 = signal_list
arr2 = label1_name
arr3 = label2_name

# Create a variable-length datatype for the dataset if signals are different length
#dtype = h5py.special_dtype(vlen=np.dtype('float32'))

# convert numpy.bytes_ to Python strings
str_list2 = [n.decode('utf-8', 'ignore') for n in arr2]
str_list3 = [n.decode('utf-8', 'ignore') for n in arr3]

# use the encode method
asciiList = [n.encode('ascii', 'ignore') for n in str_list2]
asciiList2 = [n.encode('ascii', 'ignore') for n in str_list3]

hfdat = hf.create_group('data')
hfdat.create_dataset('signal_list', data=arr1) #delete dtype=dtype if doesn't work
hfdat.create_dataset('event1_label', (len(asciiList),1),'S10', asciiList)
hfdat.create_dataset('event2_label', (len(asciiList2),1),'S10', asciiList2)

hf.close()

print(hf)



