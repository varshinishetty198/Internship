import numpy as np
data = np.arange(24)
reshaped = data.reshape(4, 3, 2)
final_array = reshaped.transpose(0, 2, 1)
print("Final Shape:", final_array.shape)
print("\nFinal Array:\n", final_array)
