def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    import sys
    import matplotlib.pyplot as plt

    n = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    values = list(fibonacci(n))
    print(values)

    plt.plot(range(n), values, marker="o")
    plt.title("Fibonacci Series")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.tight_layout()
    plt.savefig("fibonacci.png")
    plt.show()
