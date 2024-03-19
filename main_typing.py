from typing import TypedDict, Literal, NamedTuple
from dataclasses import dataclass


class UserInfo(TypedDict):
    id: int
    username: str
    email: str
    is_active: bool


@dataclass(frozen=True)
class UserScheme:
    id: int
    username: str
    email: str
    is_active: bool


class Cat(NamedTuple):
    nick: str
    age: int


User = {
    "id": 123,
    "username": "Dan",
    "email": "dan_013043@gmail.com",
    "is_active": True,
}


def get_user() -> UserInfo:
    return User


def get_user_info() -> UserScheme:
    return UserScheme(
        id=123,
        username="Dan",
        email="dan_013043@gmail.com",
    )


def my_mul(data: list) -> float:
    result = 1
    for num in data:
        result = result * num
    return result


Shape = Literal["circle", "square"]


def foo(shape):
    if shape == "circle":
        print("It`s circle")
    if shape == "square":
        print("It`s a square")


if __name__ == "__main__":
    my_mul([2])
    print(get_user()["email"])
    foo("saw")
    cat = Cat(nick="Barsik", age=5)
    print(cat.nick)
