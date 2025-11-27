import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fs = 256  # Sampling frequency (Hz)
t = np.arange(0, 1, 1/fs)  # 1 second worth of time points (256 samples)

def generate_eeg(freqs, amps, noise_level=100):
    signal = sum(a * np.sin(2 * np.pi * f * t) for f, a in zip(freqs, amps))
    noise = noise_level * np.random.randn(len(t))
    return signal + noise


def save_eeg_to_hex(eeg_signal, filename):
   
    # Normalize to [-1, 1]
    eeg_int16 = np.clip(eeg_signal, -32768, 32767)
    
    # Convert to signed 16-bit integers
    eeg_int16 = np.round(eeg_signal * (2**15 - 1)).astype(np.int16)
    
    # Convert each to 4-digit hex string (2's complement)
    hex_values = [format(x & 0xFFFF, '04X') for x in eeg_int16]

    # Write to file
    with open(filename, "w") as f:
        for hex_val in hex_values:
            f.write(hex_val + "\n")

    print(f"Saved {filename} in 16-bit signed hex format.")

# Simulated EEG classes
eeg_data = {
  # eeg_data = {
    "left": generate_eeg([2, 6, 10, 20, 40], [100, 200, 600, 1000, 100]),
    "right": generate_eeg([2, 6, 11, 22, 45], [100, 200, 600, 1000, 100]),
    "move": generate_eeg([2, 6, 9, 25, 60], [50, 100, 100, 1200, 500]),
    "idle": generate_eeg([1, 5, 10, 14, 35], [300, 400, 800, 100, 50])


}

# # Save each class to a separate CSV
# for label, data in eeg_data.items():
#     df = pd.DataFrame(data)
#     df.to_csv(f"eeg_{label}.csv", index=False)
#     print(f"Saved eeg_{label}.csv")



save_eeg_to_hex(eeg_data["left"], "eeg_left_hex.txt")
save_eeg_to_hex(eeg_data["right"], "eeg_right_hex.txt")
save_eeg_to_hex(eeg_data["move"], "eeg_move_hex.txt")
save_eeg_to_hex(eeg_data["idle"], "eeg_idle_hex.txt")



# Plot one example (Left Imagery)
plt.figure()

plt.subplot(2,2,1)
plt.plot(t, eeg_data["left"])
plt.title("Synthetic EEG - Left Imagery")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(2,2,2)
plt.plot(t, eeg_data["right"])
plt.title("Synthetic EEG - right Imagery")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(2,2,3)
plt.plot(t, eeg_data["move"])
plt.title("Synthetic EEG - focus(move) Imagery")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(2,2,4)
plt.plot(t, eeg_data["idle"])
plt.title("Synthetic EEG - idle Imagery")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()

plt.tight_layout()
plt.show()
