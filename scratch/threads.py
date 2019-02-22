from multiprocessing.pool import ThreadPool as Pool
# from multiprocessing.pool import Pool  # to use multiprocessing
import os
from time import time

import requests


URLS = [
    # 'http://python.org/about',
    'http://pymotw.com/2/collections/deque.html',
    'https://docs.python.org/2/library/multiprocessing.html',
    'http://pythong.org',
    'http://pythong.org/morehoff.html',
    'http://en.wikipedia.org/wiki/Portal:Current_events',
    'http://en.wikipedia.org/wiki/Main_page',
    'http://pymotw.com/2/',
    'http://www-news.iaea.org/EventList.aspx?ps=100&pno=0',
   ]


def timeit(func):
    def wrapper(*args, **kwargs):
        t0 = time()
        value = func(*args, **kwargs)
        print("{} took {:.1f}s".format(func.__name__, time() - t0))
        return value
    return wrapper


@timeit
def nothreads(urls):
    results = []
    for url in urls:
        results.append(requests.get(url))
    return results


@timeit
def twothreads(urls):
    pool = Pool(2)
    results = pool.map(requests.get, urls)
    return results


@timeit
def eightthreads(urls):
    pool = Pool(8)
    results = pool.map(requests.get, urls)
    return results


if __name__ == '__main__':
    print("Starting {}".format(os.getpid()))
    nothreads(URLS)
    twothreads(URLS)
    # eightthreads(URLS)
