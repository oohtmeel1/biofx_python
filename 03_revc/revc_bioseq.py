#!/usr/bin/env python3
"""
Author : Anonymous <Anonymous@localhost>
Date   : 2024-02-08
Purpose: Rock the Casbah
"""

import argparse
import os
from typing import NamedTuple
from Bio import Seq

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
    
    print(Seq.reverse_complement(args.dna))


# --------------------------------------------------
if __name__ == '__main__':
    main()