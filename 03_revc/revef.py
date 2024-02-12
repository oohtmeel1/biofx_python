#!/usr/bin/env python3
"""
Author : Anonymous <Anonymous@localhost>
Date   : 2024-02-08
Purpose: Using List comprehensions
"""

import argparse
import os
from typing import NamedTuple


class Args(NamedTuple):
    """ Command-line arguments """
    dna: str


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Print the reverse complement of DNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('dna', metavar='DNA', help='Input sequence or file')

    args = parser.parse_args()

    if os.path.isfile(args.dna):
        args.dna = open(args.dna).read().rstrip()

    return Args(args.dna)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """
    args=get_args()
    trans ={'A':'T','C':'G','G':'C','T':'A','a':'t','c':'g','t':'a','g':'c'}
    complement = [trans.get(base,base) for base in args.dna]
    print(''.join(reversed(complement)))

# --------------------------------------------------
if __name__ == '__main__':
    main()
