# encoding: utf-8

from __future__ import (print_function,
                        division,
                        unicode_literals,
                        absolute_import)

def primes(max_num):
    # Es werden nur Primzahlen kleiner max_num berechnet
    is_prime = max_num * [1]
    is_prime[0] = 0
    is_prime[1] = 0

    primes = []

    # Sieb von Erathosthenes:
    for i in range(2, max_num):
        if is_prime[i]:
            for j in range(2 * i, max_num, i):
                # Alle Vielfachen sind keine Primzahl
                is_prime[j] = 0
            primes.append(i)
    
    return primes

print(primes(100))
