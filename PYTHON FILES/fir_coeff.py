import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin


# -------------------------
# FIR Bandpass Filter Design
# -------------------------


def filter(lowcut,highcut):
    fs = 256          # Sampling frequency (Hz)
    num_taps = 64     # Number of filter taps (FIR length)

    coeffs = firwin(
    num_taps, 
    [lowcut, highcut], 
    pass_zero=False,     # Bandpass filter
    fs=fs,               
    window='hamming'     # Smooth transition, reduced ripple
    )

    return coeffs.astype(np.float16)

def save_filter_to_hex(filter, filename):
    # First scale
    
    # Clip to avoid overflow
    filter_clipped = np.clip(filter, -32768, 32767)

    # Round and convert
    filter_int16 = np.round(filter_clipped*(2**15-1)).astype(np.int16)

    # Convert each to 4-digit hex string
    hex_values = [format(x & 0xFFFF, '04X') for x in filter_int16]

    # Write to file
    with open(filename, "w") as f:
        for hex_val in hex_values:
            f.write(hex_val + "\n")

    print(f"Saved {filename} in 16-bit signed hex format.")

left= filter(8,15)
alpha_right = filter(7,17)
delta= filter(0.5,4)
beta= filter(13,30)
theta= filter(4,8)

# -------------------------
# Plot Impulse Response
# -------------------------
plt.figure(num= 1,figsize=(8, 4))
plt.stem(left, use_line_collection=True)
plt.title("FIR Filter Coefficients (Impulse Response) left")
plt.xlabel("Tap Index (n)")
plt.ylabel("Coefficient Value")
plt.grid(True)
plt.tight_layout()
plt.show(block = False)
#input("Press Enter to close all figures...")
np.set_printoptions(precision=6, suppress=True)
print("FIR Filter Coefficients (Floating Point):")
print(left)
print (len(left))

plt.figure(num= 2,figsize=(8, 4))
plt.stem(alpha_right, use_line_collection=True)
plt.title("FIR Filter Coefficients (Impulse Response) alpha right")
plt.xlabel("Tap Index (n)")
plt.ylabel("Coefficient Value")
plt.grid(True)
plt.tight_layout()
plt.show(block=False)
np.set_printoptions(precision=6, suppress=True)
print("FIR Filter Coefficients (Floating Point):")

plt.figure(num= 3,figsize=(8, 4))
plt.stem(delta, use_line_collection=True)
plt.title("FIR Filter Coefficients (Impulse Response) delta")
plt.xlabel("Tap Index (n)")
plt.ylabel("Coefficient Value")
plt.grid(True)
plt.tight_layout()
plt.show(block= False)
#input("Press Enter to close all figures...")
np.set_printoptions(precision=6, suppress=True)
print("FIR Filter Coefficients (Floating Point):")


plt.figure(num= 4,figsize=(8, 4))
plt.stem(theta, use_line_collection=True)
plt.title("FIR Filter Coefficients (Impulse Response) theta")
plt.xlabel("Tap Index (n)")
plt.ylabel("Coefficient Value")
plt.grid(True)
plt.tight_layout()
plt.show(block = False)
#input("Press Enter to close all figures...")
np.set_printoptions(precision=6, suppress=True)
print("FIR Filter Coefficients (Floating Point):")

plt.figure(num= 5,figsize=(8, 4))
plt.stem(beta, use_line_collection=True)
plt.title("FIR Filter Coefficients (Impulse Response) beta")
plt.xlabel("Tap Index (n)")
plt.ylabel("Coefficient Value")
plt.grid(True)
plt.tight_layout()
plt.show(block = False)
input("Press Enter to close all figures...")
np.set_printoptions(precision=6, suppress=True)
print("FIR Filter Coefficients (Floating Point):")



print("coeff of left")
print(left)
print (len(left))

print("coeff of alpha_right")
print(alpha_right)
print (len(alpha_right))

print("coeff of beta")
print(beta)
print (len(beta))

print("coeff of delta")

print(delta)
print (len(delta))

print("coeff of theta")
print(theta)
print (len(theta))

save_filter_to_hex(left, "alpha.txt")
save_filter_to_hex(alpha_right,"alpha_right.txt")

save_filter_to_hex(delta, "delta.txt")
save_filter_to_hex(beta, "beta.txt")
save_filter_to_hex(theta, "theta.txt")