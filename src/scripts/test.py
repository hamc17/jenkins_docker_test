import time


def epoch_fib_count():
    """
    Gets the number of of the first fibonacci number greater
    than the current time in epoch seconds
    """

    count = 2
    # initial numbers need to be set as 0 & 1
    prev = [0, 1]
    t = int(time.time())
    n = 0
    while prev[-1] < t:
        n = prev[-1] + prev[-2]
        count += 1
    prev[0], prev[1] = prev[1], n
    return count, n

if __name__ == "__main__":
    print epoch_fib_count()
