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

    for x in candidates:
        multiple = 2
        while x * multiple <= max(candidates):
            if x * multiple in candidates:
                candidates.remove(x * multiple)
            multiple += 1
        primes.append(x)

    return primes
