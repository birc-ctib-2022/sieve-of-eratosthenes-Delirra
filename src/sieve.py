"""Computing primes."""


def sieve(n: int) -> list[int]:
    """
    Compute all the primes up to (and possibly including) `n`.

    `n` must be positive.

    >>> sieve(15)
    [2, 3, 5, 7, 11, 13]

    """
    assert n > 0
    candidates = list(range(2, n + 1))
    primes = []
    # FIXME: fill out this bit

    for i in range(n - 1):
        if candidates[i] == None:
            continue

        tag = candidates[i]
        for j in range(i + tag, n - 1, tag):
            candidates[j] = None

    primes = [idx for idx in candidates if idx != None]

    return primes
print(sieve(432))