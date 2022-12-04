"""tests the main.py function"""

from bldr_test import main


def test_main():
    """testing exit code 0; which actually tests for errors"""
    assert main.main() == 0


def test_print_randoms():
    """testing exit code 0; which actually tests for errors"""
    assert main.print_randoms(10) == 0


def test_write_randoms():
    "testing length of array returned"
    assert len(main.write_randoms(10)) == 10


def test_print_look_at_array_val():
    "testing that there is no return (this is kinda silly perhaps)"
    assert main.print_look_at_array_val([1, 2, 3]) is None
