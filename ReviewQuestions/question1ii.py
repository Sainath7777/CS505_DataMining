import numpy as np
import cProfile

def main():
    # Define matrices A, B, and C using NumPy arrays
    A = np.array([[3.7827, 3.3454, 3.2341], [2.2122, 3.5678, 3.9087], [1.1234, 2.8934, 5.9087]])
    B = np.array([[3.1234, 3.0987, 3.1234], [2.1111, 3.2222, 3.3333], [1.0987, 1.3456, 5.1234]])
    C = np.array([[3.1243, 3.0989, 3.1256], [2.6721, 3.6785, 3.9017], [1.1254, 2.8956, 5.9187]])

    # Perform matrix operations using NumPy functions
    add_result = np.add(A, B)  # Element-wise addition
    subtract_result = np.subtract(A, B)  # Element-wise subtraction
    multiply_result = np.dot(A, B)  # Matrix multiplication

    # Print results
    print("A + B =", add_result)
    print("A - B =", subtract_result)
    print("A * B =", multiply_result)

# Run the main function with profiling
cProfile.run('main()')
