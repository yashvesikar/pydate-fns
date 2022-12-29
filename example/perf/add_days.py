from pydate import add_days
import random
import datetime
import time


ITERATIONS = 100000


def do_native():
    random.seed(10)
    start = time.perf_counter()
    for i in range(ITERATIONS):
        date = datetime.datetime.now()
        date = date + datetime.timedelta(days=random.randint(1, 100))
    end = time.perf_counter()
    print(f"Native: {end - start}")


def do_pydate():
    random.seed(10)
    start = time.perf_counter()
    for i in range(ITERATIONS):
        date = datetime.datetime.now()
        date = add_days(date, random.randint(1, 100))
    end = time.perf_counter()
    print(f"Pydate: {end - start}")


if __name__ == "__main__":
    do_native()
    do_pydate()
