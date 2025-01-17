#!/usr/bin/env python3
"""
Author : Anonymous <Anonymous@localhost>
Date   : 2024-02-21
Purpose: Compute GC content
"""

import argparse
from typing import NamedTuple, TextIO ,List, Tuple
import sys
from Bio import SeqIO

class Args(NamedTuple):
    """ Command-line arguments """
    file: TextIO


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Compute GC content',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='?',
                        default=sys.stdin,
                        help='Input File Sequence')

    args = parser.parse_args()

    return Args(args.file)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """
    args=get_args()
    seqs : List[Tuple[float, str]] = []
    
    for rec in SeqIO.parse(args.file,'fasta'):
        gc = 0
        for base in rec.seq.upper():
            if base in ('C','G'):
                gc +=1
        pct = (gc *100) / len(rec.seq)
        seqs.append((pct,rec.id))
        
    high = max(seqs)
    print(f'{high[1]} {high[0]:0.6f}')    


# --------------------------------------------------
if __name__ == '__main__':
    main()