import numpy as np
from tqdm import tqdm

def generate_data(data_low: int, data_upper: int, range_lower_bound: int, range_upper_bound: int, data_size: int):
    output = []
    for i in range(data_size):
        len = np.random.randint(range_lower_bound, range_upper_bound)
        unsort = np.random.randint(data_low, data_upper, len)[:,np.newaxis]
        sorted = np.sort(unsort)
        output.append((unsort, sorted))
    return output

data = generate_data(-100, 100, 10, 20, 1000)


weights = []
network = []

def init_weights(layer_config: list):
    for i in range(len(layer_config)-1):
        weights.append(np.random.randn(layer_config[i], layer_config[i + 1]))
    for i in range(len(layer_config)):
        network.append(np.zeros(layer_config[i]))

init_weights([1,4,4,1])
for i in weights:
    print(i.shape)
    
for epoch, (train,test) in enumerate(data):
    network[0] = train
    for ind, val in enumerate(weights):
        network[ind + 1] = np.tanh(np.dot(network[ind], val))