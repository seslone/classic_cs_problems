import time

from classic_cs_problems.chapter_1.fibonacci import fib, fib5


def test_fib_short():
    startTime = time.time()
    fib5_result = fib5(100)
    executionTime = time.time() - startTime
    print("Execution time in seconds: " + str(executionTime))

    startTime_1 = time.time()
    fib_list = fib(100)
    executionTime_1 = time.time() - startTime_1
    print("Execution time in seconds: " + str(executionTime_1))
    fib5_list = [item for item in fib5_result]
    assert executionTime >= executionTime_1
    assert fib5_list == fib_list


def test_fib_long():
    startTime = time.time()
    fib5_result = fib5(100000)
    executionTime = time.time() - startTime
    print("Execution time in seconds: " + str(executionTime))

    startTime_1 = time.time()
    fib_list = fib(100000)
    executionTime_1 = time.time() - startTime_1
    print("Execution time in seconds: " + str(executionTime_1))
    fib5_list = [item for item in fib5_result]
    # TODO: make my function faster than the yield!
    assert executionTime <= executionTime_1
    assert fib5_list == fib_list
