#!/usr/bin/env python3

import argparse
import sys
import time
from math import gcd


def find_pythagorean_triplet_with_sum(total, verbose: bool = False) -> int:  # type: ignore
    for m in range(2, int(total**0.5)):
        for n in range(1, m):
            if (m - n) % 2 == 1 and gcd(m, n) == 1:  # ensures primitive triplet
                k = total // (2 * m * (m + n))
                if total % (2 * m * (m + n)) == 0:
                    a = k * (m**2 - n**2)
                    b = k * (2 * m * n)
                    c = k * (m**2 + n**2)
                    if verbose:
                        print(f"a: {a} b: {b} c: {c}")
                    return a * b * c


def solve_brute_force(n: int, verbose: bool = False) -> int:  # type: ignore
    for a in range(1, n):
        for b in range(a + 1, n - a):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                if verbose:
                    print(f"a={a}, b={b}, c={c}")
                    print(f"Product abc = {a * b * c}")
                return a * b * c


def solve(n: int, verbose: bool = False) -> int:  # type: ignore
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

    return find_pythagorean_triplet_with_sum(n, verbose)


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
