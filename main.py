import numpy as np
from tqdm import tqdm

def generate_data(data_low: int, data_upper: int, range_lower_bound: int, range_upper_bound: int, data_size: int):
    output = []
    for i in range(data_size):
        len = np.random.randint(range_lower_bound, range_upper_bound)
        unsort = np.random.randint(data_low, data_upper, len)
        sorted = np.sort(unsort)
        output.append(np.asarray([unsort, sorted]))
    return output

print(generate_data(-100, 100, 10, 20, 10))