from __future__ import annotations
from typing import TypeVar, Iterable, Sequence, Generic, List, Callable, Set, Deque, Dict, Any, Optional
from typing_extensions import Protocol
from heapq import heappush, heappop

T = TypeVar('T')
C = TypeVar('C', bound='Comparable')


def Comparable(Protocol):
  def __eq__(self, other: Any) -> bool:
    ...

  def __lt__(self: C, other: C) -> bool:
    ...

  def __gt__(self: C, other: C) -> bool:
    return (not self < other) and self != other

  def __le__(self: C, other: C) -> bool:
    return self < other or self == other

  def __ge__(self: C, other: C) -> bool:
    return not self < other


class Node(Generic[T]):
  def __init__(self, state: T, parent: Optional[Node], cost: float = 0.0, heuristic: float = 0.0) -> None:
    self.state: T = state
    self.parent: Optional[Node] = parent
    self.cost: float = cost
    self.heuristic: float = heuristic

  def __lt__(self, other: Node) -> bool:
    return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def linear_contains(iterable: Iterable[T], key: T) -> bool:
  for item in iterable:
    if item == key:
      return True
  return False

def binary_contains(sequence: Sequence[C], key: C) -> bool:
  low: int = 0
  high: int = len(sequence) - 1
  while low <= high:
    mid: int = (low + high) // 2
    if sequence[mid] < key:
      low = mid + 1
    elif sequence[mid] > key:
      high = mid - 1
    else:
      return True
  return False


def dfs():
  pass


def bfs():
  pass


def node_to_path():
  pass


def astar():
  pass