from enum import IntEnum
from typing import Tuple, List

# IntEnum is implemented to make use of comparison operators
Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))

# a codon is defined as a group of 3 nucleotides
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]

# a gene is defined as multiple codons
Gene = List[Codon]

def string_to_gene(s: str) -> Gene:
  gene: Gene = []

  for i in range(0, len(s), 3):
    if (i+2) >= len(s):
      return gene
    codon: Codon = (Nucleotide[s[i]], Nucleotide[s[i +1]], Nucleotide[s[i +2]])
    gene.append(codon)
  return gene

def linear_contains(gene: Gene, key_codon: Codon) -> bool:
  """Linear Search Algo to find a Codon (sequence of 3 Nucleotides) in a given Gene

  :param Gene gene: Gene to search
  :param Codon key_codon: Condon to find
  :return: if the key is found in the gene
  :rtype: bool
  """
  for codon in gene:
    if codon == key_codon:
      return True
  return False

def binary_contains(gene: Gene, key_codon: Codon) -> bool:
  """Binary Search Algo to find a Codon (sequence of 3 Nucleotides) in a given Gene

  Assumes the Gene is pre-sorted.

  :param Gene gene: sorted Gene to search
  :param Codon key_codon: Condon to find
  :return: if the key is found in the gene
  :rtype: bool
  """
  low: int = 0
  high: int = len(gene) -1
  while low <= high:
    mid: int = (low + high) // 2
    if gene[mid] < key_codon:
      low = mid + 1
    elif gene[mid] > key_codon:
      high = mid - 1
    else:
      return True
  return False