def convert_decimal_file_to_hex32(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line_num, line in enumerate(infile, 1):
            try:
                dec_value = int(line.strip())
                
                # Convert to 32-bit signed hex
                if dec_value < 0:
                    dec_value = (1 << 32) + dec_value  # Two's complement for negatives
                
                hex_str = format(dec_value, '08X')  # Uppercase 8-digit hex
                outfile.write(hex_str + '\n')

            except ValueError:
                print(f"Skipping invalid line {line_num}: {line.strip()}")

# === Example usage ===
input_filename = 'filtered_output1.txt'   # Your input file with decimal values
output_filename = 'signed_hex_output1.txt'     # Output file with hex values

convert_decimal_file_to_hex32(input_filename, output_filename)
