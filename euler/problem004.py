#!/usr/bin/env python3

import argparse
import sys
import time


def reverse(n: int, verbose: bool = False) -> int:
    sign = -1 if n < 0 else 1
    n_abs = abs(n)
    reversed_str = str(n_abs)[::-1]
    reversed_int = int(reversed_str)
    return sign * reversed_int


def isPalindrome(n: int) -> int:
    return n == reverse(n)


def solve(n: int, verbose: bool = False) -> int:
    """
    Implement the core Project Euler logic here.

    Parameters:
        n (int): the input value for the problem.
        verbose (bool): if True, print intermediate steps or reasoning.

    Returns:
        int: the final solution.
    """
    lower: int = 10 ** (n - 1)
    upper: int = (10**n) - 1

    if verbose:
        print(f"Solving for a {n} digit number. From {lower} to {upper}")

    largestPalindrome = 0
    a = upper
    while a >= lower:
        b = upper
        while b >= a:
            if a * b <= largestPalindrome:
                break
            if isPalindrome(a * b):
                largestPalindrome = a * b
            b -= 1
        a -= 1

    result = largestPalindrome
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
