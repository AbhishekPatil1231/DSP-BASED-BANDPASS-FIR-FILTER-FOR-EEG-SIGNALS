import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 64
half_N = N // 2

# Load FIR coefficients from hex file
def load_coefficients(filename):
    with open(filename, 'r') as f:
        hex_vals = f.read().split()
    return np.array([int(x, 16) if int(x, 16) < 0x8000 else int(x, 16) - 0x10000 for x in hex_vals], dtype=np.int16)

# Load EEG input samples from text file
# Load EEG input samples stored in HEX format (16-bit signed)
def load_eeg_samples(filename):
    with open(filename, 'r') as f:
        content = f.read().split()
    return np.array([int(val, 16) if int(val, 16) < 0x8000 else int(val, 16) - 0x10000 for val in content],dtype=np.int16)


# FIR filter class
class SymmetricFIRFilter:
    def __init__(self, h_file):
        self.h = load_coefficients(h_file)
        self.x = [0] * N

    def reset(self):
        self.x = [0] * N

    def step(self, eeg_sample):
        for i in range(N - 1, 0, -1):
            self.x[i] = self.x[i - 1]
        self.x[0] = eeg_sample

        temp_sum = 0
        for i in range(half_N):
            temp_sum += int(self.h[i]) * (int(self.x[i]) + int(self.x[N - 1 - i]))

        return np.int32(temp_sum)

# MAIN
if __name__ == "__main__":
    fir = SymmetricFIRFilter("alpha.txt")
    fir.reset()

    eeg_signal = load_eeg_samples("eeg_left_hex.txt")
    outputs = []

    for sample in eeg_signal:
        y = fir.step(sample)
        outputs.append(y)

    # Save output to text file
    with open("filtered_output1.txt", "w") as f:
        for val in outputs:
            f.write(f"{val}\n")

    # Plot output
    plt.figure(figsize=(12, 5))
    plt.plot(outputs, label="Filtered EEG", color='blue')
    plt.title("FIR Filtered EEG Output")
    plt.xlabel("Sample Index")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("filtered_output_plot.png")  # Save plot as PNG
    plt.show()