def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    while True:
        try:
            n = int(input("Enter the number of Fibonacci terms to generate: "))
            if n <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    values = list(fibonacci(n))
    print(values)

    plt.plot(range(n), values, marker="o")
    plt.title("Fibonacci Series")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.tight_layout()
    plt.savefig("fibonacci.png")
    plt.show()
