from typing import Callable


def foo():
    return "Hello world"


def call_function(func: Callable[[], str]) -> int:
    return len(func())


if __name__ == "__main__":
    print(call_function(foo))
