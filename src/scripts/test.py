import time


def fib():
    count = 0
    prev = [0, 1]
    t = int(time.time())
    while prev[-1] < t:
        n = prev[-1] + prev[-2]
        count += 1
	prev[0], prev[1] = prev[1], n
    return count
      
if __name__ == "__main__":
    print "this is a test"
    print fib()