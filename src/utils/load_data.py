import numpy as np

def load_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.readlines()
            data_array = [float(line.strip()) for line in data]
            data_array = np.array(data_array)
            data_array = (data_array - np.mean(data_array)) / np.std(data_array)
            return data_array
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
        return None