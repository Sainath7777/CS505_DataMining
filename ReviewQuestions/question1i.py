# Function to subtract two matrices
def matrix_subtract(A, B):
    # Similar to addition, but with subtraction operator
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Function to multiply two matrices
def matrix_multiply(A, B):
    # Use nested list comprehensions and zip function for matrix multiplication
    return [[sum(a*b for a,b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]

def main():
    # Define matrices A, B, and C
    A = [[3.7827, 3.3454, 3.2341], [2.2122, 3.5678, 3.9087], [1.1234, 2.8934, 5.9087]]
    B = [[3.1234, 3.0987, 3.1234], [2.1111, 3.2222, 3.3333], [1.0987, 1.3456, 5.1234]]
    C = [[3.1243, 3.0989, 3.1256], [2.6721, 3.6785, 3.9017], [1.1254, 2.8956, 5.9187]]

    # Perform matrix operations
    add_result = matrix_add(A, B)
    subtract_result = matrix_subtract(A, B)
    multiply_result = matrix_multiply(A, B)

    # Print results
    print("A + B =", add_result)
    print("A - B =", subtract_result)
    print("A * B =", multiply_result)

# Run the main function with profiling
cProfile.run('main()')
