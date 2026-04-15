# 202510814.py
# Data Structures I Assignment
# Topic: Recursion & Iteration (Fibonacci and Factorial)

class MathOperations:
    def factorial(self, n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)

    def fibonacci(self, n):
        if n < 0:
            raise ValueError("Fibonacci is not defined for negative numbers.")
        if n == 0:
            return 0
        elif n == 1:
            return 1
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    def fibonacci_series(self, n):
        series = []
        for i in range(n):
            series.append(self.fibonacci(i))
        return series


def main():
    math_obj = MathOperations()

    while True:
        print("\n===== MATH MENU =====")
        print("1. Calculate Factorial")
        print("2. Generate Fibonacci Series")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            try:
                num = int(input("Enter a number: "))
                result = math_obj.factorial(num)
                print(f"Factorial of {num} is {result}")
            except ValueError as e:
                print("Error:", e)

        elif choice == "2":
            try:
                num = int(input("Enter number of terms: "))
                series = math_obj.fibonacci_series(num)
                print("Fibonacci Series:", series)
            except ValueError as e:
                print("Error:", e)

        elif choice == "3":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
