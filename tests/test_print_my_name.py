

from src.mfdomain import print_my_name


def test_say_hi():
    assert print_my_name.say_hi(message="Hello") == "Hello"
    assert print_my_name.say_hi(message=6) == "INVALID"
