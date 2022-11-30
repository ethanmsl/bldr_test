"""main function code"""


import random

random.seed(12)

def print_randoms(times_printed: int) -> int:
    """randoms"""
    for _ in range(times_printed):
        print(f"Look, here's a random number {random.random()}")

    return 0

def main() -> int:
    """main function"""
    returncode = print_randoms(10)

    return returncode
