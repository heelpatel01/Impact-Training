def fibonacci(n):
    fib_sequence = [0, 1]

    while len(fib_sequence) < n:
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)

    return fib_sequence

# Example: Print the first 10 terms of the Fibonacci sequence
n_terms = 10
fibonacci_sequence = fibonacci(n_terms)

print(f"Fibonacci Sequence (first {n_terms} terms):")
print(fibonacci_sequence)
