from scipy.signal import butter, lfilter, filtfilt
import numpy as np


def highpass_filter(data, cutoff, fs, order=4):
    pad_length = 15
    padded_signal = np.pad(data, pad_length)
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    filitered_sig = filtfilt(b, a, padded_signal)
    return filitered_sig[pad_length:-pad_length]


def lowpass_filter(data, cutoff, fs, order=4):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', output='ba')
    return lfilter(b, a, data)