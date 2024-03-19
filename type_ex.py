from typing import TypeVar, Iterable, Sequence

# тип юнион возвращает и принимает либо одно либо другое и это ок
Number = int | float

# Женерик стогая типизация что заходитб то и должно выйти, в данном примере должны быть классы,
# если заходит класс реализации то и должен вернуться данный класс
T = TypeVar("T", int, str, float, list)


def calc(x: Number, y: Number) -> Number:
    return x + y


def calculator(x: T, y: T) -> T:
    return x + y

def total_length(items: Iterable[str]) -> int:
    return sum(len(x) for x in items)

def total_length_other(items: Sequence[str]) -> int:
    return sum(len(x) for x in items)


if __name__ == "__main__":
    print(calculator(3, 5))
    print(calculator("Hello", "World"))
    print(calculator(3.5, 4.5))

    print(calculator(4, 1.4))  # error
    print(calc(4, 1.4))  # not error

    print(total_length({"Volodymyr", "Ivan", "Dmitro"}))
    print(total_length(("Volodymyr", "Ivan", "Dmitro")))
    print(total_length(["Volodymyr", "Ivan", "Dmitro"]))

    print(total_length_other({"Volodymyr", "Ivan", "Dmitro"})) #error
    print(total_length_other(("Volodymyr", "Ivan", "Dmitro")))
    print(total_length_other(["Volodymyr", "Ivan", "Dmitro"]))
