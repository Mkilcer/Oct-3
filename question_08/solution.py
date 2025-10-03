"""
Question 8: Fibonacci Sequence
Write a program that generates the Fibonacci sequence up to n terms.
"""

def fibonacci(n):
    """Generate first n numbers in Fibonacci sequence"""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence

def main():
    n = 10
    result = fibonacci(n)
    print(f"First {n} Fibonacci numbers: {result}")

if __name__ == "__main__":
    main()
