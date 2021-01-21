from prime.helpers import *
import prime.constants as c


class Prime:
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish

    def calculate_primes(self):
        primes = []
        for n in range(self.start, self.finish):
            if is_prime(n) and n not in c.SKIP_RANGE:
                primes.append(n)
        return primes

    def prettify(self):
        body = ''
        for result in self.calculate_primes():
            body += f"This is a prime number: {result} \n"

        return body