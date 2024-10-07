import matplotlib.pyplot as plt

# Data
block_sizes = [16, 64, 256, 1024, 8192, 16384]
aes_128 = [248550960, 256160150, 251796650, 256675020, 258662400, 258834430]
aes_192 = [213777010, 220836790, 216840790, 221059070, 222431910, 222494720]
aes_256 = [189141900, 192781800, 191810870, 194161660, 194486270, 195056980]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(block_sizes, aes_128, marker='o', label='AES-128 CBC')
plt.plot(block_sizes, aes_192, marker='o', label='AES-192 CBC')
plt.plot(block_sizes, aes_256, marker='o', label='AES-256 CBC')

# Labels and Title
plt.xlabel('Block Size (Bytes)')
plt.ylabel('Throughput')
plt.title('AES CBC Mode Performance Comparison')
plt.legend()
plt.grid(True)

# Show Plot
plt.show()
