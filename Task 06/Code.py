import sys
from functools import lru_cache

calls = 0


def ways_naive(n: int) -> int:
    """Ways to climb n temple steps taking 1 or 2 steps at a time."""
    global calls
    calls += 1
    if n <= 1:
        return 1
    return ways_naive(n - 1) + ways_naive(n - 2)


@lru_cache(maxsize=None)
def ways_memo(n: int) -> int:
    global calls
    calls += 1
    if n <= 1:
        return 1
    return ways_memo(n - 1) + ways_memo(n - 2)


def ways_iterative(n: int) -> int:
    if n <= 1:
        return 1
    prev2, prev1 = 1, 1
    for _ in range(2, n + 1):
        prev2, prev1 = prev1, prev2 + prev1
    return prev1


if __name__ == "__main__":
    calls = 0
    print("naive:", ways_naive(25), "calls =", calls)
    calls = 0
    print("memo :", ways_memo(25), "calls =", calls)

    for n in range(1, 7):
        ways_memo.cache_clear()
        print(f"n={n}: {ways_iterative(n)} ways")

    for n in (10, 20, 25, 30):
        calls = 0
        ans_n = ways_naive(n)
        naive_calls = calls

        ways_memo.cache_clear()
        calls = 0
        ans_m = ways_memo(n)
        memo_calls = calls
        print(f"n={n:>2} | ways={ans_n:>7} | naive_calls={naive_calls:>9} | memo_calls={memo_calls:>3}")

    print("Current recursion limit:", sys.getrecursionlimit())
    ways_memo.cache_clear()
    try:
        print("memo(1000):", ways_memo(1000))
    except RecursionError as exc:
        print(f"ways_memo(1000) failed with RecursionError: {exc}")

    iter_1000 = ways_iterative(1000)
    print(f"ways_iterative(1000) succeeded! Digits={len(str(iter_1000))}")
  
