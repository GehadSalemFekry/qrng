import numpy as np
from scipy.linalg import toeplitz
import hashlib

def read_and_filter_data(file_path):
    quantum_data = []
    classical_data = []

    with open(file_path, "r") as file:
        for line in file:
            clean_line = line.strip()
            if clean_line:
                data, label = clean_line.split()
                data_array = np.array([int(bit) for bit in data])
    
                if label == "1":
                    quantum_data.append(data_array)
                elif label == "2":
                    classical_data.append(data_array)
    
    return np.concatenate(quantum_data), np.concatenate(classical_data)

def apply_toeplitz_matrix(data, size):
    matrix = toeplitz(np.random.randint(0, 2, size=size))
    
    if len(data) % size != 0:
        padding = size - (len(data) % size)
        data = np.append(data, np.zeros(padding))
    
    data_matrix = np.array(data).reshape(-1, size)
    transformed_data = np.dot(data_matrix, matrix) % 2
    return transformed_data.flatten()

def calculate_entropy(data):
    if len(data) == 0:
        return 0

    data = np.array(data, dtype=int)
    probabilities = np.bincount(data) / len(data)
    entropy = -np.sum([p * np.log2(p) for p in probabilities if p > 0])
    return entropy

def hash_data(data, hash_function='sha256'):
    data_str = ''.join(map(str, data))
    hasher = hashlib.new(hash_function)
    hasher.update(data_str.encode())
    return np.array(list(map(int, format(int(hasher.hexdigest(), 16), 'b').zfill(hasher.digest_size * 8))), dtype=int)

file_path = "GeneratedRandomBits.txt"

quantum_data, classical_data = read_and_filter_data(file_path)

quantum_processed = apply_toeplitz_matrix(quantum_data, size=64)
classical_processed = apply_toeplitz_matrix(classical_data, size=64)

quantum_entropy = calculate_entropy(quantum_processed)
print("Entropy of Processed Quantum Data:", quantum_entropy)

classical_entropy = calculate_entropy(classical_processed)
print("Entropy of Processed Classical Data:", classical_entropy)

quantum_hash = hash_data(quantum_processed)
print("Hash of Processed Quantum Data:", quantum_hash)

classical_hash = hash_data(classical_processed)
print("Hash of Processed Classical Data:", classical_hash)

