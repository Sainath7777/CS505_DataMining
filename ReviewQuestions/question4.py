from itertools import combinations, permutations
import cProfile

def main():
    # Define lists A, B, C, D, E
    A = [1, 2, 3]
    B = ['a', 'b', 'c']
    C = [True, False]
    D = [3.14, 2.71]
    E = ['x', 'y']

    all_lists = [A, B, C, D, E]

# Compute combinations using itertools (same as above, demonstrating itertools usage)
    print("\nCombinations using itertools:")
    for i, lst in enumerate(all_lists):
        print(f"\nCombinations for list {chr(65+i)}:")
        for r in range(1, len(lst) + 1):
            combs = list(combinations(lst, r))
            print(f"  {r}-combinations: {combs}")

    # Compute permutations using itertools (same as above, demonstrating itertools usage)
    print("\nPermutations using itertools:")
    for i, lst in enumerate(all_lists):
        print(f"\nPermutations for list {chr(65+i)}:")
        perms = list(permutations(lst))
        print(f"  All permutations: {perms}")

# Run the main function with profiling
cProfile.run('main()')

