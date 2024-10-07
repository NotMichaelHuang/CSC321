import matplotlib.pyplot as plt

# Data
key_sizes = [512, 1024, 2048, 3072, 4096, 7680, 15360]
throughput = [288705.4, 113830, 33483.8, 15364.8, 8821.4, 2574.3, 643.4]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(key_sizes, throughput, marker='o', linestyle='-', color='b', label='Throughput')

# Labels and Title
plt.xlabel('Key Size (bits)')
plt.ylabel('Throughput (operations per second)')
plt.title('RSA Key Size vs Throughput')
plt.grid(True)
plt.legend()

# Show Plot
plt.show()

