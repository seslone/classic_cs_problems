from classic_cs_problems.chapter_2.dna_search import (
  Nucleotide,
  string_to_gene,
  linear_contains,
  binary_contains
)

class TestDNASearch:
  SIMPLE_GENE_STR = "ACGT"
  GENE_STR: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"

  def test_linear_contains(self):
    assert linear_contains(string_to_gene(self.SIMPLE_GENE_STR), (Nucleotide.A, Nucleotide.C, Nucleotide.G))
    assert linear_contains(string_to_gene(self.GENE_STR), (Nucleotide.G, Nucleotide.G, Nucleotide.G))

  def test_binary_contains(self):
    gene = string_to_gene(self.GENE_STR)
    gene.sort()
    assert binary_contains(gene, (Nucleotide.G, Nucleotide.G, Nucleotide.G))
