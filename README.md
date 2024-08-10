# Quantum Random Number Generator (QRNG) Project

This project aims to create and analyze a Quantum Random Number Generator (QRNG) for Webfest 2024, preprocess the data to enhance its entropy, and evaluate it against classical and true random number generators. The project is divided into several stages, each focusing on different aspects of the QRNG workflow.

## Stages Overview

### **Stage 1: Implementing a QRNG on IBM QPUs**
- **File:** [`Qiskit_Superposition_QRNG.ipynb`](Qiskit_Superposition_QRNG.ipynb)
- **Description:** This stage involves implementing a quantum random number generator using IBM’s quantum processors (QPU). The notebook contains the code for generating quantum random bits.

### **Stage 2: Achieving High Accuracy with Classification Models**
- **Files:** 
  - [`QRNG_Classifier_GBModel_final.ipynb`](QRNG_Classifier_GBModel_final.ipynb)
  - [`QRNGvsPRNG_TrainingData.txt`](QRNGvsPRNG_TrainingData.txt)
- **Description:** This stage focuses on classifying QRNG data against pseudorandom number generator (PRNG) data using machine learning models. The provided notebook includes the classifier models, evaluation metrics, and performance benchmarks.

### **Stage 3: Measuring Entropy and Real-world Implementation**
- **Files:**
  - [`stage3.ipynb`](stage3.ipynb)
  - [`visualization_analysis.ipynb`](visualization_analysis.ipynb)
- **Description:** Evaluate the entropy of quantum random numbers and compare them with classical pseudorandom number generators (PRNG) and true random number generators (TRNG). The stage also includes implementing QRNG data in a real-world application and analyzing the results.

### **Stage 4: Pre-processing and Post-processing for High Entropy**
- **File:** [`pre-post-processing.py`](pre-post-processing.py)
- **Description:** Deploy pre-processing and post-processing techniques to enhance the entropy of the generated quantum random numbers. This includes cleaning the data, applying a Toeplitz matrix transformation, and running statistical tests to ensure high entropy.

### **Stage 5: True Random Number Generator (TRNG)**
- **File:** [`trng.ipynb`](trng.ipynb)
- **Description:** Create and implement a True Random Number Generator based on physical entropy sources. The notebook demonstrates how to generate and validate true random numbers.

## Data Files
- **[`GeneratedRandomBits.txt`](GeneratedRandomBits.txt):** This file contains generated quantum random data used in various stages of the project.
- **[`QRNGvsPRNG_TrainingData.txt`](QRNGvsPRNG_TrainingData.txt):** Initial training data for classification models.

## Instructions

1. **Setup and Dependencies:**
   - Ensure you have the necessary libraries and dependencies installed. You may need `Qiskit`, `numpy`, `scipy`, `sklearn`, and other relevant libraries.

2. **Run the Notebooks:**
   - Start with `Qiskit_Superposition_QRNG.ipynb` to generate quantum random numbers.
   - Use `QRNG_Classifier_GBModel_final.ipynb` to classify the data and evaluate the performance of classification models.
   - Proceed to `stage3.ipynb` for entropy measurement and real-world application of QRNG data.
   - Apply preprocessing and post-processing techniques using `pre-post-processing.py`.
   - Finally, explore `trng.ipynb` to create and validate a True Random Number Generator.

3. **Analyze Results:**
   - Use `visualization_analysis.ipynb` to visualize and analyze the results from different stages.

## Contact
For any questions or further information, please contact authors .

