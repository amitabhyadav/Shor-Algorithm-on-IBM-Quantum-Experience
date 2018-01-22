from math import sqrt

def sieve_of_eratosthenes(n):
    primes = range(3, n + 1, 2) # primes above 2 must be odd so start at three and increase by 2
    for base in xrange(len(primes)):
        if primes[base] is None:
           continue
        if primes[base] >= sqrt(n): # stop at sqrt of n
            break
        for i in xrange(base + (base + 1) * primes[base], len(primes), primes[base]):
            primes[i] = None
    primes.insert(0,2)
    sieve=filter(None, primes)
    return  sieve

def prime_factor(sieve,n):
    p_f = []
    for prime in sieve:
        while n % prime == 0:
            p_f.append(prime)
            n /= prime
    if n > 1:
        p_f.append(n)
    return p_f

def p_fctr_exp(s,n):
    primes = prime_factor(s,n)
    exp=[]
    for p in primes:
        e=0
        while (n%p==0):
            n=n//p       # since p still divides n,
            e+=1         # we divide n by p and increase the exponent
        exp.append(e)
    return exp

def checkEqual1(iterator):
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == rest for rest in iterator)

num = input("Enter a number: ")
sieve = sieve_of_eratosthenes(num)
pf = prime_factor(sieve,num)
expo = p_fctr_exp(sieve,num)
print pf
print expo
chk = checkEqual1(pf)
print chk
if chk == True:
    print pf[0]
    print expo[0]
input()
    

    


