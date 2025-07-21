#!/usr/bin/env python3

import argparse
import sys
import time
from math import prod
from typing import Generator

BIG_NUMBER = (
    "73167176531330624919225119674426574742355349194934969835203127745063"
    "262395783180169848018694788518438586156078911294949545950173795833195"
    "285320880551112540698747158523863050715693290963295227443043557668966"
    "489504452445231617318564030987111217223831136222989342338030813533627"
    "661428280644448664523874930358907296290491560440772390713810515859307"
    "960866701724271218839987979087922749219016997208809377665727333001053"
    "367881220235421809751254540594752243525849077116705560136048395864467"
    "063244157221553975369781797784617406495514929086256932197846862248283"
    "972241375657056057490261407972968652414535100474821663704844031998900"
    "088952434506585412275886668811642717147992444292823086346567481391912"
    "316282458617866458359124566529476545682848912883142607690042242190226"
    "710556263211111093705442175069416589604080719840385096245544436298123"
    "098787992724428490918884580156166097919133875499200524063689912560717"
    "606058861164671094050775410022569831552000559357297257163626956188267"
    "0428252483600823257530420752963450"
)


def get_slices(s: str, size: int, drop_zeroes: bool = False) -> Generator[str]:
    for i in range(len(s) - size + 1):
        slice = s[i : i + size]
        if drop_zeroes and "0" in slice:
            continue
        yield slice


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

    slices = get_slices(BIG_NUMBER, n, drop_zeroes=True)
    result = max(prod(map(int, elem)) for elem in slices)

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
