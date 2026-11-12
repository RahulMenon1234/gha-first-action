
def greet(name: str) -> str:
    return f"Hello, {name}! Welcome to Python."


def main():
    name = input("Enter your name: ")
    message = greet(name)
    print(message)


if __name__ == "__main__":
    main()
