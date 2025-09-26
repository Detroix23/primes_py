"""
PRIMES
__main__.py
Try to find prime numbers efficently
"""
import modules.search as search

def main() -> None:
    n1 = search.check(400001)
    print("n1:", n1)
    
    print(search.search_only_primes(250000, "main"))
    
    """
    maximum = 500000
    for i in range(100000, maximum, 100000):
        print(search.search_only_primes(i))
    """
    
    
if __name__ == "__main__":
    main()
    
    
    
    
    