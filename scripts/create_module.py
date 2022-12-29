def main(name: str) -> None:
    # create a directory for the module
    # create a __init__.py file
    # create a test.py file
    # create a {name}.py file

    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "pydate"))

    os.makedirs(name)

    with open(os.path.join(name, "__init__.py"), "w") as f:
        f.write(f"from .{name} import {name}")

    with open(os.path.join(name, f"{name}.py"), "w") as f:
        f.write(
            f"""
from datetime import datetime

def {name}(date: datetime) -> datetime:
    pass
"""
        )

    with open(os.path.join(name, "test.py"), "w") as f:
        f.write(
            f"""
import unittest
from datetime import datetime
from .{name} import {name}

class Test{name}(unittest.TestCase):
    def test_{name}(self) -> None:
        pass
"""
        )

    print("\033c")
    print(f"NOTE: Add {name} to pydate/__init__.py")


if __name__ == "__main__":
    import argparse
    import os

    parser = argparse.ArgumentParser()
    parser.add_argument("-m", help="The name of the module to create")
    args = parser.parse_args()

    main(args.m)  # type: ignore
