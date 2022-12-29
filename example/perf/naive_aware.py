from pydate import add_days
import random
import datetime
import time


ITERATIONS = 1000000


def do_naive():
    random.seed(10)
    start = time.perf_counter()
    for i in range(ITERATIONS):
        date = datetime.datetime.utcnow()
    end = time.perf_counter()
    print(f"Naive: {end - start}")
    return end - start


def do_aware():
    random.seed(10)
    start = time.perf_counter()
    for i in range(ITERATIONS):
        date = datetime.datetime.now(datetime.timezone.utc)
    end = time.perf_counter()
    print(f"Aware: {end - start}")
    return end - start


if __name__ == "__main__":
    a = do_naive()
    b = do_aware()
    print(f"b runs {b/a:.2%} faster than a")

    # this is why i am choosing to use naive dates
