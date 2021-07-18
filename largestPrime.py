def largestPrimeFactor(number):
    largest=0
    for prime in range(2,number):
        if number%prime==0:
            if isPrime(prime):
                if largest<prime:
                    largest=prime
    return largest

def isPrime(pri):
    for num in range(2,pri):
        if pri%num==0:
            return False
    return True

print(largestPrimeFactor(13195))