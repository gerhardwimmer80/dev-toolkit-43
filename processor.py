import numpy as np

def process_data(data):
    array_data = np.array(data)
    mean = np.mean(array_data)
    std_dev = np.std(array_data)
    processed = (array_data - mean) / std_dev
    return processed


def optimize_and_process(data, threshold):
    if len(data) > threshold:
        processed = process_data(data)
        return processed[processed > 0]
    return np.array([])


def main():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    threshold = 5
    optimized_data = optimize_and_process(data, threshold)
    print(optimized_data)

if __name__ == "__main__":
    main()