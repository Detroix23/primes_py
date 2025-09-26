"""
PRIMES
search.py
"""
import time
from typing import Callable

import modules.results as results
import modules.saves as saves

def check_naive(n: int) -> bool:
    """
    "Naive way". Check every number from 2 to n, and check the modulo.
    Still includes starting from 2, going to half of the number, steping 
    2 number each time.
    """
    iterator: int = 3
    # Init with modulo of 2, to remove all multiple of 2 modulos.
    is_prime: bool = n % 2 != 0
    while iterator < ((n // 2) + 1) and is_prime:
        is_prime = (n % iterator != 0)
        
        iterator += 2
        
    return is_prime


def check(n: int) -> results.PrimeResult:
    """
    Alias for the current best accepted primality checker.
    """
    time_elapsed: float = time.monotonic()
    primality: bool = check_naive(n)
    time_elapsed =  time.monotonic() - time_elapsed
    return results.PrimeResult(
        n, 
        primality,
        time_elapsed
    )


def search_only_primes(limit: int, file_name: str = "") -> results.TestResult:
    """
    Search all the primes, and return a set of int.
    Each modulo are only prime numbers. 
    Because if the number is not dividable by n in N, it cannot be divided by
    n * k, for any k in N.
    Check each numbers from 3, or need a save file for already found prime numbers.
    """
    known: list[int] = []
    current: int = 3
    time_elapsed: float = time.monotonic()
    
    if file_name:
        known = saves.read(file_name, raise_type=True)
    if not known:
        known = [2, 3]
    else:
        current = known[-1] + 2

        
    
    while current <= limit:
        is_prime: bool = True
        iterator_known: int = 0
        tester: int = 2
        mid: int = current // 2 + 1
        in_known: bool = True
        
        while in_known and is_prime and tester < mid:
            is_prime = current % tester != 0
            
            iterator_known += 1
            tester = known[iterator_known]
            
            in_known = iterator_known <= len(known) - 1
            
        while not in_known and is_prime and tester < mid:
            is_prime = current % tester != 0
            
            tester += 2
        
        if is_prime:
            known.append(current)
        
        current += 2
    
    time_elapsed = time.monotonic() - time_elapsed
    
    if file_name:
        saves.save_list(known, file_name)
    
    return results.TestResult(time_elapsed, limit, 0, set(known))


def test(limit: int, function: Callable[[int], bool]) -> results.TestResult:
    """
    Test a primality function.
    """
    run_time: float = time.monotonic()
    result: set[int] = set() 
    for n in range(0, limit):
        if function(n):
            result.add(n)
    run_time = time.monotonic() - run_time
    
    return results.TestResult(run_time, limit, 0, result)
 