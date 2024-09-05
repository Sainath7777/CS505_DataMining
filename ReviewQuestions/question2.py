import numpy as np
import cProfile

def main():
    # I. Create the list
    my_list = [1225, 4986, 6789, 7890, 2345, 6783, 0987, 1234, 8765, 3456]

    # II. Iterate using a for loop
    print("II. Iterating using a for loop:")
    for item in my_list:
        print(item)

    # III. Iterate using for loop and range
    print("\nIII. Iterating using for loop and range:")
    for i in range(len(my_list)):
        print(f"Index {i}: {my_list[i]}")

    # IV. List Comprehension
    squared_list = [x**2 for x in my_list]  # Create a new list with squared values
    print("\nIV. List after squaring each element (using list comprehension):", squared_list)

    # V. Enumerate
    print("\nV. Using enumerate:")
    for index, value in enumerate(my_list):
        print(f"Index {index}: {value}")

    # VI. Iter function and next function
    print("\nVI. Using iter() and next():")
    iter_list = iter(my_list)  # Create an iterator object
    for _ in range(len(my_list)):
        print(next(iter_list))  # Get next item from iterator

    # VII. Map function
    def double(x):
        return x * 2

    doubled_list = list(map(double, my_list))  # Apply double function to each element
    print("\nVII. List after doubling each element (using map()):", doubled_list)

    # VIII. Using zip
    list1 = [1, 2, 3, 4, 5]
    list2 = ['a', 'b', 'c', 'd', 'e']
    zipped = list(zip(list1, list2))  # Combine elements from both lists
    print("\nVIII. Zipped lists:", zipped)

    # IX. Using NumPy Module
    np_array = np.array(my_list)  # Convert list to NumPy array
    print("\nIX. NumPy array:", np_array)
    print("Mean of the array:", np.mean(np_array))
    print("Standard deviation of the array:", np.std(np_array))

# Run the main function with profiling
cProfile.run('main()')
