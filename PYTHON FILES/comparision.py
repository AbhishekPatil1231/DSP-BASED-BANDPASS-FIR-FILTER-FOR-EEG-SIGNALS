
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

def load_signal(filename, is_hex=False, bit_width=32):
    with open(filename, 'r') as f:
        content = f.read().split()

    if is_hex:
        max_val = 1 << bit_width
        sign_bit = 1 << (bit_width - 1)
        data = []
        for x in content:
            val = int(x, 16)
            if val >= sign_bit:
                val -= max_val
            data.append(val)
        return np.array(data, dtype=np.int64)  # Use int64 to avoid overflow
    else:
        return np.array([int(x) for x in content], dtype=np.int32)



# Main comparison and plotting
def compare_signals(file1, file2, is_hex1=True, is_hex2=True,fir_taps =64):
    signal1 = load_signal(file1, is_hex1)
    signal2 = load_signal(file2, is_hex2)
    signal1 = signal1 / (2**31)
    signal2 = signal2 / (2**31)

    '''delay = (fir_taps - 1) // 2
    signal1 = signal1[:len(signal1)-delay]        # trim reference
    signal2 = signal2[delay:]'''


    # Truncate to shortest length
    min_len = min(len(signal1), len(signal2))
    signal1 = signal1[:min_len]
    signal2 = signal2[:min_len]

    # Compute MSE
    mse = mean_squared_error(signal1, signal2)

     # Compute PSNR 
    max_val = 1.0  # Because signals are normalized between -1 and 1
    if mse == 0:
        psnr = float('inf')
    else:
        psnr = 10 * np.log10(max_val**2 / mse)

    # Plot
    plt.figure(figsize=(12, 5))
    plt.plot(signal1, label="Signal 1 expected output ", color='blue')
    plt.plot(signal2, label="Signal 2 verilog output", color='red')
    plt.title(f"Signal Comparison (MSE = {mse:.7f}) (PSNR: {psnr:.2f} dB)")
    plt.xlabel("Sample Index")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("signal_comparison_plot.png")
    plt.show()
    

    print(f"\n Mean Squared Error (MSE): {mse:.7f}")
    
    print("Expected: min =", np.min(signal1), "max = ", np.max(signal1))
    print("Verilog : min =", np.min(signal2),  "max =", np.max(signal2))
    max_abs_diff = np.max(np.abs(signal1 - signal2))
    print(f"Max absolute error: {max_abs_diff:.5f}")
    print(f"PSNR: {psnr:.2f} dB")



# Example usage

compare_signals("signed_hex_output1.txt","output.txt", is_hex1=True, is_hex2=True)