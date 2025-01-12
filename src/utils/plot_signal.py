import matplotlib.pyplot as plt
import numpy as np


def plot_signal(signal, name, time_steps=2000):
    # plt.clf()
    plt.figure(figsize=(20,5))
    plt.xticks(np.arange(0, time_steps + 1, 200))
    plt.plot(signal[:time_steps], label=name)
    plt.title(name)
    plt.legend()
    plt.show()
    # plt.clf()


def plot_signals(signals, names, time_steps=2000):
    # plt.clf()
    plt.figure(figsize=(20,5))
    plt.xticks(np.arange(0, time_steps + 1, 200))
    for signal, name in zip(signals, names):
        plt.plot(signal[:time_steps], label=name)
    plt.title('Signals')
    plt.legend()
    plt.show()
    # plt.clf(