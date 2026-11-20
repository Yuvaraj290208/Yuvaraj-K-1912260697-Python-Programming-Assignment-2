import sys
import time
from functools import lru_cache


def ways_naive(n: int, counter: list[int]) -> int:
    counter[0] += 1
    if n <= 1:
        return 1
    return ways_naive(n - 1, counter) + ways_naive(n - 2, counter)


@lru_cache(maxsize=None)
def ways_memo(n: int) -> int:
    if n <= 1:
        return 1
    return ways_memo(n - 1) + ways_memo(n - 2)


def ways_redesigned(n: int) -> tuple[int, int]:
    if n <= 1:
        return 1, 0
    prev2, prev1 = 1, 1
    iterations = 0
    for _ in range(2, n + 1):
        iterations += 1
        prev2, prev1 = prev1, prev2 + prev1
    return prev1, iterations


if __name__ == "__main__":
    for n in (10, 20, 25, 30):
        cnt = [0]
        t0 = time.perf_counter()
        ans_naive = ways_naive(n, cnt)
        t_naive = time.perf_counter() - t0

        t0 = time.perf_counter()
        ans_red, iters = ways_redesigned(n)
        t_red = time.perf_counter() - t0

        assert ans_naive == ans_red
        print(
            f"n={n:>2} | naive calls={cnt[0]:>9} ({t_naive:.5f}s) | "
            f"redesigned iters={iters:>4} ({t_red:.6f}s)"
        )

    print(f"\nsys.getrecursionlimit() = {sys.getrecursionlimit()}")
    ways_memo.cache_clear()
    try:
        ways_memo(1000)
    except RecursionError as e:
        print(f"Original memoised recursion crashed at n=1000: {e}")

    t0 = time.perf_counter()
    ans_1000, iters_1000 = ways_redesigned(1000)
    t_1000 = time.perf_counter() - t0
    print(
        f"Redesigned iterative succeeded at n=1000: "
        f"{iters_1000} iterations in {t_1000:.6f}s (answer has {len(str(ans_1000))} digits)"
    )
  
