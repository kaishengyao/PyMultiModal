import numpy as np

def chunk_mean_power(chunk):
    data = [int(k) for k in chunk]
    data_mean = np.mean(data)
    data_eng  = np.mean([(k - data_mean)**2 for k in data])

