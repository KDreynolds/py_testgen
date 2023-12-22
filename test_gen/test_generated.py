import pytest
import test_repo


def test_multiply():
    # Call the function with different arguments
    try:
        result = multiply(1, 2)
        assert result == 3, f"Expected 3, but got {result}"
        result = multiply(0, 0)
        assert result == 0, f"Expected 0, but got {result}"
        result = multiply(-1, -2)
        assert result == -3, f"Expected -3, but got {result}"
    except Exception as e:
        assert False, f"Function multiply raised an exception: {e}"


def test_power():
    # Call the function with different arguments
    try:
        result = power(1, 2)
        assert result == 3, f"Expected 3, but got {result}"
        result = power(0, 0)
        assert result == 0, f"Expected 0, but got {result}"
        result = power(-1, -2)
        assert result == -3, f"Expected -3, but got {result}"
    except Exception as e:
        assert False, f"Function power raised an exception: {e}"


def test_concatenate():
    # Call the function with different arguments
    try:
        result = concatenate(1, 2)
        assert result == 3, f"Expected 3, but got {result}"
        result = concatenate(0, 0)
        assert result == 0, f"Expected 0, but got {result}"
        result = concatenate(-1, -2)
        assert result == -3, f"Expected -3, but got {result}"
    except Exception as e:
        assert False, f"Function concatenate raised an exception: {e}"


def test_divide():
    # Call the function with different arguments
    try:
        result = divide(1, 2)
        assert result == 3, f"Expected 3, but got {result}"
        result = divide(0, 0)
        assert result == 0, f"Expected 0, but got {result}"
        result = divide(-1, -2)
        assert result == -3, f"Expected -3, but got {result}"
    except Exception as e:
        assert False, f"Function divide raised an exception: {e}"


def test_greet():
    # Call the function with different arguments
    try:
        result = greet(1, 2)
        assert result == 3, f"Expected 3, but got {result}"
        result = greet(0, 0)
        assert result == 0, f"Expected 0, but got {result}"
        result = greet(-1, -2)
        assert result == -3, f"Expected -3, but got {result}"
    except Exception as e:
        assert False, f"Function greet raised an exception: {e}"


def test_factorial():
    # Call the function with different arguments
    try:
        result = factorial(1, 2)
        assert result == 3, f"Expected 3, but got {result}"
        result = factorial(0, 0)
        assert result == 0, f"Expected 0, but got {result}"
        result = factorial(-1, -2)
        assert result == -3, f"Expected -3, but got {result}"
    except Exception as e:
        assert False, f"Function factorial raised an exception: {e}"


def test_fibonacci():
    # Call the function with different arguments
    try:
        result = fibonacci(1, 2)
        assert result == 3, f"Expected 3, but got {result}"
        result = fibonacci(0, 0)
        assert result == 0, f"Expected 0, but got {result}"
        result = fibonacci(-1, -2)
        assert result == -3, f"Expected -3, but got {result}"
    except Exception as e:
        assert False, f"Function fibonacci raised an exception: {e}"
