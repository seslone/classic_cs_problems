# this naive recursion method runs exponentially and can quickly exhaust the call stack
def fib1(n: int) -> int:
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


# print(fib(7))


# A better method would cache the preious values of the function
# so that subsequent calls do not always recaluculate
from typing import Dict

memo: Dict[int, int] = {0: 0, 1: 1}  # our base cases


def fib2(n: int) -> int:
    if n not in memo:
        memo[n] = fib2(n - 1) + fib2(n - 2)  # memoization
    return memo[n]


# print(fib2(50))

# The cache can be handled with the below decorator instead of explicitly.
from functools import lru_cache


@lru_cache(maxsize=None)
def fib3(n: int) -> int:
    if n < 2:
        return n
    return fib3(n - 2) + fib3(n - 1)


# print(fib3(50))

# Best implementation - the loop will only ever run in O(n) with one call to the function
def fib4(n: int) -> int:
    if n == 0:
        return n
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
    return next


# print(fib4(50))

# Implementation that creates the full list of fibonacci numbers
from typing import Generator


def fib5(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0:
        yield 1
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next


# for i in fib5(50):
#     print(i)


# My own implementation to create the list of fib nums
from typing import List


def fib(n: int) -> List[int]:
    if n <= 0:
        raise ValueError("This function can only take non-zero positive integers.")
    fib_nums = [None] * (n + 1)
    fib_nums[0] = 0
    fib_nums[1] = 1
    for i in range(2, n + 1):
        fib_nums[i] = fib_nums[i - 1] + fib_nums[i - 2]
    return fib_nums


# print(fib(2))
