def calculate_pi(n_terms: int) -> float:
    numerator: float = 4.0
    denominator: float = 1.0
    operation: float = 1.0
    pi: float = 0.0
    for _ in range(n_terms):
        pi += operation * (numerator / denominator)
        operation *= -1
        denominator += 2
    return pi


print(calculate_pi(5))
print(calculate_pi(10))
print(calculate_pi(100))
