
from src.main import greet


def test_greet():
    result = greet("Rahul")

    assert result == "Hello, Rahul! Welcome to Python."
