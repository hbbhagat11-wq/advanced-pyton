class Fibonacci:
    def __init__(self, n: int):
        self.n = n

    # Recursive method
    def recursive(self, n=None):
        if n is None:
            n = self.n

        if n <= 1:
            return n

        return self.recursive(n - 1) + self.recursive(n - 2)

    # Dynamic Programming (Iterative)
    def dynamic(self):
        if self.n <= 0:
            return 0
        elif self.n == 1:
            return 1

        a, b = 0, 1

        for _ in range(2, self.n + 1):
            a, b = b, a + b

        return b

    # Display Fibonacci sequence
    def display_sequence(self):
        sequence = []

        a, b = 0, 1

        for _ in range(self.n):
            sequence.append(a)
            a, b = b, a + b

        return sequence


class MainProgram:
    @staticmethod
    def main():
        try:
            n = int(input("Enter the value of n: "))

            if n < 0:
                print("Please enter a non-negative integer.")
                return

            fib = Fibonacci(n)

            print("\nFibonacci Sequence:")
            print(fib.display_sequence())

            print(f"\nRecursive Fibonacci({n}) = {fib.recursive()}")
            print(f"Dynamic Fibonacci({n}) = {fib.dynamic()}")

        except ValueError:
            print("Invalid input! Please enter an integer.")


if __name__ == "__main__":
    MainProgram.main()