"""Print the Collatz sequence starting at 27 and the number of transitions."""


def collatz(start):
    """Return the Collatz sequence from start down to 1, inclusive."""
    n = start
    sequence = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence


def main():
    sequence = collatz(27)
    for n in sequence:
        print(n)
    transitions = len(sequence) - 1
    print(f"Total transitions: {transitions}")


if __name__ == "__main__":
    main()
