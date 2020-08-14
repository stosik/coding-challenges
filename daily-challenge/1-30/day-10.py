# This problem was asked by Apple.

# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

import time

def scheduler(f, n):
    time.sleep(n)
    f()

def hello_world():
    print("Hello World")


scheduler(hello_world, 1)