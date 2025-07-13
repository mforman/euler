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

    lastFactor = None

    if n % 2 == 0:
        if verbose:
            print(f"{n} is divisible by 2. Setting lastFactor = 2")
        n = n // 2
        lastFactor = 2
        while n % 2 == 0:
            n = n // 2
    else:
        lastFactor = 1

    factor = 3
    while n > 1:
        if n % factor == 0:
            n = n // factor
            lastFactor = factor
            if verbose:
                print(f"{n*lastFactor} is divisible by {lastFactor}. Setting n = {n}")
            while n % factor == 0:
                n = n // factor
        factor = factor + 2

    result = lastFactor

    if verbose:
        print(f"Computed result: {result}")

    return result


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
