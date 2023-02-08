"""main function code"""


import random
from typing import TypeVar

import typer

app = typer.Typer()
random.seed(12)


def write_randoms(num_to_write: int) -> list[float]:
    """write randoms"""
    return [random.random() for _ in range(num_to_write)]


T = TypeVar("T")


# ugh, won't let me use type variable because not using for enough constraint
# I kinda get it, since it's not going to create specialized sub functions
# but also seems to complain about 'Any'
# and I'm not sure how to provide a trait-like element
# so that it only takes types thatre *`printable`* for example
def print_look_at_array_val(array: list[int | float]) -> None:
    """print look at array val"""
    for val in array:
        print(f"Look at this array value: {val}")


def print_randoms(times_printed: int) -> int:
    """randoms"""
    array = write_randoms(times_printed)
    print_look_at_array_val(array)
    return 0


@app.command()
def main() -> int:
    """main function"""
    returncode = print_randoms(10)

    return returncode
