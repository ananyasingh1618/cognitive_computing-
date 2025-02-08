import numpy as np
import matplotlib.pyplot as plt
image = np.random.randint(0, 256, size=(5, 5))
print("Grayscale Image:")
print(image)
sobel_filter = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])
filtered_image = np.dot(image[1:4, 1:4], sobel_filter)
print("Filtered Image:")
print(filtered_image)
normalized_image = (filtered_image - filtered_image.min()) / (filtered_image.max() - filtered_image.min()) * 255
normalized_image = normalized_image.astype(int)
print("Normalized Edge-Detected Image:")
print(normalized_image)
edge_strength = normalized_image.sum(axis=1)
strongest_edge_row = np.argmax(edge_strength)
print(f"Row with the strongest edge: {strongest_edge_row}")
plt.bar(range(len(edge_strength)), edge_strength)
plt.title("Edge Intensity Across Rows")
plt.xlabel("Row Number")
plt.ylabel("Edge Strength")
plt.show()