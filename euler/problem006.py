#!/usr/bin/env python3

import argparse
import sys
import time


def solve(n: int, verbose: bool = False) -> int:
    """
    Implement the core Project Euler logic here.

    Parameters:
        n (int): the input value for the problem.
        verbose (bool): if True, print intermediate steps or reasoning.

    Returns:
        int: the final solution.
    """
    if verbose:
        print(f"Solving problem for n = {n}")

    sum_of_squares = sum([i**2 for i in range(1, n + 1)])
    squared_sum = sum(i for i in range(1, n + 1)) ** 2

    if verbose:
        print(f"Sum of squares: {sum_of_squares}")
        print(f"Squared sum {squared_sum}")

    return squared_sum - sum_of_squares


def main():
    parser = argparse.ArgumentParser(description="Project Euler problem solver")
    parser.add_argument("n", type=int, nargs="?", help="Input value for the problem (e.g., limit, nth term, etc.)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    if args.n is not None:
        n = args.n
    else:
        try:
            n = int(input("Enter the input value (e.g., limit, nth term): ").strip())
        except ValueError:
            print("Invalid input. Please enter an integer.")
            sys.exit(1)

    start = time.time()
    result = solve(n, verbose=args.verbose)
    duration = time.time() - start

    print(f"Result: {result}")
    print(f"Time taken: {duration:.6f} seconds")


if __name__ == "__main__":
    main()
