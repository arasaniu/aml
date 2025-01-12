import matplotlib.pyplot as plt

def plot_signal(signal, name, time_steps=2000, color="b"):
    plt.clf()
    plt.figure(figsize=(20,5))
    plt.plot(signal[:time_steps], label=name, color=color)
    plt.title(name)
    plt.show()
    plt.clf()