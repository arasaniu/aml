from scipy.signal import butter, lfilter, filtfilt
import numpy as np


def highpass_filter(data, cutoff, fs, order=4, flatten=True):
    pad_length = 15

    # Ensure `data` is 1D before padding
    if len(data.shape) > 1 and flatten:
        data = data.values.flatten()  # Flatten to 1D if necessary

    # Apply padding
    padded_signal = np.pad(data, pad_length)

    # Design high-pass filter
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='high', analog=False)

    # Filter the signal
    filtered_sig = filtfilt(b, a, padded_signal)

    # Return the signal with padding removed
    return filtered_sig[pad_length:-pad_length]


def lowpass_filter(data, cutoff, fs, order=4):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', output='ba')
    return lfilter(b, a, data)