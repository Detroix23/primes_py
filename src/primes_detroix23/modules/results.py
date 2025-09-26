"""
PRIMES
results.py
"""

class PrimeResult:
    number: int
    prime: bool
    time_elapsed: float
    
    def __init__(self, number: int, prime: bool, time_elapsed: float) -> None:
        self.number = number
        self.prime = prime
        self.time_elapsed = time_elapsed
    
    def __str__(self) -> str:
        return f"PrimeResult: {self.number}, prime: {self.prime}, time: {self.time_elapsed:.2f}"
    

class TestResult:
    time_elapsed: float
    upper_limit: int
    lower_limit: int
    results: set[int]
    
    def __init__(
        self, 
        time_elapsed: float, 
        upper_limit: int, 
        lower_limit: int = 0, 
        results: set[int] = set()
    ) -> None:
        self.time_elapsed: float = time_elapsed
        self.upper_limit: int = upper_limit
        self.lower_limit: int = lower_limit
        self.results: set[int] = results

    def __str__(self) -> str:
        return f"""TestResults:
    - Time: {self.time_elapsed:.2f}s
    - Limits: {self.lower_limit}, {self.upper_limit}
    - Results: {list(self.results)[-20:]}
"""
