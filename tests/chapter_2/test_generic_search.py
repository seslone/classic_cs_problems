from  classic_cs_problems.chapter_2.generic_search import (
  Comparable,
  binary_contains,
  linear_contains
)

def test_linear_contains_numeric():
  assert linear_contains([1, 5, 15, 15, 15, 15, 20], 5)


def test_binary_contains_numeric():
  assert binary_contains([1, 5, 15, 15, 15, 15, 20], 5)


def test_binary_contains_string():
  assert binary_contains(["a", "d", "e", "f", "z"], "f")


def test_binary_contains_string_null_case():
  assert not binary_contains(["john", "mark", "ronald", "sarah"], "sheila")
